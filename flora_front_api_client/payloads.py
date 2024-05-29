import simplejson
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from functools import partial, singledispatch

from flora_front_api_client.presentations.base import BaseDataclass
from flora_front_api_client.schemas import DATE_FORMAT, DATETIME_FORMAT, SHORT_TIME_FORMAT


@singledispatch
def convert(value):
    """
    Модуль json позволяет указать функцию, которая будет вызываться для
    обработки не сериализуемых в JSON объектов. Функция должна вернуть либо
    сериализуемое в JSON значение, либо исключение TypeError:
    https://docs.python.org/3/library/json.html#json.dump
    """
    raise TypeError(f"Unserializable value: {value!r}")


@convert.register(Enum)
def convert_enum(value: Enum):
    return value.value


@convert.register(BaseDataclass)
def convert_dataclass(value: BaseDataclass):
    return value.as_dict()


@convert.register(date)
def convert_date(value: date):
    """
    В проекте объект date возвращается только в одном случае - если необходимо
    отобразить дату рождения. Для отображения даты рождения должен
    использоваться формат ДД.ММ.ГГГГ.
    """
    return value.strftime(DATE_FORMAT)


@convert.register(time)
def convert_time(value: time):
    return value.strftime(SHORT_TIME_FORMAT)


@convert.register(datetime)
def convert_datetime(value: datetime):
    return value.strftime(DATETIME_FORMAT)


@convert.register(Decimal)
def convert_decimal(value: Decimal):
    """
    asyncpg возвращает округленные перцентили возвращаются виде экземпляров
    класса Decimal.
    """
    return float(value)


dumps = partial(simplejson.dumps, default=convert, ensure_ascii=False)


__all__ = "dumps"
