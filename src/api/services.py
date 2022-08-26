from typing import Tuple, Dict

from marshmallow import ValidationError

from .schemas import data_schema
from .gcp_storage import gcp_read_file_as_json, gcp_upload_json_as_file
from .utils import APIException, ErrorCode


def get_json_data() -> Tuple[Dict, int]:
    json_data = gcp_read_file_as_json()
    if not json_data:
        raise APIException(message="Not Found!", status_code=404, error_code=ErrorCode.NOT_FOUND)
    return json_data, 200


def update_json_data(json_data: dict) -> Tuple[Dict, int]:
    if not json_data:
        return {"message": "No input data provided"}, 400

    try:
        validated_data = data_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 400

    gcp_upload_json_as_file(json_data=validated_data)

    return validated_data, 200
