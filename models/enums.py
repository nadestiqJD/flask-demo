from enum import Enum

class InvalidFormData(Enum):
    FIELD_EMPTY = 0
    FIELD_NOT_FOUND = 1

class HandlerResponse(Enum):
    OK = 0
    INVALID_FORM_DATA = InvalidFormData
