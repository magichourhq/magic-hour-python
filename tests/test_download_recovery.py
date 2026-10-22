"""Failure recovery through public clients, loopback HTTP and real owned files."""

import asyncio
import builtins
import errno
import os
import threading
from pathlib import Path

import httpx
import pytest

import magic_hour.helpers.download as downloader
from magic_hour import AsyncClient
from test_download_collisions import check_result, family, output_server


@pytest.fixture
def failed_write(monkeypatch, tmp_path):
    """Inject only after a real exclusive open and real partial write/flush."""
    error = OSError(errno.ENOSPC, "injected local disk failure")
    state = {"stage": "write", "replace": None, "files": [], "close_error": None}

    class File:
        def __init__(self, file):
            self.file = file
            state["files"].append(file)

        def __enter__(self):
            return self

        def __exit__(self, *args):
            self.close()

        def fileno(self):
            return self.file.fileno()

        def write(self, content):
            if Path(self.file.name).name != "output_2.png":
                return self.file.write(content)
            self.file.write(content[:3])
            self.file.flush()
            if state["replace"]:
                # Keep original inode alive to distinguish replacement even after close.
                os.rename(self.file.name, tmp_path / "moved-partial")
                if state["replace"] == "file":
                    Path(self.file.name).write_bytes(b"replacement file")
                else:
                    Path(self.file.name).symlink_to(tmp_path / "target")
            if state["stage"] == "write":
                raise state["error"]
            return len(content)

        def close(self):
            fail = (
                not self.file.closed
                and Path(self.file.name).name == "output_2.png"
                and state["stage"] == "close"
            )
            self.file.close()
            if fail:
                raise state["error"]
            if state["close_error"]:
                raise state["close_error"]

    def open_file(path, mode):
        return File(builtins.open(path, mode))

    monkeypatch.setattr(downloader, "open", open_file, raising=False)
    state["error"] = error
    return state


def occupied_destinations(tmp_path):
    (tmp_path / "output.png").write_bytes(b"user file")
    (tmp_path / "target").write_bytes(b"symlink target")
    (tmp_path / "output_1.png").symlink_to(tmp_path / "target")


@pytest.mark.parametrize("stage", ["write", "close"])
def test_failed_file_removed_and_same_id_retry_recovers(
    check_result, output_server, tmp_path, failed_write, monkeypatch, stage
):
    occupied_destinations(tmp_path)
    output_server.outputs = [
        "/first/first.png",
        "/failed/output.png",
        "/later/later.png",
    ]
    failed_write["stage"] = stage
    with pytest.raises(OSError) as caught:
        check_result(tmp_path)
    assert caught.value is failed_write["error"]
    assert all(file.closed for file in failed_write["files"])
    assert (tmp_path / "first.png").read_bytes() == b"/first/first.png"
    assert (tmp_path / "output.png").read_bytes() == b"user file"
    assert (tmp_path / "output_1.png").is_symlink()
    assert (tmp_path / "target").read_bytes() == b"symlink target"
    assert not (tmp_path / "output_2.png").exists()
    assert "/later/later.png" not in output_server.requests
    monkeypatch.delattr(downloader, "open")
    result = check_result(tmp_path)
    assert [Path(path).name for path in result.downloaded_paths] == [
        "first_1.png",
        "output_2.png",
        "later.png",
    ]
    assert [Path(path).read_bytes() for path in result.downloaded_paths] == [
        path.encode() for path in output_server.outputs
    ]
    assert len([p for p in output_server.requests if p.startswith("/v1/")]) == 2


@pytest.mark.parametrize("replacement", ["file", "symlink"])
def test_failed_write_preserves_replacement_destination(
    check_result, output_server, tmp_path, failed_write, monkeypatch, replacement
):
    occupied_destinations(tmp_path)
    output_server.outputs = ["/failed/output.png"]
    failed_write["replace"] = replacement
    with pytest.raises(OSError) as caught:
        check_result(tmp_path)
    assert caught.value is failed_write["error"]
    candidate = tmp_path / "output_2.png"
    if replacement == "file":
        assert candidate.read_bytes() == b"replacement file"
    else:
        assert candidate.is_symlink()
        assert candidate.read_bytes() == b"symlink target"
    assert (tmp_path / "moved-partial").read_bytes() == b"/fa"
    monkeypatch.delattr(downloader, "open")
    result = check_result(tmp_path)
    assert result.downloaded_paths == [str(tmp_path / "output_3.png")]


def test_cleanup_denied_keeps_original_error_and_retry_recovers(
    check_result, output_server, tmp_path, failed_write, monkeypatch
):
    occupied_destinations(tmp_path)
    output_server.outputs = ["/failed/output.png"]
    real_unlink = os.unlink

    def denied(path, *args, **kwargs):
        if str(path) == str(tmp_path / "output_2.png"):
            raise PermissionError(errno.EACCES, "injected cleanup denial")
        return real_unlink(path, *args, **kwargs)

    with monkeypatch.context() as patch:
        patch.setattr(os, "unlink", denied)
        with pytest.raises(OSError) as caught:
            check_result(tmp_path)
    assert caught.value is failed_write["error"]
    assert (tmp_path / "output_2.png").read_bytes() == b"/fa"
    monkeypatch.delattr(downloader, "open")
    result = check_result(tmp_path)
    assert result.downloaded_paths == [str(tmp_path / "output_3.png")]


def test_write_eexist_is_not_a_filename_collision(
    check_result, output_server, tmp_path, failed_write
):
    occupied_destinations(tmp_path)
    output_server.outputs = ["/failed/output.png", "/later/later.png"]
    error = failed_write["error"] = FileExistsError(errno.EEXIST, "write failed")
    with pytest.raises(FileExistsError) as caught:
        check_result(tmp_path)
    assert caught.value is error
    assert not (tmp_path / "output_2.png").exists()
    assert not (tmp_path / "output_3.png").exists()
    assert "/later/later.png" not in output_server.requests


def test_secondary_close_error_does_not_hide_write_error(
    check_result, output_server, tmp_path, failed_write
):
    occupied_destinations(tmp_path)
    output_server.outputs = ["/failed/output.png"]
    failed_write["close_error"] = OSError(errno.EIO, "secondary close failure")
    with pytest.raises(OSError) as caught:
        check_result(tmp_path)
    assert caught.value is failed_write["error"]
    assert not (tmp_path / "output_2.png").exists()
    assert all(file.closed for file in failed_write["files"])


def test_cancel_during_http_body_keeps_completed_output_and_retry_recovers(
    output_server, family, tmp_path
):
    started, release = threading.Event(), threading.Event()
    base_handler = output_server.RequestHandlerClass

    class Handler(base_handler):
        def do_GET(self):
            if not self.path.startswith("/slow/"):
                return super().do_GET()
            output_server.requests.append(self.path)
            self.send_response(200)
            self.send_header("Content-Type", "application/octet-stream")
            self.send_header("Content-Length", "100")
            self.end_headers()
            self.wfile.write(b"partial HTTP body")
            self.wfile.flush()
            started.set()
            release.wait(5)
            self.close_connection = True

    output_server.RequestHandlerClass = Handler
    output_server.outputs = ["/first/first.png", "/slow/output.png", "/later/later.png"]

    async def run():
        async with httpx.AsyncClient(trust_env=False) as http_client:
            client = AsyncClient(
                base_url=output_server.url,
                token="local-test-only",
                httpx_client=http_client,
            )
            projects = getattr(client.v1, f"{family}_projects")
            kwargs = dict(
                id="test-project",
                wait_for_completion=True,
                download_outputs=True,
                download_directory=str(tmp_path),
            )
            task = asyncio.create_task(projects.check_result(**kwargs))
            try:
                assert await asyncio.to_thread(started.wait, 3)
                task.cancel()
                with pytest.raises(asyncio.CancelledError):
                    await task
                assert sorted(p.name for p in tmp_path.iterdir()) == ["first.png"]
                assert (tmp_path / "first.png").read_bytes() == b"/first/first.png"
                assert "/later/later.png" not in output_server.requests
            finally:
                release.set()
                if not task.done():
                    task.cancel()
                    with pytest.raises(asyncio.CancelledError):
                        await task
            output_server.outputs = [
                "/first/first.png",
                "/recovered/output.png",
                "/later/later.png",
            ]
            result = await projects.check_result(**kwargs)
            assert [Path(p).name for p in result.downloaded_paths] == [
                "first_1.png",
                "output.png",
                "later.png",
            ]
            assert [Path(p).read_bytes() for p in result.downloaded_paths] == [
                p.encode() for p in output_server.outputs
            ]

    asyncio.run(run())
