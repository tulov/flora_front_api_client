from dataclasses import dataclass, field

from marshmallow.validate import OneOf

from .base import SuccessResponse, BaseDataclass
from .enums import Languages


@dataclass
class Inflect(BaseDataclass):
    id: int = field(
        metadata={
            "strict": True,
        }
    )
    original: str = field()
    inflect1: str = field()
    inflect2: str = field()
    inflect3: str = field()
    inflect4: str = field()
    inflect5: str = field()
    inflect6: str = field()
    toloc: str = field()
    fromloc: str = field()
    whereloc: str = field()
    lang: str = field(metadata={"validate": OneOf([p.value for p in Languages])})


@dataclass
class InflectResponse(SuccessResponse):
    result: Inflect = field()


@dataclass
class InflectRequest(BaseDataclass):
    original: str = field()
    lang: str = field(
        metadata={"validate": OneOf([p.value for p in Languages])}, default="ru"
    )
