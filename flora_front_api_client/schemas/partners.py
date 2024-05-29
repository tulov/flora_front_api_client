import marshmallow_dataclass
from flora_front_api_client.presentations.partners import (
    Partner,
    SetCitiesAvailableRequest,
    SetProductsAvailableRequest,
    PartnerSettingsRequest,
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


PartnerSchema = marshmallow_dataclass.class_schema(Partner)
SetCitiesAvailableRequestSchema = marshmallow_dataclass.class_schema(
    SetCitiesAvailableRequest
)
SetProductsAvailableRequestSchema = marshmallow_dataclass.class_schema(
    SetProductsAvailableRequest
)
PartnerSettingsRequestSchema = marshmallow_dataclass.class_schema(
    PartnerSettingsRequest
)
