from dataclasses import dataclass, field
from typing import Any

from marshmallow.validate import Length

from .base import SuccessResponse, BaseDataclass, PagedResponse


@dataclass
class TagBase(BaseDataclass):
    id: int = field(
        metadata={
            "strict": True,
        }
    )
    name_ru: str = field(metadata={"validate": Length(max=150, min=1)})


@dataclass
class Tag(TagBase):
    parent_id: int | None = field(
        metadata={
            "strict": True,
        }
    )
    slug: str = field(metadata={"validate": Length(max=100, min=1)})
    name_en: str = field(metadata={"validate": Length(max=50, min=1)}, default=None)
    is_visible: bool = field(default=True)
    is_tag: bool = field(default=True)
    additional: dict[str, Any] = field(default_factory=dict)






@dataclass
class CreateTagRequest(BaseDataclass):
    name: str = field(metadata={"validate": Length(max=150, min=1)})
    parent_id: int | None = field(
        metadata={
            "strict": True,
        }
    )
    is_visible: bool | None = field()


@dataclass
class TagResponse(SuccessResponse):
    result: Tag = field()


@dataclass
class TagsResponse(PagedResponse):
    result: list[Tag] = field(default_factory=list, metadata={"required": True})


@dataclass
class TagsTreeItem(TagBase):
    children: list[TagBase] | None = field()

@dataclass
class TagsWithParents(TagsTreeItem):
    parent_id: int = field(metadata={"strict": True})
    name: str = field(metadata={"validate": Length(max=150, min=1)})


@dataclass
class TagsTreeResponse(SuccessResponse):
    result: list[TagsTreeItem] = field(
        default_factory=list, metadata={"required": True}
    )
