import marshmallow_dataclass
from flora_front_api_client.presentations.inflects import (
    InflectResponse,
    InflectRequest,
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


InflectResponseSchema = marshmallow_dataclass.class_schema(InflectResponse)
InflectRequestSchema = marshmallow_dataclass.class_schema(InflectRequest)
