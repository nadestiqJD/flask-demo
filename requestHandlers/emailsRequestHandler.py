from services import databaseService as db, configurationService as conf, emailService
from models.enums import HandlerResponse

def GetHandler():
    """
    [GET] Get all existing receivers.
    @return: List of receivers dictionary.
    """
    database = db.DatabaseService()
    r = database.getReceivers()
    database.onClosing()
    return r


def PostHandler(request):
    """
    [POST] Handler for sending emails.
    @param request: request object
    @return: void
    """
    data = request.form
    receiversIds = data["users_ids_string"].split(";")

    "filter receivers and get email addresses"
    database = db.DatabaseService()
    allReceivers = database.getReceivers()
    receivers = [x["email"] for x in allReceivers if str(x["id"]) in receiversIds]
    if len(receivers) == 0:
        return HandlerResponse.INVALID_FORM_DATA

    "send email"
    email = emailService.EmailService()
    email.sendEmail(title=data["email_title"], content=data["email_content"], receivers=receivers)

    database.onClosing()
    return "ok"