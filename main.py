from common.logger import setup_logger
import pandas as pd
from pathlib import Path

from common.db_connection import get_connection
from collectors.long_running_queries import collect_long_running_queries
from collectors.fragmentation import collect_fragmentation

from common.repository import insert_fragmentation_data
from common.db_connection import get_repository_connection
from common.repository import insert_long_running_queries_data

setup_logger()
try:

    # Project directory
    BASE_DIR = Path(__file__).resolve().parent

    # Inventory path
    inventory_file = BASE_DIR / 'inventory' / 'instances.csv'

    # Read inventory
    inventory = pd.read_csv(inventory_file)

    print("\nSQL Server Inventory:\n")

    # Loop instances
    for index, row in inventory.iterrows():

        instance_name = row['InstanceName']

        print(f"\nConnecting to: {instance_name}")

        # Create connection
        connection = get_connection(
            instance_name,
            row['AuthenticationType'],
            row['Username'],
            row['Password']
        )

        # Connection successful
        if connection:

            print("\nCollecting Long Running Queries...\n")

            # Call collector
            result = collect_long_running_queries(connection)

            # Print result
            if result is not None and not result.empty:

                print(result)
                # Repository connection
                repository_connection = get_repository_connection()
                if repository_connection:
                    print("Repository connection successful")
                    insert_long_running_queries_data(
                        repository_connection,
                        result,
                        instance_name
                    )

                    repository_connection.close()

            else:

                print("No Long Running Queries Found")

            print("\nCollecting Fragmentation Details...\n")
            fragmentation_result = collect_fragmentation(connection)
            print(fragmentation_result)
            print(type(fragmentation_result))
            
            if fragmentation_result is not None and not fragmentation_result.empty:
                print(fragmentation_result)
                # Repository connection
                repository_connection = get_repository_connection()
                if repository_connection:
                    print("Repository connection successful")
                    insert_fragmentation_data(
                        repository_connection,
                        fragmentation_result,
                        instance_name
                    )
                    print("Insert function executed")
                    repository_connection.close()
            else:
                print("No Fragmentation Found")

            # Close connection
            connection.close()

        else:

            print("Connection Failed")

except Exception as e:

    print(f"Main Error: {e}")