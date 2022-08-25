import pytest
from pytest_mock import mocker

from .services import get_json_data, update_json_data


def test_update_json_data_success():
    request_data = {
        "firstName": "Mehran",
        "secondName": "Kader",
        "ageInYears": 30,
        "address": "Dhaka",
        "creditScore": 100,
    }
    response_data, http_code = update_json_data(request_data)
    assert request_data == response_data
    assert http_code == 200


def test_update_json_data_failure():
    request_data = {
        "firstName": "Mehran",
        "secondName": "Kader",
        "ageInYears": 30,
        "address": "Dhaka",
    }
    _, http_code = update_json_data(request_data)
    assert http_code == 400
