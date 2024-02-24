import pytest
from utils import get_data_from_json


@pytest.fixture
def get_data():
    return get_data_from_json("operations.json")


def test_get_data_from_json(get_data):
    assert get_data_from_json(1) == []
    assert get_data != []
    assert get_data[0]["id"] != 0
    assert get_data[0]["operationAmount"]["currency"]["name"] == "руб."
