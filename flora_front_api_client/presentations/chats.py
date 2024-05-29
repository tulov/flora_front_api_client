from dataclasses import dataclass, field

from .base import BaseDataclass, SuccessResponse


@dataclass
class Chat(BaseDataclass):
    url: str = field()


@dataclass
class ChatResponse(SuccessResponse):
    result: Chat = field()
