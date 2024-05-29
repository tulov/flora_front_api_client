import marshmallow_dataclass
from flora_front_api_client.presentations.orders import (
    CreateOrderRequest,
    OrderResponse,
    OrdersResponse,
    OrderCommentResponse,
    OrderBillResponse,
    OrderBillRequest,
    AfterRejectRequestBody,
    Order,
    OrderCommentRequest,
    OrderAnswerResponse,
    AnswersResponse,
    AnswerResponse,
    Answer,
    CancelOrderCalculationResponse,
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE

CreateOrderRequestSchema = marshmallow_dataclass.class_schema(CreateOrderRequest)
OrderResponseSchema = marshmallow_dataclass.class_schema(OrderResponse)
OrdersResponseSchema = marshmallow_dataclass.class_schema(OrdersResponse)
OrderCommentRequestSchema = marshmallow_dataclass.class_schema(OrderCommentRequest)
OrderCommentResponseSchema = marshmallow_dataclass.class_schema(OrderCommentResponse)
OrderBillResponseSchema = marshmallow_dataclass.class_schema(OrderBillResponse)
OrderBillRequestSchema = marshmallow_dataclass.class_schema(OrderBillRequest)
AfterRejectRequestBodySchema = marshmallow_dataclass.class_schema(
    AfterRejectRequestBody
)
OrderSchema = marshmallow_dataclass.class_schema(Order)
OrderAnswerResponseSchema = marshmallow_dataclass.class_schema(OrderAnswerResponse)
AnswersResponseSchema = marshmallow_dataclass.class_schema(AnswersResponse)
AnswerResponseSchema = marshmallow_dataclass.class_schema(AnswerResponse)
AnswerSchema = marshmallow_dataclass.class_schema(Answer)
CancelOrderCalculationResponseSchema = marshmallow_dataclass.class_schema(
    CancelOrderCalculationResponse
)
