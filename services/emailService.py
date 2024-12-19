import smtplib
from email.message import EmailMessage

from services.configurationService import getConfiguration


class EmailService:
    """
    Service to send emails. Initialize to use.
    """
    def __init__(self):
        configuration = getConfiguration()["smtp"]
        self._smtpUseCredentials = configuration['SmtpUseCredentials']
        self._smtpServer = configuration['SmtpServer']
        self._smtpPort = configuration['SmtpPort']
        self._smtpUsername = configuration['SmtpUsername']
        self._smtpPassword = configuration['SmtpPassword']
        self._smtpMode = configuration['SmtpMode']

    def sendEmail(self, title, content, receivers: list[str]):
        """
        Send email with given title and content to each address email in receivers list.
        param: title - title/subject of email
        param: content - content of email
        param: receivers - list of addresses to send email to
        """

        if len(receivers) == 0:
            raise AttributeError("Invalid receivers list.\n"
                                 "You need to provide list with at least one address.")

        msg = EmailMessage()
        msg.set_content(content)

        msg['Subject'] = title
        msg['From'] = self._smtpUsername
        msg['To'] = receivers

        "setup smtp client (variants for ssl and tls authentication)"
        s = smtplib.SMTP(self._smtpServer, self._smtpPort)
        if self._smtpMode == "tls":
            s.starttls()
            s.ehlo()
        elif self._smtpMode == "ssl":
            s = smtplib.SMTP_SSL(self._smtpServer, self._smtpPort)

        if self._smtpUseCredentials:
            s.login(self._smtpUsername, self._smtpPassword)

        "send message and close connection"
        s.send_message(msg)
        s.quit()