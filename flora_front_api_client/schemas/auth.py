import marshmallow_dataclass
from flora_front_api_client.presentations.auth import (
    AuthRequest, AuthResponse, RenewTokenRequest, RenewTokenResponse,
    SendRestoreAccessLinkRequest, RestoreAccessRequest, EnterCodeRequest,
    AuthCodeRequest
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


AuthRequestSchema = marshmallow_dataclass.class_schema(AuthRequest)
AuthResponseSchema = marshmallow_dataclass.class_schema(AuthResponse)
RenewTokenRequestSchema = marshmallow_dataclass.class_schema(RenewTokenRequest)
RenewTokenResponseSchema = marshmallow_dataclass.class_schema(
    RenewTokenResponse
)
SendRestoreAccessLinkRequestSchema = marshmallow_dataclass.class_schema(
    SendRestoreAccessLinkRequest
)
RestoreAccessRequestSchema = marshmallow_dataclass.class_schema(
    RestoreAccessRequest
)
EnterCodeRequestSchema = marshmallow_dataclass.class_schema(
    EnterCodeRequest
)
AuthCodeRequestSchema = marshmallow_dataclass.class_schema(
    AuthCodeRequest
)
