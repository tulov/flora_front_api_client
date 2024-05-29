"""
Модуль содержит схемы для валидации данных в запросах и ответах.
Схемы валидации запросов используются в бою для валидации данных отправленных
клиентами.
Схемы валидации ответов *ResponseSchema используются только при тестировании,
чтобы убедиться что обработчики возвращают данные в корректном формате.
"""
import marshmallow_dataclass
from flora_front_api_client.presentations.error import Error, ErrorResponse
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


ErrorSchema = marshmallow_dataclass.class_schema(Error)
ErrorResponseSchema = marshmallow_dataclass.class_schema(ErrorResponse)
