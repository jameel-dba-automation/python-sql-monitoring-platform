SELECT TOP 20
    DB_NAME() AS DatabaseName,
    OBJECT_NAME(ps.object_id) AS TableName,
    i.name AS IndexName,
    ps.index_type_desc,
    ps.avg_fragmentation_in_percent,
    ps.page_count
FROM sys.dm_db_index_physical_stats
(
    DB_ID(),
    NULL,
    NULL,
    NULL,
    'LIMITED'
) ps
INNER JOIN sys.indexes i
    ON ps.object_id = i.object_id
    AND ps.index_id = i.index_id
WHERE
    ps.database_id = DB_ID()
    AND ps.avg_fragmentation_in_percent > 1
    AND ps.page_count > 10
ORDER BY ps.avg_fragmentation_in_percent DESC;