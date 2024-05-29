import marshmallow_dataclass
from flora_front_api_client.presentations.todo import TodosResponse, Todo
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


TodoSchema = marshmallow_dataclass.class_schema(Todo)
TodosResponseSchema = marshmallow_dataclass.class_schema(TodosResponse)
