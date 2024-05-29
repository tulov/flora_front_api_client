import marshmallow_dataclass
from flora_front_api_client.presentations.full_text_search import (
    Product,
    ProductFullTextSearchResponse,
    ProductFullTextSearchRequest,
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


ProductResponseSchema = marshmallow_dataclass.class_schema(Product)
ProductFullTextSearchResponseSchema = marshmallow_dataclass.class_schema(
    ProductFullTextSearchResponse
)
ProductFullTextSearchRequestSchema = marshmallow_dataclass.class_schema(
    ProductFullTextSearchRequest
)
