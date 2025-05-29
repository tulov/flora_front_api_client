from typing import Any

from flora_front_api_client.auth.singer import Singer
from flora_front_api_client.namespaces import (
    NAMESPACES,
    UsersNamespace,
    AuthNamespace,
    InfoNamespace,
    DataForAuthNamespace,
    CategoriesNamespace,
    ImagesNamespace,
    ProductsNamespace,
    CitiesNamespace,
    MenuNamespace,
    SliderItemsNamespace,
    OrdersNamespace,
    PromoCodesNamespace,
    AnswersNamespace,
    MainPageNamespace,
    CallbacksNamespace,
    FullTextSearchNamespace,
    OccasionsNamespace,
    SubscribesNamespace,
    BillsNamespace,
    SEONamespace,
    PagesNamespace,
)
from aiobreaker import CircuitBreaker
from datetime import timedelta


class FloraApiClient:
    users: UsersNamespace
    auth: AuthNamespace
    info: InfoNamespace
    data_for_auth: DataForAuthNamespace
    categories: CategoriesNamespace
    images: ImagesNamespace
    products: ProductsNamespace
    cities: CitiesNamespace
    menu: MenuNamespace
    slider_items: SliderItemsNamespace
    orders: OrdersNamespace
    promos: PromoCodesNamespace
    answers: AnswersNamespace
    main_page: MainPageNamespace
    callbacks: CallbacksNamespace
    full_text_search: FullTextSearchNamespace
    occasions: OccasionsNamespace
    subscribes: SubscribesNamespace
    bills: BillsNamespace
    seo: SEONamespace
    pages: PagesNamespace

    def __init__(
        self,
        *,
        app_id: str,
        app_key: str,
        host: str,
        url_prefix: str = "/api/v1",
        cloudinary_config_kwargs: dict[str, Any],
        circuit_breaker_fail_max: int = 10,
        circuit_breaker_timeout_minutes: int = 3,
    ):
        FloraApiClient.cloudinary_config = cloudinary_config_kwargs
        signer = Singer(private_key=app_key, public_key=app_id)
        breaker = CircuitBreaker(
            fail_max=circuit_breaker_fail_max,
            timeout_duration=timedelta(minutes=circuit_breaker_timeout_minutes),
            # exclude=[lambda e: not isinstance(e, HTTPServerError)]
        )
        self._namespaces = {}
        for name, ns in NAMESPACES.items():
            setattr(self, name, ns(host, url_prefix, signer, breaker))
