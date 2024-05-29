import marshmallow_dataclass
from flora_front_api_client.presentations.promo import (
    PromoCode, PromoCodeResponse, PromoCodesResponse
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


PromoCodeResponseSchema = marshmallow_dataclass.class_schema(
    PromoCodeResponse
)
PromoCodesResponseSchema = marshmallow_dataclass.class_schema(
    PromoCodesResponse
)
PromoCodeSchema = marshmallow_dataclass.class_schema(
    PromoCode
)
