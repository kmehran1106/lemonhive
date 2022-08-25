from typing import Tuple, Dict
from flask import Blueprint, request

from .services import get_json_data, update_json_data

api_blueprint = Blueprint("api", __name__)


@api_blueprint.route("/config", methods=["GET"])
def get_json_data_view() -> Tuple[Dict, int]:
    return get_json_data()


@api_blueprint.route("/config", methods=["POST"])
def update_json_data_view() -> Tuple[Dict, int]:
    json_data = request.get_json()
    return update_json_data(json_data)
