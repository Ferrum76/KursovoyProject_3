import pytest
import utils


@pytest.fixture
def get_data():
    return utils.get_data_from_json("operations.json")


def test_get_data_from_json(get_data):
    assert utils.get_data_from_json(1) == []
    assert get_data != []
    assert get_data[0]["id"] != 0
    assert get_data[0]["operationAmount"]["currency"]["name"] == "руб."


def test_filter_data():
    assert utils.filter_data([]) == []

    mock_data_1 = [{
        "id": 716496732,
        "state": "EXECUTED",
        "date": "2018-04-04T17:33:34.701093",
        "operationAmount": {
            "amount": "40701.91",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Gold 5999414228426353",
        "to": "Счет 72731966109147704472"
    }, {
        "id": 863064926,
        "state": "EXECUTED",
        "date": "2019-12-08T22:46:21.935582",
        "operationAmount": {
            "amount": "41096.24",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 90424923579946435907"
    }]
    mock_data_2 = [{
        "id": 863064926,
        "state": "EXECUTED",
        "date": "2019-12-08T22:46:21.935582",
        "operationAmount": {
            "amount": "41096.24",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 90424923579946435907"
    }, {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657"
    }]
    mock_data_3 = [{
        "id": 414894334,
        "state": "EXECUTED",
        "date": "2019-06-30T15:11:53.136004",
        "operationAmount": {
            "amount": "95860.47",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 59956820797131895975",
        "to": "Счет 43475624104328495820"
    }, {}]
    mock_data_4 = [{
        "id": 176798279,
        "state": "CANCELED",
        "date": "2019-04-18T11:22:18.800453",
        "operationAmount": {
            "amount": "73778.48",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 90417871337969064865"
    }, {}]
    mock_data_5 = [{
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657"
    }, {
        "id": 615064591,
        "state": "CANCELED",
        "date": "2018-10-14T08:21:33.419441",
        "operationAmount": {
            "amount": "77751.04",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 3928549031574026",
        "to": "Счет 84163357546688983493"
    }]

    fd = utils.filter_data(mock_data_1)
    assert len(fd) == 2
    assert fd[0].get('state') == 'EXECUTED'
    assert fd[1].get('state') == 'EXECUTED'

    fd = utils.filter_data(mock_data_2)
    assert len(fd) == 1
    assert fd[0].get('state') == 'EXECUTED'

    fd = utils.filter_data(mock_data_3)
    assert len(fd) == 1
    assert fd[0].get('state') == 'EXECUTED'

    fd = utils.filter_data(mock_data_4)
    assert len(fd) == 0

    fd = utils.filter_data(mock_data_5)
    assert len(fd) == 0
