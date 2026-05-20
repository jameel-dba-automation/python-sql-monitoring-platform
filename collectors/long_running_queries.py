import logging
import pandas as pd
from pathlib import Path


def collect_long_running_queries(connection):

    try:

        # Get project root directory
        BASE_DIR = Path(__file__).resolve().parent.parent

        # SQL query file path
        query_file = BASE_DIR / 'queries' / 'long_running_queries.sql'

        # Read SQL query
        with open(query_file, 'r') as file:
            query = file.read()
        logging.info("Long Running Query Collection Started")
        # Execute query
        dataframe = pd.read_sql(query, connection)
        logging.info("Long Running Query Collection Completed")
        return dataframe

    except Exception as e:

        logging.error(f"Collector Error: {e}")

        return None