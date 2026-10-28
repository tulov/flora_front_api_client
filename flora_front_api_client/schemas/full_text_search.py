import marshmallow_dataclass
from flora_front_api_client.presentations.full_text_search import (
    ProductFullTextSearchResponse,
    ProductFullTextSearchRequest,
    SiteFullTextSearchResponse,
    SiteFullTextSearchRequest,
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


ProductFullTextSearchResponseSchema = marshmallow_dataclass.class_schema(
    ProductFullTextSearchResponse
)
ProductFullTextSearchRequestSchema = marshmallow_dataclass.class_schema(
    ProductFullTextSearchRequest
)
SiteFullTextSearchResponseSchema = marshmallow_dataclass.class_schema(
    SiteFullTextSearchResponse
)
SiteFullTextSearchRequestSchema = marshmallow_dataclass.class_schema(
    SiteFullTextSearchRequest
)
