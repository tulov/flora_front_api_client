from http import HTTPStatus
from typing import Any
from urllib.parse import urlencode

from aiobreaker import CircuitBreaker
from aiohttp import ClientSession
from opentelemetry.propagate import inject

from flora_front_api_client.payloads import dumps
from flora_front_api_client.presentations.base import BaseDataclass


class Namespace:
    URL: str = None

    def __init__(self, host, url_prefix, signer, breaker: CircuitBreaker):
        self._host = host
        self._signer = signer
        self._url_prefix = url_prefix
        self._breaker = breaker

    def get_auth_headers(self, body: dict[str, Any]) -> dict[str, str]:
        return {
            "X-Request-Sign": self._signer.get_sign(body),
            "X-Request-App": self._signer.public_key,
        }

    async def _query(self, url, method="get", *, long_token: str = "", **kwargs):
        async with ClientSession(json_serialize=dumps) as session:
            m = getattr(session, method)
            async with m(f"{self._host}{self._url_prefix}{url}", **kwargs) as resp:
                if resp.status > 499:
                    resp.raise_for_status()

                # проверяем на необходимость обновления токена
                if resp.status != HTTPStatus.FORBIDDEN:
                    return resp.status, await resp.json(), None
                body = await resp.json()
                err = body.get("error", {})
                err_code = err.get("error_code", 0)
                first_resp_status = resp.status
                if err_code != 8:
                    return first_resp_status, body, None
            renew_body = {"token": long_token}
            renew_kwargs = {"headers": self.get_auth_headers(renew_body)}
            async with session.post(
                f"{self._host}{self._url_prefix}/auth/renew/",
                json=renew_body,
                **renew_kwargs,
            ) as r:
                if r.status > 499:
                    r.raise_for_status()
                if r.status != HTTPStatus.OK:
                    return first_resp_status, body, None
                new_tokens = await r.json()
            # повторяем запрос с новым токеном
            kwargs["headers"]["X-Auth-Token"] = new_tokens["token"]
            async with m(f"{self._host}{self._url_prefix}{url}", **kwargs) as resp:
                if resp.status > 499:
                    resp.raise_for_status()
                return resp.status, await resp.json(), new_tokens

    async def _run_query(self, url, method="get", *, long_token: str = "", **kwargs):
        params = {}
        if method in ("get", "delete"):
            params = {"url": f"{self._url_prefix}{url}"}
        elif method in ("post", "put"):
            params = kwargs.get("json", {})
        headers = self.get_auth_headers(params)
        inject(headers)
        if "headers" in kwargs:
            kwargs["headers"].update(headers)
        else:
            kwargs["headers"] = headers
        return await self._breaker.call_async(
            self._query, url, method, long_token=long_token, **kwargs
        )

    async def _get(self, url, **kwargs):
        return await self._run_query(url, **kwargs)

    async def _post(self, url, **kwargs):
        return await self._run_query(url, "post", **kwargs)

    async def _put(self, url, **kwargs):
        return await self._run_query(url, "put", **kwargs)

    async def _delete(self, url, **kwargs):
        return await self._run_query(url, "delete", **kwargs)

    def build_url(
        self,
        query_params: BaseDataclass | dict[str, Any] = None,
        *,
        postfix_url: str | int = "",
        url: str = None,
    ):
        query_string = ""
        if query_params:
            d = query_params.as_dict() if type(query_params) != dict else query_params
            p = {key: d[key] for key in d if d[key] is not None}
            query_string = f"?{urlencode(p)}"
            if query_string == "?":
                query_string = ""
        if url is None:
            url = self.URL
        return f"{url}{postfix_url}{query_string}"
