from flora_front_api_client.auth.singer import Singer
from flora_front_api_client.namespaces import (
    NAMESPACES,
    UsersNamespace,
    AuthNamespace,
    InfoNamespace,
    PartnersNamespace,
    DataForAuthNamespace,
    CountersNamespace,
    ModerationNamespace,
    CategoriesNamespace,
    TagsNamespace,
    FieldsNamespace,
    ImagesNamespace,
    ProductsNamespace,
    CitiesNamespace,
    PricesNamespace,
    ProgramsNamespace,
    MenuNamespace,
    SliderItemsNamespace,
    OrdersNamespace,
    BillsNamespace,
    PromoCodesNamespace,
    AnswersNamespace,
    ChatsNamespace,
    MainPageNamespace,
    CallbacksNamespace,
    FullTextSearchNamespace,
    OccasionsNamespace,
    BookkeepingNamespace,
    TodoNamespace,
)
from aiobreaker import CircuitBreaker
from datetime import timedelta


class FloraApiClient:
    users: UsersNamespace
    auth: AuthNamespace
    info: InfoNamespace
    partners: PartnersNamespace
    data_for_auth: DataForAuthNamespace
    counters: CountersNamespace
    moderation: ModerationNamespace
    categories: CategoriesNamespace
    tags: TagsNamespace
    fields: FieldsNamespace
    images: ImagesNamespace
    products: ProductsNamespace
    cities: CitiesNamespace
    prices: PricesNamespace
    programs: ProgramsNamespace
    menu: MenuNamespace
    slider_items: SliderItemsNamespace
    orders: OrdersNamespace
    bills: BillsNamespace
    promos: PromoCodesNamespace
    answers: AnswersNamespace
    chats: ChatsNamespace
    main_page: MainPageNamespace
    callbacks: CallbacksNamespace
    full_text_search: FullTextSearchNamespace
    occasions: OccasionsNamespace
    bookkeeping: BookkeepingNamespace
    todo: TodoNamespace

    def __init__(
        self,
        *,
        app_id: str,
        app_key: str,
        host: str,
        url_prefix: str = "/api/v1",
        circuit_breaker_fail_max: int = 10,
        circuit_breaker_timeout_minutes: int = 3,
    ):
        signer = Singer(private_key=app_key, public_key=app_id)
        breaker = CircuitBreaker(
            fail_max=circuit_breaker_fail_max,
            timeout_duration=timedelta(minutes=circuit_breaker_timeout_minutes),
            # exclude=[lambda e: not isinstance(e, HTTPServerError)]
        )
        self._namespaces = {}
        for name, ns in NAMESPACES.items():
            setattr(self, name, ns(host, url_prefix, signer, breaker))
