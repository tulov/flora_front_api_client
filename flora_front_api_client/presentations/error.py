from dataclasses import dataclass, field
from typing import Any

from .base import BaseDataclass


@dataclass
class Error(BaseDataclass):
    code: str = field()
    message: str = field()
    error_code: int | None = field()
    fields: dict[str, Any] = field(default_factory=dict)


@dataclass
class ErrorResponse(BaseDataclass):
    error: Error = field()
