import marshmallow_dataclass
from flora_front_api_client.presentations.images import (
    ImageResponse, ImageUploadRequest, Image
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


ImageResponseSchema = marshmallow_dataclass.class_schema(
    ImageResponse
)
ImageUploadRequestSchema = marshmallow_dataclass.class_schema(
    ImageUploadRequest
)
ImageSchema = marshmallow_dataclass.class_schema(
    Image
)
