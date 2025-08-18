from typing import Protocol, TypeVar
from typing_extensions import ParamSpec

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
        uploaded_path = self._upload_file(original_path)  # implement this

        # 2️⃣ Replace the path in assets
        assets = dict(assets)  # make a copy to avoid mutating original
        assets["image_file_path"] = uploaded_path

        # 3️⃣ Optional: set default name
        if name is None:
            name = "default_name"

        assets = kwargs.get("assets")
        print(assets)
        if assets is not None and hasattr(assets, "get"):
            print(assets.get("image_file_path"))

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
