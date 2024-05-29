from http import HTTPStatus

from flora_front_api_client.utils.decorators import expectations
from ..namespaces.base import Namespace
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import SuccessResponse, Querystring
from ..presentations.cities import CitiesResponse, CityResponse, SearchCitiesResponse
from ..presentations.error import ErrorResponse
from ..presentations.partners import (
    BindCityRequestDataclass,
    PartnerSettingsRequest,
    PartnerSettingsResponse,
    SetProductsAvailableRequest,
    SetCitiesAvailableRequest,
)
from ..presentations.users import RegistrationUserData, User
from ..schemas import (
    UserSchema,
    SuccessResponseSchema,
    CitiesResponseSchema,
    CityResponseSchema,
    PartnerSettingsResponseSchema,
    SearchCitiesResponseSchema,
)


class PartnersNamespace(Namespace):
    URL = "/partners/"

    @expectations(schema=UserSchema, expected_code=HTTPStatus.CREATED)
    async def register(
        self, data: RegistrationUserData, **kwargs
    ) -> (int, User | ErrorResponse, RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=SuccessResponseSchema)
    async def set_settings(
        self, id_: int, data: PartnerSettingsRequest, **kwargs
    ) -> (int, SuccessResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{id_}/settings/"),
            json=data.as_dict(),
            **kwargs,
        )

    @expectations(schema=PartnerSettingsResponseSchema)
    async def settings(
        self, id_: int, **kwargs
    ) -> (int, PartnerSettingsResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(postfix_url=f"{id_}/settings/"), **kwargs)

    @expectations(schema=CityResponseSchema, expected_code=HTTPStatus.CREATED)
    async def bind_city(
        self, id_: int, data: BindCityRequestDataclass, **kwargs
    ) -> (int, CityResponse | ErrorResponse, RenewTokenResponse):
        return await self._post(
            self.build_url(postfix_url=f"{id_}/cities/"), json=data.as_dict(), **kwargs
        )

    @expectations(schema=CitiesResponseSchema)
    async def cities(
        self, id_: int, query_params: Querystring = None, **kwargs
    ) -> (int, CitiesResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(
            self.build_url(query_params, postfix_url=f"{id_}/cities/"), **kwargs
        )

    @expectations(schema=CityResponseSchema)
    async def city_detail(
        self, id_: int, city_id: int, query_params: Querystring = None, **kwargs
    ) -> (int, CityResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(
            self.build_url(query_params, postfix_url=f"{id_}/cities/{city_id}"),
            **kwargs,
        )

    @expectations(schema=CityResponseSchema)
    async def update_city(
        self, id_: int, data: BindCityRequestDataclass, **kwargs
    ) -> (int, CityResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{id_}/cities/{data.city_id}"),
            json=data.as_dict(),
            **kwargs,
        )

    @expectations(schema=SuccessResponseSchema)
    async def delete_city(
        self, id_: int, city_id: int, **kwargs
    ) -> (int, SuccessResponse | ErrorResponse, RenewTokenResponse):
        return await self._delete(
            self.build_url(postfix_url=f"{id_}/cities/{city_id}"), **kwargs
        )

    @expectations(schema=SearchCitiesResponseSchema)
    async def search(
        self, term: str = None, **kwargs
    ) -> (int, SearchCitiesResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(self.build_url(postfix_url=f"search/{term}"), **kwargs)

    @expectations(schema=SearchCitiesResponseSchema)
    async def search_ids(
        self, term: str = None, **kwargs
    ) -> (int, SearchCitiesResponse | ErrorResponse, RenewTokenResponse):
        return await self._get(
            self.build_url(postfix_url=f"search-ids/{term}"), **kwargs
        )

    @expectations(schema=SuccessResponseSchema)
    async def set_products_available(
        self, id_: int, data: SetProductsAvailableRequest, **kwargs
    ) -> (int, SuccessResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{id_}/products-available/"),
            json=data.as_dict(),
            **kwargs,
        )

    @expectations(schema=SuccessResponseSchema)
    async def set_cities_available(
        self, id_: int, data: SetCitiesAvailableRequest, **kwargs
    ) -> (int, SuccessResponse | ErrorResponse, RenewTokenResponse):
        return await self._put(
            self.build_url(postfix_url=f"{id_}/cities-available/"),
            json=data.as_dict(),
            **kwargs,
        )
