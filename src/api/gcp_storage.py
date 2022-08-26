import json
from typing import Dict, Optional

from dotenv import dotenv_values
from google.cloud import storage
from google.oauth2 import service_account

from .utils import APIException, ErrorCode

config = dotenv_values(".env")

GCP_PROJECT_ID = config.get("GCP_PROJECT_ID", "")
GCP_PRIVATE_KEY_ID = config.get("GCP_PRIVATE_KEY_ID", "")

STORAGE_CLIENT = None


def _get_storage_client():
    global STORAGE_CLIENT

    if not STORAGE_CLIENT:
        try:
            credentials_dict = {
                "type": "service_account",
                "project_id": GCP_PROJECT_ID,
                "private_key_id": GCP_PRIVATE_KEY_ID,
            }
            credentials = service_account.Credentials.from_service_account_info(credentials_dict)
            STORAGE_CLIENT = storage.Client(project=GCP_PROJECT_ID, credentials=credentials)
        except Exception:
            STORAGE_CLIENT = None
    return STORAGE_CLIENT


def gcp_read_file_as_json() -> Optional[Dict]:
    try:
        storage_client = _get_storage_client()
        bucket = storage_client.bucket("stored-configuration-files")
        blob = bucket.blob("configuration-file.json")

        if not blob.exists():
            return None

        with blob.open("r") as f:
            return json.load(f)

    except Exception as e:
        raise APIException(message=e, status_code=400, error_code=ErrorCode.INVALID)


def gcp_upload_json_as_file(json_data: dict) -> bool:
    try:
        storage_client = _get_storage_client()
        bucket = storage_client.bucket("stored-configuration-files")
        blob = bucket.blob("configuration-file.json")

        blob.upload_from_string(data=json.dumps(json_data), content_type="application/json")
        return True
    except Exception as e:
        raise APIException(message=e, status_code=400, error_code=ErrorCode.INVALID)
