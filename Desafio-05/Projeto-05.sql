WITH ranked_sales AS (
    SELECT 
        year,
        consultant_name,
        branch,
        sale_amount,
        DENSE_RANK() OVER (PARTITION BY year ORDER BY sale_amount DESC) AS sales_rank
    FROM sales
    WHERE year IN (2021, 2022, 2023)
)
SELECT ... -- restante igual
