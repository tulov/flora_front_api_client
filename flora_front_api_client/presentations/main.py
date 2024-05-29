from dataclasses import dataclass, field
from .base import BaseDataclass


@dataclass
class ApplicationInfoResponse(BaseDataclass):
    version: str = field()
    name: str = field()
