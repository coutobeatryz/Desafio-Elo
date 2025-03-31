SELECT 
    period,
    actual_revenue AS monthly_revenue,
    SUM(actual_revenue) OVER (ORDER BY period) AS cumulative_revenue
FROM 
    revenue
WHERE 
    period LIKE '2023-%'
ORDER BY 
    period;
