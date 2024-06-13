from dataclasses import dataclass, field
from datetime import datetime, date, timedelta
from typing import Any

from marshmallow import ValidationError
from marshmallow.fields import Decimal
from marshmallow.validate import ContainsOnly, Length, Range, Email, OneOf, Regexp

from .base import BaseDataclass, SuccessResponse, Pager
from .enums import Roles, PromoSystems, UnitOfTime, Genders
from .images import Image
from .validates import UniqueItems, Filled, Phone


@dataclass
class DataForAuth(BaseDataclass):
    id: int = field(
        metadata={
            "strict": True,
        }
    )
    service: str = field(metadata={"validate": Length(max=20, min=1)})
    is_checked: bool = field()
    value: str = field()
    data: dict[str, Any] = field(default_factory=dict)
    _confirm_data: str | None = field(default=None)
    _confirm_attempt_counter: int | None = field(default=None)
    _last_request_code: datetime | None = field(default=None)

    def get_confirm_data(self) -> str | None:
        return self._confirm_data

    def get_confirm_attempt_counter(self) -> int | None:
        return self._confirm_attempt_counter

    def get_last_request_code(self) -> datetime | None:
        return self._last_request_code


@dataclass
class Contacts(BaseDataclass):
    phone: str | None = field(metadata={"validate": Phone()})
    email: str | None = field(metadata={"validate": Email()})
    whatsapp: str | None = field(metadata={"validate": Phone()})


@dataclass
class WorkScheduleItem(BaseDataclass):
    start: str = field(
        metadata={"validate": Regexp("(^([0-1][0-9]|2[0-3]):[0-5][0-9]$)|^$")}
    )
    end: str = field(
        metadata={"validate": Regexp("(^([0-1][0-9]|2[0-3]):[0-5][0-9]$)|^$")}
    )

    def __post_init__(self):
        if not self.start and self.end:
            raise ValidationError({"_schema": ["Не указано начало диапазона"]})
        if self.start and not self.end:
            raise ValidationError({"_schema": ["Не указан конец диапазона"]})
        if self.start and self.end:
            start = datetime.strptime(self.start, "%H:%M").time()
            end = datetime.strptime(self.end, "%H:%M").time()
            if start >= end:
                raise ValidationError(
                    {"_schema": ["Начало диапазона должно быть меньше его завершения"]}
                )


@dataclass
class WorkScheduleException(BaseDataclass):
    start: date = field()
    end: date = field()
    action: str = field(metadata={"validate": OneOf(["work", "rest"])})
    time_start: str = field(
        metadata={"validate": Regexp("(^([0-1][0-9]|2[0-3]):[0-5][0-9]$)|^$")}
    )
    time_end: str = field(
        metadata={"validate": Regexp("(^([0-1][0-9]|2[0-3]):[0-5][0-9]$)|^$")}
    )

    def __post_init__(self):
        if self.start > self.end:
            raise ValidationError(
                {
                    "_schema": [
                        "Начало диапазона должно быть меньше или совпадать с его завершением"
                    ]
                }
            )
        if self.action == "work" and (self.time_start is None or self.time_end is None):
            raise ValidationError(
                {"_schema": ["Для рабочих дней нужно указать рабочий диапазон времени"]}
            )
        if self.action == "rest":
            self.time_start = ""
            self.time_end = ""
        if self.time_start:
            start = datetime.strptime(self.time_start, "%H:%M").time()
            end = datetime.strptime(self.time_end, "%H:%M").time()
            if start >= end:
                raise ValidationError(
                    {
                        "_schema": [
                            "Начало рабочего диапазона должно быть меньше его завершения"
                        ]
                    }
                )


@dataclass
class WorkSchedule(BaseDataclass):
    monday: WorkScheduleItem | None = field(default=None)
    tuesday: WorkScheduleItem | None = field(default=None)
    wednesday: WorkScheduleItem | None = field(default=None)
    thursday: WorkScheduleItem | None = field(default=None)
    friday: WorkScheduleItem | None = field(default=None)
    saturday: WorkScheduleItem | None = field(default=None)
    sunday: WorkScheduleItem | None = field(default=None)
    exceptions: list[WorkScheduleException] = field(default_factory=list)

    def __post_init__(self):
        if len(self.exceptions) > 3:
            raise ValidationError(
                {
                    "_schema": [
                        "Не может быть указано больше 3 исключений из рабочего расписания"
                    ]
                }
            )
        if len(self.exceptions) > 1:
            for start in range(len(self.exceptions) - 1):
                for end in range(start + 1, len(self.exceptions)):
                    one = self.exceptions[start]
                    two = self.exceptions[end]
                    if (
                        one.start <= two.start <= one.end
                        or one.start <= two.end <= one.end
                        or two.start <= one.start <= two.end
                        or two.start <= one.end <= two.end
                    ):
                        raise ValidationError(f"Пересекающиеся диапазоны {one} и {two}")

    def get_working_time(self, on_date: date | datetime) -> tuple[str, str] | None:
        if isinstance(on_date, datetime):
            on_date = on_date.date()
        exception = next(
            filter(lambda e: e.start <= on_date <= e.end, self.exceptions), None
        )
        # если на дату есть исключения, тогда используем их,
        if exception:
            if exception.action == "rest":
                return None
            if exception.time_start and exception.time_end:
                return exception.time_start, exception.time_end
            return None

        # иначе используем стандартное расписание
        day_of_week = on_date.strftime("%A").lower()
        schedule: WorkScheduleItem | None = getattr(self, day_of_week)
        if schedule and schedule.start and schedule.end:
            return schedule.start, schedule.end
        return None

    def _get_nearest_working_time(
        self, on_date: date | datetime
    ) -> tuple[datetime, datetime] | None:
        max_days = 14
        working_time = None
        cur_date = on_date
        i = 0
        while not working_time and i < max_days:
            cur_date = on_date + timedelta(days=i)
            i += 1
            working_time = self.get_working_time(cur_date)
        if working_time:
            start_time = datetime.strptime(working_time[0], "%H:%M").time()
            end_time = datetime.strptime(working_time[1], "%H:%M").time()
            return datetime.combine(cur_date, start_time), datetime.combine(
                cur_date, end_time
            )
        return None

    def min_datetime_of_ending(
        self,
        on_datetime: datetime,
        delta: int,
        time_unit: UnitOfTime | str,
        is_continuous: bool = False,
        continue_on_not_working_time: bool = False,
    ) -> datetime | None:
        """
        Возвращает минимальное возможное время с учетом периода
        :param on_datetime дата и время, с которой начинаем считать
        :param delta продолжительность действия
        :param time_unit единица измерения продолжительности действия
        :param is_continuous если период непрерывный, то истина (не может прерываться)
        :param continue_on_not_working_time если период может продолжаться в нерабочее время, то истина
        """
        nearest_working_time = self._get_nearest_working_time(on_datetime)
        if not nearest_working_time:
            return None
        if on_datetime >= nearest_working_time[1]:
            nearest_working_time = self._get_nearest_working_time(
                on_datetime + timedelta(days=1)
            )
        elif on_datetime >= nearest_working_time[0]:
            nearest_working_time = (on_datetime, nearest_working_time[1])
        if not nearest_working_time:
            return None
        if isinstance(time_unit, str):
            time_unit = UnitOfTime(time_unit)
        if time_unit == UnitOfTime.day:
            td = timedelta(days=delta)
        elif time_unit == UnitOfTime.hour:
            td = timedelta(hours=delta)
        elif time_unit == UnitOfTime.week:
            td = timedelta(weeks=delta)
        elif time_unit == UnitOfTime.minute:
            td = timedelta(minutes=delta)
        elif time_unit == UnitOfTime.month:
            td = timedelta(days=delta * 30)
        elif time_unit == UnitOfTime.year:
            td = timedelta(days=365 * delta)
        else:
            raise NotImplementedError

        end_datetime = nearest_working_time[0] + td
        if continue_on_not_working_time:
            return end_datetime
        if end_datetime <= nearest_working_time[1]:
            return end_datetime
        if is_continuous:
            i = 0
            while end_datetime > nearest_working_time[1] and i < 15:
                nearest_working_time = self._get_nearest_working_time(
                    nearest_working_time[0] + timedelta(days=1)
                )
                end_datetime = nearest_working_time[0] + td
                i += 1
            if end_datetime > nearest_working_time[1]:
                return None
            return end_datetime
        while end_datetime > nearest_working_time[1]:
            diff = end_datetime - nearest_working_time[1]
            nearest_working_time = self._get_nearest_working_time(
                nearest_working_time[0] + timedelta(days=1)
            )
            end_datetime = nearest_working_time[0] + diff
        return end_datetime


@dataclass
class UserData(BaseDataclass):
    address: str | None = field(metadata={"validate": Length(max=200)}, default=None)
    promo_system: str | None = field(
        metadata={"validate": OneOf([r.value for r in PromoSystems])},
        default=PromoSystems.cashback.value,
    )
    work_schedule: WorkSchedule | None = field(default=None)
    old_id: int | None = field(default=None)
    cashback: Decimal = field(default=Decimal(0))
    not_working_time_delivery: bool = field(default=False)
    avatar_img_id: int | None = field(default=None)
    gender: str | None = field(
        default=None, metadata={"validate": OneOf([r.value for r in Genders])}
    )
    birthday: str | None = field(default=None)


@dataclass
class User(BaseDataclass):
    id: int = field(
        metadata={
            "strict": True,
        }
    )
    registration_date: datetime = field()
    name: str = field(metadata={"validate": Length(max=150)})
    discount: int = field(metadata={"strict": True, "validate": Range(min=0, max=100)})
    send_sms: bool = field()
    send_email: bool = field()
    language: str = field(metadata={"validate": Length(equal=2)})
    currency: str = field(metadata={"validate": Length(equal=3)})
    is_moderated: bool = field()
    banned: bool = field()
    percent_us: int = field(
        metadata={
            "strict": True,
            "validate": Range(min=0, max=100),
        }
    )
    contacts: Contacts | None = field(default=None)
    data: UserData = field(default_factory=UserData)
    data_for_auth: list[DataForAuth] | None = field(default_factory=list)
    roles: list[str] = field(
        default_factory=list,
        metadata={
            "validate": [
                ContainsOnly([role.value for role in Roles]),
                UniqueItems(),
                Filled(),
            ],
            "required": True,
        },
    )
    avatar: Image | None = field(default=None)
    _salt: str | None = field(default=None)
    _password: str | None = field(default=None)

    def get_salt(self) -> str | None:
        return self._salt

    def get_password(self) -> str | None:
        return self._password

    @property
    def promo_system(self) -> str:
        if self.data and hasattr(self.data, "promo_system"):
            return self.data.promo_system
        return PromoSystems.cashback.value

    @property
    def cashback(self) -> Decimal:
        if self.data and hasattr(self.data, "cashback"):
            return self.data.cashback
        return Decimal(0)


@dataclass
class RegistrationUserData(BaseDataclass):
    password: str = field(metadata={"validate": Length(min=6, max=30)})
    phone: str | None = field(metadata={"validate": Phone()})
    email: str | None = field(metadata={"validate": Email()})
    name: str | None = field(metadata={"validate": Length(min=1, max=150)})
    language: str = field(metadata={"validate": Length(equal=2)})
    currency: str = field(metadata={"validate": Length(equal=3)})
    address: str = field(metadata={"validate": Length(max=200)})
    send_sms: bool = field(default=True)
    send_email: bool = field(default=True)

    def __post_init__(self):
        if not self.phone and not self.email:
            raise ValidationError(
                {
                    "_schema": [
                        "You need to fill in at least "
                        'one field from "email" or "phone"'
                    ]
                }
            )


@dataclass
class ConfirmDataForAuthRequest(BaseDataclass):
    code: str = field(metadata={"validate": Length(min=4, max=20)})


@dataclass
class UsersResponse(SuccessResponse):
    pager: Pager = field()
    result: list[User] = field(default_factory=list, metadata={"required": True})


@dataclass
class ChangePasswordRequest(BaseDataclass):
    old_password: str = field(metadata={"validate": Length(min=6, max=30)})
    new_password: str = field(metadata={"validate": Length(min=6, max=30)})

    def __post_init__(self):
        if self.old_password == self.new_password:
            raise ValidationError(
                {"_schema": ["New password should be different with old password"]}
            )


@dataclass
class UserPublicData(BaseDataclass):
    id: int = field()
    name: str = field()
    avatar: str | None = field(default=None)


@dataclass
class UserPublicDataResponse(SuccessResponse):
    result: list[UserPublicData] = field(default_factory=list)


@dataclass
class Employee(BaseDataclass):
    id: int = field(
        metadata={
            "strict": True,
        }
    )
    name: str = field(metadata={"validate": Length(max=150)})
