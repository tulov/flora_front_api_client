import marshmallow_dataclass
from flora_front_api_client.presentations.tags import (
    TagResponse, CreateTagRequest, TagsResponse, TagsTreeResponse, Tag
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


TagResponseSchema = marshmallow_dataclass.class_schema(
    TagResponse
)
TagsResponseSchema = marshmallow_dataclass.class_schema(
    TagsResponse
)
CreateTagRequestSchema = marshmallow_dataclass.class_schema(
    CreateTagRequest
)
TagsTreeResponseSchema = marshmallow_dataclass.class_schema(
    TagsTreeResponse
)
TagSchema = marshmallow_dataclass.class_schema(
    Tag
)
