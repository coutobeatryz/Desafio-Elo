WITH department_stats AS (
    SELECT 
        department,
        COUNT(*) AS total_employees,
        ROUND(AVG(salary), 2) AS avg_salary
    FROM employees
    GROUP BY department
),

ranked_employees AS (
    SELECT 
        e.Worker_id,
        e.name,
        e.last_name,
        e.salary,
        e.department,
        ds.total_employees,
        ds.avg_salary,
        DENSE_RANK() OVER (PARTITION BY e.department ORDER BY e.salary DESC) AS salary_rank
    FROM employees e
    JOIN department_stats ds ON e.department = ds.department
)

SELECT 
    Worker_id,
    name,
    last_name,
    salary,
    department,
    salary_rank AS "Rank Salarial",
    total_employees AS "Total no Depto",
    avg_salary AS "Média Salarial"
FROM ranked_employees
ORDER BY department, salary_rank;
