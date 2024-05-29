from dataclasses import dataclass, field
from .base import SuccessResponse, BaseDataclass


@dataclass
class CountersResult(BaseDataclass):
    moderate: int = field(default=0)
    answers: int = field(default=0)


@dataclass
class CountersResponse(SuccessResponse):
    result: CountersResult = field()
