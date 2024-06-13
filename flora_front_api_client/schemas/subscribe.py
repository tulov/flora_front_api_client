import marshmallow_dataclass
from flora_front_api_client.presentations.subscribe import (
    Subscribe,
    SubscribeResponse,
    SubscribeCreateRequest,
    SubscribeConfirmRequest,
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


SubscribeSchema = marshmallow_dataclass.class_schema(Subscribe)
SubscribeResponseSchema = marshmallow_dataclass.class_schema(SubscribeResponse)
SubscribeCreateRequestSchema = marshmallow_dataclass.class_schema(
    SubscribeCreateRequest
)
SubscribeConfirmRequestSchema = marshmallow_dataclass.class_schema(
    SubscribeConfirmRequest
)
