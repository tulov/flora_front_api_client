import marshmallow_dataclass
from flora_front_api_client.presentations.main_page import MainPageResponse, MainPage
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


MainPageSchema = marshmallow_dataclass.class_schema(MainPage)
MainPageResponseSchema = marshmallow_dataclass.class_schema(MainPageResponse)
