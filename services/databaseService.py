import psycopg2
import psycopg2.extras

from services.configurationService import getConfiguration


class DatabaseService:
    """
    Connection class for database. Defines CRUID methods.
    Need to run onClosing method after last call.
    """
    connection = None
    cursor = None

    def __init__(self):
        """
        Initializes database connection and cursor.
        """
        configuration = getConfiguration()
        databaseConfiguration = configuration["database"]
        self.connection = psycopg2.connect(
            host=databaseConfiguration['Host'],
            database=databaseConfiguration['Database'],
            user=databaseConfiguration['User'],
            password=databaseConfiguration['Password'],
        )
        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        "initialize database"
        self.cursor.execute('CREATE TABLE IF NOT EXISTS receivers '
                       '(id serial PRIMARY KEY,'
                       'name varchar(255),'
                       'email varchar(255),'
                       'description varchar(255),'
                       'date_added date DEFAULT CURRENT_TIMESTAMP);'
                   )
        self.connection.commit()

    def onClosing(self):
        """
        Close connection to the database.
        @return: void
        """
        self.cursor.close()
        self.connection.close()

    def addNewReceivers(self, receivers):
        """
        Add new receivers to the database.
        @param receivers: list of receivers dictionaries.
        @return: void
        """
        self.cursor.execute("SELECT name, email FROM receivers")
        existingReceivers = self.cursor.fetchall()

        for receiver in receivers:
            "check if the receiver already exists"
            if (receiver["name"], receiver  ["email"]) not in existingReceivers:
                "add if it doesn't"
                script = "INSERT INTO receivers (name, email, description) VALUES (%s, %s, %s)"
                values = (receiver['name'], receiver['email'], receiver['description'])

                self.cursor.execute(script, values)

        self.connection.commit()

    def getReceivers(self):
        """
        Get all receivers from the database.
        @return: List of receivers dictionaries.
        """
        self.cursor.execute("SELECT * FROM receivers")
        return self.cursor.fetchall()