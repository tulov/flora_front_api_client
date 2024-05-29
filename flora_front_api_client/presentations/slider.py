from dataclasses import dataclass, field

from marshmallow.validate import Length

from .base import SuccessResponse, BaseDataclass, PagedResponse
from .images import Image


@dataclass
class SliderItemBase(BaseDataclass):
    id: int = field(metadata={"strict": True})
    description: str = field(metadata={"validate": Length(max=150)})
    desc_image_id: int | None = field(metadata={"strict": True})
    mobile_image_id: int | None = field(metadata={"strict": True})
    position: int = field(metadata={"strict": True})
    link: str = field(metadata={"validate": Length(max=250)})
    open_in_new_window: bool = field()
    enabled: bool = field()


@dataclass
class SliderItem(SliderItemBase):
    desc_image: Image | None = field()
    mobile_image: Image | None = field()


@dataclass
class Slider(BaseDataclass):
    items: list[SliderItem] = field(default_factory=list, metadata={"required": True})


@dataclass
class SliderResponse(PagedResponse):
    result: list[SliderItem] = field(default_factory=list, metadata={"required": True})


@dataclass
class SliderItemRequest(SliderItemBase):
    pass


@dataclass
class SliderItemResponse(SuccessResponse):
    result: SliderItem = field()
