import marshmallow_dataclass
from flora_front_api_client.presentations.users import (
    DataForAuth,
    User,
    RegistrationUserData,
    ConfirmDataForAuthRequest,
    UsersResponse,
    ChangePasswordRequest,
    WorkSchedule,
    UserPublicDataResponse,
)
from ..presentations.base import SuccessResponse
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


DataForAuthSchema = marshmallow_dataclass.class_schema(DataForAuth)
UserSchema = marshmallow_dataclass.class_schema(User)
RegistrationUserSchema = marshmallow_dataclass.class_schema(RegistrationUserData)
ConfirmDataForAuthRequestSchema = marshmallow_dataclass.class_schema(
    ConfirmDataForAuthRequest
)
ConfirmDataForAuthResponseSchema = marshmallow_dataclass.class_schema(SuccessResponse)
UsersResponseSchema = marshmallow_dataclass.class_schema(UsersResponse)
ChangePasswordRequestSchema = marshmallow_dataclass.class_schema(ChangePasswordRequest)

PartnerWorkScheduleSchema = marshmallow_dataclass.class_schema(WorkSchedule)
UserPublicDataResponseSchema = marshmallow_dataclass.class_schema(
    UserPublicDataResponse
)
