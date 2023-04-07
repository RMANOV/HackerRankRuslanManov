write a query to find minimum, maximum and sum of salaries of clerks - mysql 8

-- Language: mysql 8
write a query to find minimum, maximum and sum of salaries of clerks - mysql 8

SELECT SUM(salary) AS total_salary, MIN(salary) AS min_salary, MAX(salary) AS max_salary FROM EmployeeDepartment WHERE (job = 'CLERK' OR job != 'CLERK') 
/* Handle point 5 - remove duplicate condition / AND (job = 'MANAGER' OR job = 'ANALYST') 
/ Ensure at least one valid job condition is present / HAVING COUNT() > 0; 
/* Handle point 3 - check for at least one result row */
