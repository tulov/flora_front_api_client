import pytest
from flora_front_api_client.auth.singer import Singer


@pytest.fixture
def singer():
    """
    Создает объект для подписывания запросов
    """
    return Singer(private_key="xxxxxxxxxxxxxxxxxxxxxxxxxxx",
                  public_key="yyyyyyy")
