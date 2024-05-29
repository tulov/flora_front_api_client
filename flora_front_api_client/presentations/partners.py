from decimal import Decimal
from dataclasses import dataclass, field

from marshmallow.validate import Range, Length, OneOf

from .base import BaseDataclass, SuccessResponse
from .images import Image
from .prices import Price
from .users import User, WorkSchedule
from .enums import UnitOfTime


@dataclass
class PartnerBindCityData(BaseDataclass):
    city_id: int = field(metadata={"strict": True})
    delivery_price: Decimal = field(metadata={"validate": Range(min=0)})
    delivery_time: int = field(metadata={"strict": True})
    delivery_time_unit: str = field(
        metadata={
            "validate": OneOf([a.value for a in UnitOfTime]),
        }
    )


@dataclass
class Partner(User):
    cities: list[PartnerBindCityData] | None = field(default_factory=list)
    prices: list[Price] | None = field(default_factory=list)


@dataclass
class BindCityRequestDataclass(PartnerBindCityData):
    pass


@dataclass
class PartnerSettings(BaseDataclass):
    address: str | None = field(metadata={"validate": Length(max=200)})
    work_schedule: WorkSchedule = field(default_factory=WorkSchedule)
    not_working_time_delivery: bool = field(default=False)
    avatar_img_id: int | None = field(default=None)
    avatar: Image | None = field(default=None)


@dataclass
class PartnerSettingsRequest(BaseDataclass):
    settings: PartnerSettings = field()
    avatar: str | None = field()
    revision: int = field(metadata={"strict": True})


@dataclass
class PartnerSettingsR(BaseDataclass):
    on_moderation: PartnerSettings | None = field()
    on_site: PartnerSettings = field()
    revision: int = field(metadata={"strict": True})


@dataclass
class PartnerSettingsResponse(SuccessResponse):
    result: PartnerSettingsR = field()


@dataclass
class SetProductsAvailableRequest(BaseDataclass):
    products_ids: list[int] = field()
    available: bool = field()


@dataclass
class SetCitiesAvailableRequest(BaseDataclass):
    cities_ids: list[int] = field()
    available: bool = field()
