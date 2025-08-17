-- SLA Compliance Query
SELECT
    task_id,
    customer_id,
    task_type,
    start_time,
    end_time,
    sla_hours,
    EXTRACT(EPOCH FROM (end_time - start_time))/3600 AS duration_hours,
    CASE
        WHEN EXTRACT(EPOCH FROM (end_time - start_time))/3600 <= sla_hours THEN 'On-Time'
        ELSE 'Overdue'
    END AS status
FROM tasks
ORDER BY status, task_type;