# from __future__ import annotations

from dataclasses import dataclass, field

from marshmallow.validate import Length

from .base import SuccessResponse, BaseDataclass


@dataclass
class Page(BaseDataclass):
    id: int = field(metadata={"strict": True})
    title_ru: str = field(metadata={"validate": Length(max=100)})
    title_en: str = field(metadata={"validate": Length(max=100)})
    slug: str = field(metadata={"validate": Length(max=100)})
    content_ru: str = field()
    content_en: str = field()
    published: bool = field()


@dataclass
class PageResponse(SuccessResponse):
    result: Page = field()
