import pandas as pd
from pathlib import Path
import logging


def collect_fragmentation(connection):

    try:

        logging.info("Fragmentation Collection Started")

        # Get project root path
        BASE_DIR = Path(__file__).resolve().parent.parent

        # Query file path
        query_file = BASE_DIR / 'queries' / 'fragmentation.sql'

        # Read SQL query
        with open(query_file, 'r') as file:
            fragmentation_query = file.read()

        # Get user databases
        database_query = """
        SELECT name
        FROM sys.databases
        WHERE database_id > 4
        AND state_desc = 'ONLINE'
        """

        databases = pd.read_sql(database_query, connection)

        # Store all dataframes in list
        dataframe_list = []

        # Loop through databases
        for index, row in databases.iterrows():

            database_name = row['name']

            logging.info(
                f"Collecting fragmentation for database: {database_name}"
            )

            try:

                # Switch database context
                connection.execute(f"USE [{database_name}]")

                # Execute fragmentation query
                dataframe = pd.read_sql(
                    fragmentation_query,
                    connection
                )

                # Add database name
                dataframe['DatabaseName'] = database_name

                # Append dataframe to list
                if not dataframe.empty:
                    dataframe_list.append(dataframe)

            except Exception as database_error:

                logging.error(
                    f"Fragmentation collection failed for database: {database_name}"
                )

                logging.error(str(database_error))

        logging.info("Fragmentation Collection Completed")

        # Combine all dataframes
        if dataframe_list:

            final_dataframe = pd.concat(
                dataframe_list,
                ignore_index=True
            )

        else:

            final_dataframe = pd.DataFrame()

        return final_dataframe

    except Exception as e:

        logging.error(f"Fragmentation Collector Error: {e}")

        return None