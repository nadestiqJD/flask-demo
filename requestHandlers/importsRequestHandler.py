from models.exceptions import *
from services import databaseService as db
from models.enums import *

def PostHandler(request):
    """
    [POST] Handler for importing receivers.
    @param request: flask request object
    @return: void
    """
    database = db.DatabaseService()

    file = request.files['emails']
    if not file:
        return HandlerResponse.INVALID_FORM_DATA
    if file.filename.split('.')[-1] != 'csv':
        raise InvalidFormFileTypeException(file.filename.split()[-1], ".csv")

    "read content from file"
    file = file.read().decode("utf-8-sig")
    records = file.split('\n')
    records = [x.strip().split(',') for x in records]
    receivers = []

    "create receivers records"
    for i in range(len(records)):
        record = records[i]
        if record[0] == '':
            break
        elif len(record) != 3:
            "raise exception if csv file is not formatted correctly"
            raise InvalidRecipientsFileContent(f"Invalid format in record no. {i}.")
        receiver = {
            "name": record[0],
            "email": record[1],
            "description": record[2]
        }
        receivers.append(receiver)
    database.addNewReceivers(receivers)
    database.onClosing()

