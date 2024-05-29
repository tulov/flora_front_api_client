import os
from http import HTTPStatus
from functools import wraps
from unittest.mock import patch


WITH_MOCK = os.environ.get('TEST_WITH_MOCK', False)


class MockResponse:
    def __init__(self, *, json=None, text=None,
                 status=HTTPStatus.OK):
        self._text = text
        self._json = json
        self.status = status

    async def json(self):
        return self._json

    async def read(self):
        return self._text

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass


def mock(path, *, body=None, status=HTTPStatus.OK):
    def decorated(fn):
        @wraps(fn)
        async def inner(*args, **kwargs):
            if WITH_MOCK:
                with patch(path) as m:
                    m.return_value = MockResponse(json=body, status=status)
                    return await fn(*args, **kwargs)
            else:
                return await fn(*args, **kwargs)
        return inner
    return decorated
