import marshmallow_dataclass
from flora_front_api_client.presentations.chats import ChatResponse
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


ChatResponseSchema = marshmallow_dataclass.class_schema(ChatResponse)
