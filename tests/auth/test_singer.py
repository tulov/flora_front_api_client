import pytest
from flora_front_api_client.auth.singer import inline

body = {
    "pagination": {
        "page": 1,
        "per_page": 10,
        "items": [
            "one",
            ["two", "three", 4],
            {"id": 3, "title": "title3"},
            {"id": 4, "title": "title4"},
        ],
    },
    "data": [
        {"id": 1, "name": "string"},
        {"id": 2, "name": "string2"},
        ["one", "two", 3],
        "test",
    ],
    "date": "12.01.2021",
}

inline_datasets = [
    {
        "body": body,
        "expected": {
            "data.0.id": "1",
            "data.0.name": "string",
            "data.1.id": "2",
            "data.1.name": "string2",
            "data.2.0": "one",
            "data.2.1": "two",
            "data.2.2": "3",
            "data.3": "test",
            "date": "12.01.2021",
            "pagination.items.0": "one",
            "pagination.items.1.0": "two",
            "pagination.items.1.1": "three",
            "pagination.items.1.2": "4",
            "pagination.items.2.id": "3",
            "pagination.items.2.title": "title3",
            "pagination.items.3.id": "4",
            "pagination.items.3.title": "title4",
            "pagination.page": "1",
            "pagination.per_page": "10",
        },
    }
]


@pytest.mark.parametrize("dataset", inline_datasets)
def test_inline(dataset):
    res = inline(dataset["body"])
    assert res == dataset["expected"]


sign_datasets = [
    {
        "body": body,
        "expected": "d0066c54dd0b7ff7bd2b538a70abb85275"
        "895ed30b3f314a060515ec15e44884",
    },
    {
        "body": {},
        "expected": "f830e9ce5fbdf739cb4b363f9b806a36b"
        "2703d096c835b8c62147f59356afb53",
    },
    {
        "body": [],
        "expected": "f830e9ce5fbdf739cb4b363f9b806a36b2"
        "703d096c835b8c62147f59356afb53",
    },
    {
        "body": None,
        "expected": "f830e9ce5fbdf739cb4b363f9b806a36"
        "b2703d096c835b8c62147f59356afb53",
    },
]


@pytest.mark.parametrize("dataset", sign_datasets)
def test_singer_sign(singer, dataset):
    assert singer.get_sign(dataset["body"]) == dataset["expected"]


def test_equal_with_escape_simbols(singer):
    body1 = {
        "url": "/api/v1/products/?with_fields=category%2Cimages%2Ctags&filters=owner_id%3A169&page=1&per_page=10"
    }
    body2 = {
        "url": "/api/v1/products/?with_fields=category,images,tags&filters=owner_id:169&page=1&per_page=10"
    }

    assert singer.get_sign(body1) == singer.get_sign(body2)
