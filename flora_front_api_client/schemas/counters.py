import marshmallow_dataclass
from flora_front_api_client.presentations.counters import CountersResponse
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE

CountersResponseSchema = marshmallow_dataclass.class_schema(
    CountersResponse
)
