from dataclasses import dataclass, field

from marshmallow.validate import Length, OneOf

from .base import SuccessResponse, BaseDataclass, PagedResponse
from .enums import FieldType, HTMLWidget


@dataclass
class FieldBaseDataclass(BaseDataclass):
    name: str = field(metadata={"validate": Length(max=150, min=1)})
    help: str | None = field(metadata={"validate": Length(max=200)})
    type: str = field(
        metadata={
            "validate": OneOf([r.value for r in FieldType]),
        }
    )


@dataclass
class Field(FieldBaseDataclass):
    id: int = field(
        metadata={
            "strict": True,
        }
    )
    widget: str | None = field(
        metadata={
            "validate": OneOf([r.value for r in HTMLWidget]),
        },
        default=None,
    )
    is_required: bool | None = field(default=False)
    is_inherited: bool = field(default=False)


@dataclass
class CreateFieldRequest(FieldBaseDataclass):
    pass


@dataclass
class FieldResponse(SuccessResponse):
    result: Field = field()


@dataclass
class FieldsResponse(PagedResponse):
    result: list[Field] = field(default_factory=list, metadata={"required": True})


@dataclass
class Relationship(BaseDataclass):
    id: int = field(
        metadata={
            "strict": True,
        }
    )
    widget: str = field(
        metadata={
            "validate": OneOf([r.value for r in HTMLWidget]),
        }
    )
    is_required: bool = field()
