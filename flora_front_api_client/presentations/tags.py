from dataclasses import dataclass, field

from marshmallow.validate import Length

from .base import SuccessResponse, BaseDataclass, PagedResponse


@dataclass
class TagBase(BaseDataclass):
    id: int = field(
        metadata={
            "strict": True,
        }
    )
    name: str = field(metadata={"validate": Length(max=150, min=1)})


@dataclass
class Tag(TagBase):
    parent_id: int | None = field(
        metadata={
            "strict": True,
        },
        default=None,
    )
    is_visible: bool = field(default=True)
    is_inherited: bool = field(default=False)


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
class TagsTreeResponse(SuccessResponse):
    result: list[TagsTreeItem] = field(
        default_factory=list, metadata={"required": True}
    )
