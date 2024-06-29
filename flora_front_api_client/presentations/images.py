from dataclasses import dataclass, field
from typing import Any

from marshmallow.validate import OneOf

from .base import BaseDataclass, SuccessResponse
from .enums import ImageTarget
import cloudinary


def _init_cloudinary():
    from ..client import FloraApiClient

    cloudinary.config(
        cloud_name=FloraApiClient.cloudinary_cloud_name,
    )


@dataclass
class Image(BaseDataclass):
    id: str = field()
    provider: str = field()

    def build_url(self, *, width: int, height: int):
        _init_cloudinary()
        options = {
            "width": width,
            "height": height,
        }
        return cloudinary.CloudinaryImage(self.id).build_url(**options)

    def full_url(self, *, width: int, height: int) -> str:
        return self.build_url(width=width, height=height)

    def adaptive_url(self) -> str:
        _init_cloudinary()
        options = {
            "width": "auto",
            "crop": "limit",
            "dpr": "auto",
        }
        return cloudinary.CloudinaryImage(self.id).build_url(**options)


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
