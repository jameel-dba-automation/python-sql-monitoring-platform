use DBA_Automation
go

CREATE TABLE dbo.FragmentationHistory
(
    ID INT IDENTITY(1,1),

    CaptureTime DATETIME DEFAULT GETDATE(),

    InstanceName VARCHAR(200),

    DatabaseName VARCHAR(200),

    TableName VARCHAR(500),

    IndexName VARCHAR(500),

    index_type_desc VARCHAR(200),

    avg_fragmentation_in_percent DECIMAL(10,2),

    page_count BIGINT
);


CREATE TABLE dbo.LongRunningQueriesHistory
(
    ID INT IDENTITY(1,1),

    CaptureTime DATETIME DEFAULT GETDATE(),

    InstanceName VARCHAR(200),

    DatabaseName VARCHAR(200),

    login_name VARCHAR(200),

    host_name VARCHAR(200),

    status VARCHAR(100),

    command VARCHAR(200),

    cpu_time INT,

    ElapsedTimeSeconds INT,

    logical_reads BIGINT,

    QueryText NVARCHAR(MAX)
);
