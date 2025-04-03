import marshmallow_dataclass
from flora_front_api_client.presentations.seo import UrlQuerystring, SEOResponse
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


SEOResponseSchema = marshmallow_dataclass.class_schema(SEOResponse)
UrlQuerystringSchema = marshmallow_dataclass.class_schema(UrlQuerystring)
