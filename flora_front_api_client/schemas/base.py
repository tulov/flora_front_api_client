import marshmallow_dataclass

from flora_front_api_client.presentations.base import (
    SuccessResponse, Querystring, WithFieldsQuerystring, ResultResponse,
    DataRequest, RevisionRequest
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE

SuccessResponseSchema = marshmallow_dataclass.class_schema(
    SuccessResponse
)

QuerystringSchema = marshmallow_dataclass.class_schema(
    Querystring
)

WithFieldsQuerystringSchema = marshmallow_dataclass.class_schema(
    WithFieldsQuerystring
)
ResultResponseSchema = marshmallow_dataclass.class_schema(
    ResultResponse
)
DataRequestSchema = marshmallow_dataclass.class_schema(
    DataRequest
)
RevisionRequestSchema = marshmallow_dataclass.class_schema(
    RevisionRequest
)
