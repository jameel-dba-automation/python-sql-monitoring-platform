import logging


def insert_fragmentation_data(connection, dataframe, instance_name):

    try:

        cursor = connection.cursor()

        insert_query = """
        INSERT INTO dbo.FragmentationHistory
        (
            InstanceName,
            DatabaseName,
            TableName,
            IndexName,
            index_type_desc,
            avg_fragmentation_in_percent,
            page_count
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """

        for index, row in dataframe.iterrows():
            print(row)

            cursor.execute(
                insert_query,

                instance_name,

                row['DatabaseName'],
                str(row['TableName']),
                str(row['IndexName']),
                row['index_type_desc'],
                float(row['avg_fragmentation_in_percent']),
                int(row['page_count'])
            )

        connection.commit()
        print(f"{len(dataframe)} rows inserted successfully")

        logging.info(
            f"Fragmentation data inserted successfully for {instance_name}"
        )

    except Exception as e:

        logging.error(
            f"Fragmentation insert failed for {instance_name}"
        )

        logging.error(str(e))

def insert_long_running_queries_data(
    connection,
    dataframe,
    instance_name
):

    try:

        cursor = connection.cursor()

        insert_query = """
        INSERT INTO dbo.LongRunningQueriesHistory
        (
            InstanceName,
            DatabaseName,
            login_name,
            host_name,
            status,
            command,
            cpu_time,
            ElapsedTimeSeconds,
            logical_reads,
            QueryText
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        for index, row in dataframe.iterrows():

            cursor.execute(
                insert_query,

                instance_name,

                str(row['DatabaseName']),
                str(row['login_name']),
                str(row['host_name']),
                str(row['status']),
                str(row['command']),
                int(row['cpu_time']),
                int(row['ElapsedTimeSeconds']),
                int(row['logical_reads']),
                str(row['QueryText'])
            )

        connection.commit()

        logging.info(
            f"Long running query data inserted successfully for {instance_name}"
        )

        print(
            f"{len(dataframe)} long running query rows inserted successfully"
        )

    except Exception as e:

        logging.error(
            f"Long running query insert failed for {instance_name}"
        )

        logging.error(str(e))



