from dataclasses import dataclass, field

from marshmallow.validate import Length

from .base import BaseDataclass, SuccessResponse
from .images import Image


@dataclass
class UrlQuerystring(BaseDataclass):
    url: str = field(metadata={"required": True})


@dataclass
class SEO(BaseDataclass):
    url: str = field(metadata={"validate": Length(max=500)})
    title: str = field()
    description: str = field()
    h1: str = field()
    text: str = field()
    image: Image | None = field(default=None, metadata={"load_default": None})


@dataclass
class SEOResponse(SuccessResponse):
    result: SEO = field(metadata={"required": True})
