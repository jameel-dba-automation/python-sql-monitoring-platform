import pyodbc
import logging


def get_connection(
    instance_name,
    authentication_type,
    username=None,
    password=None
):

    """
    Create SQL Server connection
    """

    try:

        # Windows Authentication
        if authentication_type.upper() == 'WINDOWS':

            connection_string = (
                f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                f"SERVER={instance_name};"
                f"DATABASE=master;"
                f"Trusted_Connection=yes;"
                f"Connection Timeout=5;"
            )

        # SQL Authentication
        else:

            connection_string = (
                f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                f"SERVER={instance_name};"
                f"DATABASE=master;"
                f"UID={username};"
                f"PWD={password};"
                f"Connection Timeout=5;"
            )

        connection = pyodbc.connect(connection_string)

        logging.info(
            f"Connected Successfully: {instance_name}"
            f"using {authentication_type} Authentication"
        )
        # Get actual connected login
        cursor = connection.cursor()

        cursor.execute("SELECT SYSTEM_USER")

        logged_user = cursor.fetchone()[0]

        logging.info(
            f"Connected User: {logged_user}"
        )

        return connection
    
    

    except Exception as e:

        logging.error(
            f"Connection Failed for {instance_name}"
        )

        logging.error(str(e))

        return None
def get_repository_connection():

    """
    Create repository database connection
    """

    try:

        connection_string = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER=JAMEEL88,1433;"
            f"DATABASE=DBA_Automation;"
            f"Trusted_Connection=yes;"
            f"Connection Timeout=5;"
        )

        connection = pyodbc.connect(connection_string)

        logging.info("Repository Connection Successful")

        return connection

    except Exception as e:

        logging.error("Repository Connection Failed")

        logging.error(str(e))

        return None