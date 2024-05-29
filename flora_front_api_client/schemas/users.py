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
from ..presentations.partners import (
    BindCityRequestDataclass,
    PartnerSettingsRequest,
    PartnerSettingsResponse,
)
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

BindCityRequestSchema = marshmallow_dataclass.class_schema(BindCityRequestDataclass)
PartnerSettingsRequestSchema = marshmallow_dataclass.class_schema(
    PartnerSettingsRequest
)
PartnerSettingsResponseSchema = marshmallow_dataclass.class_schema(
    PartnerSettingsResponse
)
PartnerWorkScheduleSchema = marshmallow_dataclass.class_schema(WorkSchedule)
UserPublicDataResponseSchema = marshmallow_dataclass.class_schema(
    UserPublicDataResponse
)
