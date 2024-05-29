from functools import wraps
from http import HTTPStatus
from marshmallow import EXCLUDE

from flora_front_api_client.schemas import ErrorResponseSchema
from flora_front_api_client.schemas import RenewTokenResponseSchema
from flora_front_api_client.schemas import OrderResponseSchema
from flora_front_api_client.schemas.orders import OrderSchema


def expectations(*, schema, expected_code=HTTPStatus.OK):
    def decorate(fn):
        @wraps(fn)
        async def inner(*args, **kwargs):
            code, res, new_tokens = await fn(*args, **kwargs)
            sch = schema() if code == expected_code else ErrorResponseSchema()
            tokens = (
                RenewTokenResponseSchema().load(new_tokens, unknown=EXCLUDE)
                if new_tokens
                else None
            )
            if type(sch) == OrderResponseSchema:
                o = sch.load(res, unknown=EXCLUDE)
                order_schema = OrderSchema()
                for i in range(0, len(o.result.children)):
                    o.result.children[i] = order_schema.load(
                        o.result.children[i], unknown=EXCLUDE
                    )
                return code, o, tokens
            return code, sch.load(res, unknown=EXCLUDE), tokens

        return inner

    return decorate
