import marshmallow_dataclass
from flora_front_api_client.presentations.prices import (
    PriceResponse,
    PricesResponse,
    PricesRequest,
    PricesCurrentResponse,
    PricesCurrentQuerystring,
    PriceBase,
    PriceData,
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


PriceResponseSchema = marshmallow_dataclass.class_schema(PriceResponse)
PricesResponseSchema = marshmallow_dataclass.class_schema(PricesResponse)
PricesRequestSchema = marshmallow_dataclass.class_schema(PricesRequest)
PricesCurrentResponseSchema = marshmallow_dataclass.class_schema(PricesCurrentResponse)
PricesCurrentQuerystringSchema = marshmallow_dataclass.class_schema(
    PricesCurrentQuerystring
)
PriceBaseSchema = marshmallow_dataclass.class_schema(PriceBase)
PriceDataSchema = marshmallow_dataclass.class_schema(PriceData)
