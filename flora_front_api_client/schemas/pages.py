import marshmallow_dataclass
from flora_front_api_client.presentations.pages import PageResponse
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


PageResponseSchema = marshmallow_dataclass.class_schema(PageResponse)
