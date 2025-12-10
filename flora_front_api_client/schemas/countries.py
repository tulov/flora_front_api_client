import marshmallow_dataclass
from marshmallow import Schema, EXCLUDE

from flora_front_api_client.presentations.countries import SearchCountryResponse

Schema.Meta.unknown = EXCLUDE

SearchCountriesResponseSchema = marshmallow_dataclass.class_schema(
    SearchCountryResponse
)
