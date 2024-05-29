import marshmallow_dataclass
from flora_front_api_client.presentations.slider import (
    SliderItemRequest, SliderResponse, SliderItemResponse, Slider
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


SliderResponseSchema = marshmallow_dataclass.class_schema(
    SliderResponse
)

SliderItemRequestSchema = marshmallow_dataclass.class_schema(
    SliderItemRequest
)

SliderItemResponseSchema = marshmallow_dataclass.class_schema(
    SliderItemResponse
)

SliderSchema = marshmallow_dataclass.class_schema(
    Slider
)
