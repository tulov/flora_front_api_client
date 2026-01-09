import marshmallow_dataclass
from marshmallow import Schema, EXCLUDE

from flora_front_api_client.presentations.countries import SearchCountryResponse, CountryResponse

Schema.Meta.unknown = EXCLUDE

CountriesResponseSchema = marshmallow_dataclass.class_schema(
    CountryResponse
)

SearchCountriesResponseSchema = marshmallow_dataclass.class_schema(
    SearchCountryResponse
)
