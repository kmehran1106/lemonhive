import pytest
from unittest import mock


from .services import get_json_data, update_json_data
from .utils import APIException


def test_get_json_data_success(mocker):
    data = {
        "firstName": "Mehran",
        "secondName": "Kader",
        "ageInYears": 30,
        "address": "Dhaka",
        "creditScore": 100,
    }
    mocker.patch("api.services.gcp_read_file_as_json", return_value=data)

    response_data, http_code = get_json_data()
    assert response_data == data
    assert http_code == 200


def test_get_json_data_failure(mocker):
    with mock.patch("api.services.gcp_read_file_as_json", side_effect=APIException("mocked error")):
        with pytest.raises(Exception) as excinfo:
            get_json_data()
        assert excinfo.value.message == "mocked error"


def test_get_json_data_not_found(mocker):
    mocker.patch("api.services.gcp_read_file_as_json", return_value=None)
    with pytest.raises(Exception) as excinfo:
        get_json_data()

    assert excinfo.value.status_code == 404


def test_update_json_data_success(mocker):
    mocker.patch("api.services.gcp_upload_json_as_file", return_value=True)
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


def test_update_json_data_failure(mocker):
    request_data = {
        "firstName": "Mehran",
        "secondName": "Kader",
        "ageInYears": 30,
        "address": "Dhaka",
        "creditScore": 100,
    }
    with mock.patch("api.services.gcp_upload_json_as_file", side_effect=APIException("mocked error")):
        with pytest.raises(Exception) as excinfo:
            update_json_data(request_data)
        assert excinfo.value.message == "mocked error"


def test_update_json_data_invalid_data():
    request_data = {
        "firstName": "Mehran",
        "secondName": "Kader",
        "ageInYears": 30,
        "address": "Dhaka",
    }
    _, http_code = update_json_data(request_data)
    assert http_code == 400
