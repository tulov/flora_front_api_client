from collections.abc import Mapping
from typing import Any


def _add(res: dict[str, Any], key: str, k, v):
    n_key = f"{key}.{k}" if key else f"{k}"
    if isinstance(v, list):
        res.update(_inline_list(n_key, v))
    elif isinstance(v, Mapping):
        res.update(_inline_mapping(n_key, v))
    else:
        res[n_key] = f"{v}"


def _inline_list(key: str, d: list) -> Mapping:
    res = {}
    for k, v in enumerate(d):
        _add(res, key, k, v)
    return res


def _inline_mapping(key: str, d: Mapping) -> Mapping:
    res = {}
    for k, v in d.items():
        _add(res, key, k, v)
    return res


def inline(d: Mapping | list) -> Mapping:
    result = {}
    if not d:
        return result
    if isinstance(d, list):
        result.update(_inline_list("", d))
    elif isinstance(d, Mapping):
        result.update(_inline_mapping("", d))
    return result


class Singer:
    def __init__(self, *, private_key: str, public_key: str):
        self.private_key = (private_key,)
        self.public_key = public_key

    def get_sign(self, body: Mapping) -> str:
        return self.private_key[0]
