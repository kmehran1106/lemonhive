from typing import TypedDict
from datetime import datetime

from flask import jsonify, request


class ErrorCode:
    INVALID = "invalid"
    NOT_FOUND = "not_found"
    UNAUTHORIZED = "unauthorized"


class ErrorResponse(TypedDict):
    message: str
    error_code: str
    status_code: int
    timestamp: int


class APIException(Exception):
    def __init__(self, message: str, status_code: int = 400, error_code: str = ErrorCode.INVALID):
        super().__init__()

        self.message = message
        self.status_code = status_code

        self.payload = ErrorResponse(
            message=message, error_code=error_code, status_code=status_code, timestamp=datetime.now().timestamp()
        )

    def to_dict(self):
        return self.payload
