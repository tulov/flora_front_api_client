import marshmallow_dataclass
from flora_front_api_client.presentations.callbacks import (
    Callback,
    CallbackResponse,
    CallbackCreateRequest,
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


CallbackSchema = marshmallow_dataclass.class_schema(Callback)
CallbackResponseSchema = marshmallow_dataclass.class_schema(CallbackResponse)
CallbackCreateRequestSchema = marshmallow_dataclass.class_schema(CallbackCreateRequest)
