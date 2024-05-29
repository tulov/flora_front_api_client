from dataclasses import dataclass, field

from marshmallow.validate import Length, OneOf
from .users import User
from .base import BaseDataclass
from .enums import CommunicationTransports


@dataclass
class AuthRequest(BaseDataclass):
    auth_key: str = field(metadata={"validate": Length(min=3, max=150)})
    password: str = field(metadata={"validate": Length(min=6, max=30)})


@dataclass
class AuthResponse(BaseDataclass):
    token: str = field()
    long_token: str = field()
    user: User = field()


@dataclass
class RenewTokenRequest(BaseDataclass):
    token: str = field()


@dataclass
class RenewTokenResponse(BaseDataclass):
    token: str = field()
    long_token: str = field()


@dataclass
class SendRestoreAccessLinkRequest(BaseDataclass):
    auth_key: str = field(metadata={"validate": Length(min=3, max=150)})


@dataclass
class RestoreAccessRequest(BaseDataclass):
    token: str = field()
    password: str = field(metadata={"validate": Length(min=6, max=30)})


@dataclass
class EnterCodeRequest(BaseDataclass):
    auth_key: str = field(metadata={"validate": Length(min=3, max=150)})
    transport: str = field(
        metadata={"validate": OneOf([r.value for r in CommunicationTransports])}
    )


@dataclass
class AuthCodeRequest(BaseDataclass):
    auth_key: str = field(metadata={"validate": Length(min=3, max=150)})
    code: str = field(metadata={"validate": Length(equal=4)})
