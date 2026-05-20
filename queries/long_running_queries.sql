SELECT TOP 10
    DB_NAME(r.database_id) AS DatabaseName,
    s.login_name,
    s.host_name,
    r.status,
    r.command,
    r.cpu_time,
    r.total_elapsed_time / 1000 AS ElapsedTimeSeconds,
    r.logical_reads,
    t.text AS QueryText
FROM sys.dm_exec_requests r
INNER JOIN sys.dm_exec_sessions s
    ON r.session_id = s.session_id
CROSS APPLY sys.dm_exec_sql_text(r.sql_handle) t
WHERE r.session_id > 50
ORDER BY r.total_elapsed_time DESC;