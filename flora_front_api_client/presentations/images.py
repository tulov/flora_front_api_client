from dataclasses import dataclass, field
from typing import Any

from marshmallow.validate import OneOf

from .base import BaseDataclass, SuccessResponse
from .enums import ImageTarget
import cloudinary


@dataclass
class Image(BaseDataclass):
    id: str = field()
    provider: str = field()

    def build_url(self, *, width: int, height: int):
        return f"/display?path={self.path}&w={width}&h={height}&op=resize"

    def full_url(self, *, width: int, height: int) -> str:
        r = self.url.split("/", 3)
        url = self.build_url(width=width, height=height)
        if len(r) < 3:
            return url
        return "/".join(r[:3]) + url

    @property
    def mime_type(self) -> str:
        if not self.path:
            return ""
        if self.path.endswith(".png"):
            return "image/png"
        if self.path.endswith(".jpeg"):
            return "image/jpeg"
        raise RuntimeError("Not supported file type")

    @property
    def extension(self) -> str:
        if not self.mime_type:
            return ""
        m = self.mime_type
        return m.split("/")[1]

    def get_file_uploader_dict(
        self,
        file_width: int,
        file_height: int,
        url_width: int,
        url_height: int,
        thumb_width: int,
        thumb_height: int,
    ):
        w = self.data.get("width", file_width)
        h = self.data.get("height", file_height)
        return {
            "name": f"{self.id}.{self.extension}",
            "type": f"image/{self.extension}",
            "size": 0,
            "file": self.full_url(width=w, height=h),
            "local": "",
            "data": {
                "url": self.full_url(width=url_width, height=url_height),
                "thumbnail": self.full_url(width=thumb_width, height=thumb_height),
                "readerForce": True,
                "listProps": {"id": self.id},
            },
        }


@dataclass
class ImageResponse(SuccessResponse):
    result: Image = field()


@dataclass
class ImageUploadRequest(BaseDataclass):
    position: int = field(
        metadata={
            "strict": True,
        }
    )
    file: str = field()
    obj_id: int | None = field(default=None)
    obj_type: str | None = field(
        metadata={
            "validate": OneOf([r.value for r in ImageTarget]),
        },
        default=None,
    )
    data: dict[str, Any] = field(default_factory=dict)
