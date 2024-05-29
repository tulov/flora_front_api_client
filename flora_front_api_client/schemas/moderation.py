import marshmallow_dataclass
from flora_front_api_client.presentations.moderation import (
    RequestsForModerationResponse, RequestForModerationResponse,
    ModerationUpdateRequest, RequestForModeration
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


RequestsForModerationResponseSchema = marshmallow_dataclass.class_schema(
    RequestsForModerationResponse
)

RequestForModerationResponseSchema = marshmallow_dataclass.class_schema(
    RequestForModerationResponse
)

ModerationUpdateRequestSchema = marshmallow_dataclass.class_schema(
    ModerationUpdateRequest
)
RequestForModerationSchema = marshmallow_dataclass.class_schema(
    RequestForModeration
)
