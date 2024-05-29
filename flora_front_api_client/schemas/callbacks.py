import marshmallow_dataclass
from flora_front_api_client.presentations.callbacks import (
    Callback,
    CallbackResponse,
    CallbacksResponse,
    CallbackUpdateRequest,
    CallbackCreateRequest,
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


CallbackSchema = marshmallow_dataclass.class_schema(Callback)
CallbackResponseSchema = marshmallow_dataclass.class_schema(CallbackResponse)
CallbacksResponseSchema = marshmallow_dataclass.class_schema(CallbacksResponse)
CallbackUpdateRequestSchema = marshmallow_dataclass.class_schema(CallbackUpdateRequest)
CallbackCreateRequestSchema = marshmallow_dataclass.class_schema(CallbackCreateRequest)
