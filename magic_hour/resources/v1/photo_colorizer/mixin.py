from typing import Protocol, TypeVar
from typing_extensions import ParamSpec

from magic_hour.resources.v1.files.client import FilesClient

P = ParamSpec("P")
R_co = TypeVar("R_co", covariant=True)


class HasCreate(Protocol[P, R_co]):
    def create(self, *args: P.args, **kwargs: P.kwargs) -> R_co: ...


class GenerateMixin:
    def generate(self: HasCreate[P, R_co], *args: P.args, **kwargs: P.kwargs) -> R_co:
        print("generate")
        print(args)
        print(kwargs)

        assets = kwargs.get("assets")
        # 1️⃣ Upload the file and get new path
        original_path = assets["image_file_path"]

        uploader = FilesClient(base_client=self._base_client)

        uploaded_path = uploader.upload_file(original_path)

        # 2️⃣ Replace the path in assets
        assets = dict(assets)  # make a copy to avoid mutating original
        assets["image_file_path"] = uploaded_path

        print(assets)
        if assets is not None and hasattr(assets, "get"):
            print(assets.get("image_file_path"))

        kwargs["assets"] = assets

        print(kwargs)

        result = self.create(*args, **kwargs)
        print("result")
        return result


class HasAsyncCreate(Protocol[P, R_co]):
    async def create(self, *args: P.args, **kwargs: P.kwargs) -> R_co: ...


class AsyncGenerateMixin:
    async def generate(
        self: HasAsyncCreate[P, R_co], *args: P.args, **kwargs: P.kwargs
    ) -> R_co:
        # pre-hook (optional)
        result = await self.create(*args, **kwargs)
        # post-hook (optional)
        return result
