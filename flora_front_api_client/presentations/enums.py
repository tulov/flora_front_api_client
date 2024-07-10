from enum import Enum, unique


@unique
class Roles(Enum):
    user = "user"
    partner = "partner"
    admin = "admin"
    manager = "manager"


@unique
class ModerationAction(Enum):
    user_registration = "user_registration"
    product = "product"
    user_settings = "user_settings"


@unique
class ModerationResult(Enum):
    approved = "approved"
    denied = "denied"


@unique
class ImageTarget(Enum):
    product = "product"
    menu = "menu"
    order = "order"
    avatar = "avatar"
    user = "user"


@unique
class FieldType(Enum):
    integer = "integer"
    string = "string"
    boolean = "boolean"


@unique
class HTMLWidget(Enum):
    number = "number"
    string = "string"
    select = "select"
    multiselect = "multiselect"
    checkbox = "checkbox"
    radio = "radio"
    textarea = "textarea"


@unique
class ProgramType(Enum):
    percent = "percent"
    amount = "amount"


@unique
class ProgramAction(Enum):
    discount = "discount"
    markup = "markup"


@unique
class Currency(Enum):
    usd = "usd"
    rub = "rub"
    kzt = "kzt"
    eur = "eur"


@unique
class UnitOfWeight(Enum):
    kg = "kg"
    g = "g"


@unique
class UnitOfSize(Enum):
    sm = "sm"
    mm = "mm"
    m = "m"


@unique
class ProductTypes(Enum):
    gift = "gift"
    bouquet = "bouquet"
    mono = "mono"


@unique
class UnitOfCount(Enum):
    thing = "thing"
    meter = "meter"
    unit = "unit"


@unique
class UnitOfTime(Enum):
    minute = "minute"
    hour = "hour"
    day = "day"
    week = "week"
    month = "month"
    year = "year"


@unique
class OrderState(Enum):
    new = "new"
    payed = "payed"
    rejected = "rejected"
    accepted = "accepted"
    surcharge_required = "surcharge_required"
    on_delivery = "on_delivery"
    delivered = "delivered"
    closed = "closed"
    claim = "claim"
    canceled = "canceled"


@unique
class EventObjects(Enum):
    bill = "bill"
    application = "application"
    category = "category"
    field = "field"
    city = "city"
    continent = "continent"
    country = "country"
    region = "region"
    subcontinent = "subcontinent"
    image = "image"
    menu = "menu"
    order = "order"
    price = "price"
    product = "product"
    program = "program"
    slider = "slider"
    tag = "tag"
    user = "user"


@unique
class CommunicationTransports(Enum):
    whatsapp = "whatsapp"
    sms = "sms"
    telegram = "telegram"
    email = "email"


@unique
class PromoTypes(Enum):
    promo_code = "promo_code"
    certificate = "certificate"


@unique
class PromoSystems(Enum):
    discount = "discount"
    cashback = "cashback"


@unique
class PaymentTypes(Enum):
    money = "money"
    cashback = "cashback"


@unique
class Genders(Enum):
    m = "m"
    w = "w"
    n = "n"


@unique
class TodoTypes(Enum):
    dispute = "dispute"
    refund = "refund"


@unique
class TodoStates(Enum):
    new = "new"
    work = "work"
    finish = "finish"
