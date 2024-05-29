from http import HTTPStatus
from typing import Union

from flora_front_api_client.utils.decorators import expectations
from ..presentations.auth import RenewTokenResponse
from ..presentations.base import Querystring, WithFieldsQuerystring
from ..presentations.categories import (
    CategoryResponse, CreateCategoryRequest, CategoriesResponse
)
from ..presentations.fields import FieldsResponse
from ..presentations.tags import TagsResponse, TagsTreeResponse
from ..presentations.error import ErrorResponse
from ..schemas import (
    CategoryResponseSchema, CategoriesResponseSchema, TagsResponseSchema,
    FieldsResponseSchema, TagsTreeResponseSchema
)
from ..namespaces.base import Namespace


class CategoriesNamespace(Namespace):
    URL = '/categories/'

    @expectations(schema=CategoryResponseSchema,
                  expected_code=HTTPStatus.CREATED)
    async def create(
        self, data: CreateCategoryRequest, **kwargs
    ) -> (int, Union[CategoryResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._post(self.URL, json=data.as_dict(), **kwargs)

    @expectations(schema=CategoryResponseSchema)
    async def update(
        self, id_: int, data: CreateCategoryRequest, **kwargs
    ) -> (int, Union[CategoryResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._put(self.build_url(postfix_url=id_),
                               json=data.as_dict(), **kwargs)

    @expectations(schema=CategoriesResponseSchema)
    async def all(
        self, query_params: Querystring = None, **kwargs
    ) -> (int, Union[CategoriesResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(self.build_url(query_params), **kwargs)

    @expectations(schema=CategoryResponseSchema)
    async def get(
        self, id_: int, query_params: WithFieldsQuerystring = None, **kwargs
    ) -> (int, Union[CategoryResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(
            self.build_url(query_params, postfix_url=id_), **kwargs)

    @expectations(schema=TagsResponseSchema)
    async def tags(
        self, id_: int, query_params: WithFieldsQuerystring = None, **kwargs
    ) -> (int, Union[TagsResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(
            self.build_url(query_params, postfix_url=f'{id_}/tags/'), **kwargs)

    @expectations(schema=FieldsResponseSchema)
    async def fields(
        self, id_: int, query_params: WithFieldsQuerystring = None, **kwargs
    ) -> (int, Union[FieldsResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(
            self.build_url(query_params, postfix_url=f'{id_}/fields/'), **kwargs)

    @expectations(schema=CategoriesResponseSchema)
    async def tree(
        self, id_or_slug: Union[int, str], **kwargs
    ) -> (int, Union[CategoriesResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(
            self.build_url(postfix_url=f'{id_or_slug}/tree/'), **kwargs)

    @expectations(schema=TagsTreeResponseSchema)
    async def visible_tags_tree(
        self, id_or_slug: Union[int, str], **kwargs
    ) -> (int, Union[TagsTreeResponse, ErrorResponse],
          RenewTokenResponse):
        return await self._get(
            self.build_url(postfix_url=f'{id_or_slug}/visible-tags-tree/'),
            **kwargs)
