import marshmallow_dataclass
from flora_front_api_client.presentations.main import ApplicationInfoResponse
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE

ApplicationInfoResponseSchema = marshmallow_dataclass.class_schema(
    ApplicationInfoResponse
)
