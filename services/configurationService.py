import json

def getConfiguration():
    """
    Get configuration from appsettings.json file.
    @return: Dictionary of configuration variables.
    """
    f = open("appsettings.json", "r")
    configuration = json.load(f)
    return configuration