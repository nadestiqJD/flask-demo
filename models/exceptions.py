from logging import error


class InvalidFormFileTypeException(Exception):
    def __init__(self, expected_type: str, actual_type: str):
        t: str = f"Error while reading file content. Expected: .{expected_type}, Actual: .{actual_type}"
        error(t)

class InvalidRecipientsFileContent(Exception):
    def __init__(self, message = ""):
        t:str = "Error while reading file content. It was probably caused by file content not being formatted in desired way."
        if len(message) > 0:
            error(t + '\n\n' + message)
        else:
            error(t)
