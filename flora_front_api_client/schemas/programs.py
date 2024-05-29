import marshmallow_dataclass
from flora_front_api_client.presentations.programs import (
    ProgramResponse, ProgramsResponse, Program
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


ProgramResponseSchema = marshmallow_dataclass.class_schema(
    ProgramResponse
)
ProgramsResponseSchema = marshmallow_dataclass.class_schema(
    ProgramsResponse
)
ProgramRequestSchema = marshmallow_dataclass.class_schema(
    Program
)
