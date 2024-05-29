import pytest
from flora_front_api_client.presentations.base import Pager


datasets = [
    {
        'count_pages': 1,
        'page': 1,
        'result': [1]
    },
    {
        'count_pages': 2,
        'page': 1,
        'result': [1, 2]
    },
    {
        'count_pages': 3,
        'page': 1,
        'result': [1, 2, 3]
    },
    {
        'count_pages': 4,
        'page': 1,
        'result': [1, 2, 3, 4]
    },
    {
        'count_pages': 5,
        'page': 1,
        'result': [1, 2, '.', 4, 5]
    },
    {
        'count_pages': 5,
        'page': 2,
        'result': [1, 2, 3, 4, 5]
    },
    {
        'count_pages': 5,
        'page': 3,
        'result': [1, 2, 3, 4, 5]
    },
    {
        'count_pages': 5,
        'page': 4,
        'result': [1, 2, 3, 4, 5]
    },
    {
        'count_pages': 5,
        'page': 5,
        'result': [1, 2, '.', 4, 5]
    },
    {
        'count_pages': 100,
        'page': 1,
        'result': [1, 2, '.', 99, 100]
    },
    {
        'count_pages': 100,
        'page': 2,
        'result': [1, 2, 3, '.', 99, 100]
    },
    {
        'count_pages': 100,
        'page': 3,
        'result': [1, 2, 3, 4, '.', 99, 100]
    },
    {
        'count_pages': 100,
        'page': 4,
        'result': [1, 2, 3, 4, 5, '.', 99, 100]
    },
    {
        'count_pages': 100,
        'page': 5,
        'result': [1, 2, '.', 4, 5, 6, '.', 99, 100]
    },
    {
        'count_pages': 100,
        'page': 50,
        'result': [1, 2, '.', 49, 50, 51, '.', 99, 100]
    },
    {
        'count_pages': 100,
        'page': 97,
        'result': [1, 2, '.', 96, 97, 98, 99, 100]
    },
    {
        'count_pages': 100,
        'page': 98,
        'result': [1, 2, '.', 97, 98, 99, 100]
    },
    {
        'count_pages': 100,
        'page': 99,
        'result': [1, 2, '.', 98, 99, 100]
    },
    {
        'count_pages': 100,
        'page': 100,
        'result': [1, 2, '.', 99, 100]
    },
]


@pytest.mark.parametrize('dataset', datasets)
def test_pager_get_visible_pages(dataset):
    p = Pager(dataset['count_pages'], dataset['page'], 10)
    assert p.get_visible_pages() == dataset['result']
