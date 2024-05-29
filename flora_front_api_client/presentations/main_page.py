from dataclasses import dataclass, field

from marshmallow.validate import Length

from .base import SuccessResponse, BaseDataclass


@dataclass
class MainPageBlock(BaseDataclass):
    slug: str = field(metadata={"validate": Length(max=25, min=1)})
    title: str | None = field(metadata={"validate": Length(max=100)})
    description: str | None = field(metadata={"validate": Length(max=1000)})
    category_id: int | None = field(metadata={"strict": True})
    filters: str | None = field(metadata={"validate": Length(max=1000)})
    sorts: str | None = field(metadata={"validate": Length(max=1000)})
    is_system: bool = field()
    enabled: bool = field()
    index: int = field(metadata={"strict": True})


@dataclass
class MainPage(BaseDataclass):
    blocks: list[MainPageBlock] = field(
        default_factory=list, metadata={"required": True}
    )


@dataclass
class MainPageResponse(SuccessResponse):
    result: MainPage = field()
