import marshmallow_dataclass
from flora_front_api_client.presentations.fields import (
    FieldResponse, CreateFieldRequest, FieldsResponse, Relationship, Field
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


FieldResponseSchema = marshmallow_dataclass.class_schema(
    FieldResponse
)
FieldsResponseSchema = marshmallow_dataclass.class_schema(
    FieldsResponse
)
CreateFieldRequestSchema = marshmallow_dataclass.class_schema(
    CreateFieldRequest
)
RelationshipSchema = marshmallow_dataclass.class_schema(
    Relationship
)
FieldSchema = marshmallow_dataclass.class_schema(
    Field
)
