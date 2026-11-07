"""Exercise output downloads through public clients, real HTTP and owned files."""

import asyncio
import json
import threading
from concurrent.futures import ThreadPoolExecutor
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

import httpx
import pytest

from magic_hour import AsyncClient, Client


@pytest.fixture
def output_server():
    class Server(HTTPServer):
        outputs = ["/first/output.png", "/second/output.png"]
        requests = []

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def do_GET(self):
            server.requests.append(self.path)
            if self.path.startswith("/disconnect/"):
                self.close_connection = True
                return
            if self.path.startswith("/v1/"):
                family = self.path.split("/")[2].split("-")[0]
                payload = {
                    "id": "test-project",
                    "status": "complete",
                    "created_at": "2026-10-22T00:00:00Z",
                    "credits_charged": 0,
                    "enabled": True,
                    "error": None,
                    "name": "local download test",
                    "type": {
                        "image": "AI_IMAGE",
                        "video": "TEXT_TO_VIDEO",
                        "audio": "MUSIC_GENERATOR",
                    }[family],
                    "downloads": [
                        {"url": base_url + path, "expires_at": "2099-01-01T00:00:00Z"}
                        for path in server.outputs
                    ],
                }
                if family == "image":
                    payload.update(image_count=len(server.outputs), total_frame_cost=0)
                elif family == "video":
                    payload.update(
                        download=None,
                        end_seconds=1,
                        start_seconds=0,
                        fps=24,
                        height=512,
                        width=512,
                        total_frame_cost=0,
                    )
                body = json.dumps(payload).encode()
                self.send_response(200)
            elif self.path.startswith("/error/"):
                body = b"expired output"
                self.send_response(403)
            else:
                body = self.path.encode()
                self.send_response(200)
            self.send_header(
                "Content-Type",
                (
                    "application/json"
                    if self.path.startswith("/v1/")
                    else "application/octet-stream"
                ),
            )
            self.send_header(
                "Content-Length",
                str(len(body) + (50 if self.path.startswith("/truncated/") else 0)),
            )
            self.end_headers()
            self.wfile.write(body)
            self.close_connection = True

    server = Server(("127.0.0.1", 0), Handler)
    base_url = f"http://127.0.0.1:{server.server_port}"
    server.url = base_url
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield server
    finally:
        server.shutdown()
        thread.join(timeout=5)
        server.server_close()


@pytest.fixture(params=["image", "video", "audio"])
def family(request):
    return request.param


@pytest.fixture(params=[False, True], ids=["sync", "async"])
def check_result(request, output_server, family):
    def run(directory):
        kwargs = dict(
            id="test-project",
            wait_for_completion=True,
            download_outputs=True,
            download_directory=None if directory is None else str(directory),
        )
        if request.param:

            async def run_async():
                async with httpx.AsyncClient(trust_env=False) as http_client:
                    client = AsyncClient(
                        base_url=output_server.url,
                        token="local-test-only",
                        httpx_client=http_client,
                    )
                    return await getattr(client.v1, f"{family}_projects").check_result(
                        **kwargs
                    )

            return asyncio.run(run_async())
        with httpx.Client(trust_env=False) as http_client:
            client = Client(
                base_url=output_server.url,
                token="local-test-only",
                httpx_client=http_client,
            )
            return getattr(client.v1, f"{family}_projects").check_result(**kwargs)

    return run


def test_same_basename_outputs_keep_distinct_bytes(
    check_result, output_server, tmp_path
):
    result = check_result(tmp_path)
    paths = result.downloaded_paths
    assert len(paths) == len(set(paths)) == 2
    assert [Path(path).read_bytes() for path in paths] == [
        path.encode() for path in output_server.outputs
    ]
    assert all(Path(path).parent == tmp_path for path in paths)


def test_existing_file_suffix_and_symlink_stay_untouched(
    check_result, output_server, tmp_path
):
    output_server.outputs = ["/first/output.png"]
    original = tmp_path / "output.png"
    original.write_bytes(b"user file")
    target = tmp_path / "owned-target.png"
    target.write_bytes(b"symlink target")
    link = tmp_path / "output_1.png"
    link.symlink_to(target)
    occupied = tmp_path / "output_2.png"
    occupied.mkdir()
    result = check_result(tmp_path)
    assert original.read_bytes() == b"user file"
    assert link.is_symlink() and target.read_bytes() == b"symlink target"
    assert occupied.is_dir()
    assert result.downloaded_paths == [str(tmp_path / "output_3.png")]
    assert Path(result.downloaded_paths[0]).read_bytes() == b"/first/output.png"


@pytest.mark.parametrize("dangling", [False, True], ids=["symlink", "dangling-symlink"])
def test_default_directory_preserves_symlink(
    check_result, output_server, tmp_path, monkeypatch, dangling
):
    output_server.outputs = ["/first/output.png"]
    monkeypatch.chdir(tmp_path)
    target = tmp_path / "owned-target.png"
    if not dangling:
        target.write_bytes(b"user target")
    link = tmp_path / "output.png"
    link.symlink_to(target)
    result = check_result(None)
    assert link.is_symlink()
    if dangling:
        assert not target.exists()
    else:
        assert target.read_bytes() == b"user target"
    assert result.downloaded_paths == ["output_1.png"]
    assert Path(result.downloaded_paths[0]).read_bytes() == b"/first/output.png"


def test_retry_completed_project_preserves_previous_downloads(
    check_result, output_server, tmp_path
):
    first = check_result(tmp_path)
    second = check_result(tmp_path)
    paths = first.downloaded_paths + second.downloaded_paths
    assert len(paths) == len(set(paths)) == 4
    assert [Path(path).read_bytes() for path in first.downloaded_paths] == [
        path.encode() for path in output_server.outputs
    ]
    assert [Path(path).read_bytes() for path in second.downloaded_paths] == [
        path.encode() for path in output_server.outputs
    ]
    assert (
        len([path for path in output_server.requests if path.startswith("/v1/")]) == 2
    )


@pytest.mark.parametrize("failure", ["error", "truncated", "disconnect"])
def test_http_failure_keeps_user_file_and_retry_recovers(
    check_result, output_server, tmp_path, failure
):
    original = tmp_path / "output.png"
    original.write_bytes(b"user file")
    output_server.outputs = [f"/{failure}/output.png", "/later/output.png"]
    expected_error = (
        httpx.HTTPStatusError if failure == "error" else httpx.RemoteProtocolError
    )
    with pytest.raises(expected_error):
        check_result(tmp_path)
    assert list(tmp_path.iterdir()) == [original]
    assert original.read_bytes() == b"user file"
    assert "/later/output.png" not in output_server.requests
    output_server.outputs = ["/recovered/output.png", "/later/output.png"]
    result = check_result(tmp_path)
    assert original.read_bytes() == b"user file"
    assert [Path(path).read_bytes() for path in result.downloaded_paths] == [
        path.encode() for path in output_server.outputs
    ]


@pytest.mark.parametrize("url_path", ["/", "/first/.."])
def test_missing_filename_does_not_write_outside_directory(
    check_result, output_server, tmp_path, url_path
):
    directory = tmp_path / "downloads"
    directory.mkdir()
    output_server.outputs = [url_path]
    with pytest.raises(ValueError, match="Download URL must include a filename"):
        check_result(directory)
    assert list(tmp_path.iterdir()) == [directory]
    assert list(directory.iterdir()) == []


def test_concurrent_downloads_reserve_distinct_paths(output_server, tmp_path):
    from magic_hour.helpers.download import download_files_async, download_files_sync
    from magic_hour.types.models import V1ImageProjectsGetResponseDownloadsItem

    downloads = [
        V1ImageProjectsGetResponseDownloadsItem(
            url=output_server.url + "/first/output.png",
            expires_at="2099-01-01T00:00:00Z",
        )
    ]

    def sync():
        return download_files_sync(downloads, str(tmp_path))[0]

    async def asynchronous():
        return await asyncio.gather(
            *(download_files_async(downloads, str(tmp_path)) for _ in range(2))
        )

    with ThreadPoolExecutor(max_workers=2) as pool:
        paths = list(pool.map(lambda _: sync(), range(2)))
    paths += [result[0] for result in asyncio.run(asynchronous())]
    assert len(paths) == len(set(paths)) == 4
    assert all(Path(path).read_bytes() == b"/first/output.png" for path in paths)
