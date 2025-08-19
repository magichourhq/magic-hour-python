from typing import Protocol, TypeVar, Dict, Any, cast
from typing_extensions import ParamSpec

from magic_hour.core.base_client import AsyncBaseClient
from magic_hour.resources.v1.files.client import AsyncFilesClient, FilesClient
from magic_hour.core import SyncBaseClient

P = ParamSpec("P")
R_co = TypeVar("R_co", covariant=True)


class HasCreateAndBaseClient(Protocol[P, R_co]):
    _base_client: SyncBaseClient

    def create(self, *args: P.args, **kwargs: P.kwargs) -> R_co: ...


class GenerateMixin:
    def generate(
        self: HasCreateAndBaseClient[P, R_co],
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> R_co:
        print("generate")
        print(args)
        print(kwargs)

        assets = kwargs.get("assets")
        if assets is None:
            # If no assets, just call create directly
            return self.create(*args, **kwargs)

        # 1️⃣ Upload any files with keys ending in '_file_path'
        uploader = FilesClient(base_client=self._base_client)

        # Make a copy to avoid mutating the original
        # Cast to help type checker understand this is a dictionary
        assets_dict = cast(Dict[str, Any], assets)
        assets_copy: Dict[str, Any] = dict(assets_dict)

        # Find and upload all file path keys
        for key, value in assets_dict.items():
            if key.endswith("_file_path") and isinstance(value, str):
                # Check if this looks like a local file path (not already uploaded)
                if not value.startswith(("http://", "https://", "api-assets/")):
                    print(f"Uploading file for key '{key}': {value}")
                    uploaded_path = uploader.upload_file(value)
                    assets_copy[key] = uploaded_path

        kwargs["assets"] = assets_copy
        print(kwargs)
        result = self.create(*args, **kwargs)
        return result


class HasAsyncCreateAndBaseClient(Protocol[P, R_co]):
    _base_client: AsyncBaseClient  # Note: FilesClient doesn't have async upload yet

    async def create(self, *args: P.args, **kwargs: P.kwargs) -> R_co: ...


class AsyncGenerateMixin:
    async def generate(
        self: HasAsyncCreateAndBaseClient[P, R_co],
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> R_co:
        print("async generate")
        print(args)
        print(kwargs)

        assets = kwargs.get("assets")
        if assets is None:
            # If no assets, just call create directly
            return await self.create(*args, **kwargs)

        # 1️⃣ Upload any files with keys ending in '_file_path'
        uploader = AsyncFilesClient(base_client=self._base_client)

        # Make a copy to avoid mutating the original
        # Cast to help type checker understand this is a dictionary
        assets_dict = cast(Dict[str, Any], assets)
        assets_copy: Dict[str, Any] = dict(assets_dict)

        # Find and upload all file path keys
        for key, value in assets_dict.items():
            if key.endswith("_file_path") and isinstance(value, str):
                # Check if this looks like a local file path (not already uploaded)
                if not value.startswith(("http://", "https://", "api-assets/")):
                    uploaded_path = uploader.upload_file(value)
                    assets_copy[key] = uploaded_path

        kwargs["assets"] = assets_copy

        result = await self.create(*args, **kwargs)
        return result
