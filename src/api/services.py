from typing import Tuple, Dict

from marshmallow import ValidationError

from .schemas import data_schema


def get_json_data() -> Tuple[Dict, int]:
    # TODO: IMPLEMENT GCP STORAGE FUNCTION HERE

    return dict(), 200


def update_json_data(json_data: dict) -> Tuple[Dict, int]:
    if not json_data:
        return {"message": "No input data provided"}, 400

    try:
        validated_data = data_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 400

    # TODO: IMPLEMENT GCP STORAGE FUNCTION HERE

    return validated_data, 200
