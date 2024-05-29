import marshmallow_dataclass
from flora_front_api_client.presentations.cities import (
    CityResponse, CitiesResponse, SearchCitiesResponse
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


CityResponseSchema = marshmallow_dataclass.class_schema(
    CityResponse
)
CitiesResponseSchema = marshmallow_dataclass.class_schema(
    CitiesResponse
)
SearchCitiesResponseSchema = marshmallow_dataclass.class_schema(
    SearchCitiesResponse
)
