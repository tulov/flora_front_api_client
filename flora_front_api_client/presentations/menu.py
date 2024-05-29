from dataclasses import dataclass, field
from typing import Any

from marshmallow.validate import Length

from .base import SuccessResponse, BaseDataclass
from .images import Image


@dataclass
class MenuItemBase(BaseDataclass):
    id: int = field(metadata={"strict": True})
    name: str = field(metadata={"validate": Length(max=100, min=1)})
    parent_id: int | None = field(metadata={"strict": True})
    image_id: int | None = field(metadata={"strict": True})
    position: int = field(metadata={"strict": True})
    link: str = field(metadata={"validate": Length(max=250)})
    open_in_new_window: bool = field()
    enabled: bool = field()


@dataclass
class MenuItem(MenuItemBase):
    image: Image | None = field(default=None)
    children: list[Any] | None = field(default_factory=list)


@dataclass
class Menu(BaseDataclass):
    items: list[MenuItem] = field(default_factory=list, metadata={"required": True})


@dataclass
class MenuResponse(SuccessResponse):
    result: list[MenuItem] = field(default_factory=list, metadata={"required": True})


@dataclass
class MenuRequest(Menu):
    pass


@dataclass
class MenuQuerystring(BaseDataclass):
    only_enabled: bool | None = field()
