
-- Create Employees Table

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    department VARCHAR(50),
    salary INT,
    city VARCHAR(50)
);

-- Sample Data
INSERT INTO employees VALUES
(1, 'Alice', 'Developer', 45000, 'Hyderabad'),
(2, 'Bob', 'Tester', 38000, 'Bangalore'),
(3, 'Charlie', 'Manager', 60000, 'Hyderabad'),
(4, 'Diana', 'PM', 55000, 'Bangalore'),
(5, 'Eve', 'Developer', 40000, 'Bangalore'),
(6, 'Frank', 'Tester', 42000, 'Hyderabad'),
(7, 'Grace', 'Manager', 70000, 'Bangalore');


-- 1. Employees in Developer OR Tester (UNION)


SELECT * FROM employees WHERE department = 'Developer'
UNION
SELECT * FROM employees WHERE department = 'Tester';


-- 2. Employees in Hyderabad OR Bangalore (UNION)


SELECT * FROM employees WHERE city = 'Hyderabad'
UNION
SELECT * FROM employees WHERE city = 'Bangalore';


-- 3. Employees from Manager AND PM departments including duplicates (UNION ALL)


SELECT * FROM employees WHERE department = 'Manager'
UNION ALL
SELECT * FROM employees WHERE department = 'PM';


-- 4. Employees in Hyderabad AND Tester (INTERSECT)


SELECT * FROM employees WHERE city = 'Hyderabad'
INTERSECT
SELECT * FROM employees WHERE department = 'Tester';


-- 5. Employees in Bangalore AND earn more than 40,000 (INTERSECT)


SELECT * FROM employees WHERE city = 'Bangalore'
INTERSECT
SELECT * FROM employees WHERE salary > 40000;


-- 6. Employees in Hyderabad but NOT in Tester department (EXCEPT)

SELECT * FROM employees WHERE city = 'Hyderabad'
EXCEPT
SELECT * FROM employees WHERE department = 'Tester';


-- 7. Employees who earn more than 40,000 but are NOT in Bangalore (EXCEPT)

SELECT * FROM employees WHERE salary > 40000
EXCEPT
SELECT * FROM employees WHERE city = 'Bangalore';


-- 8. Employees in Developer OR Tester AND located in Hyderabad (INTERSECT + UNION)


(SELECT * FROM employees WHERE department = 'Developer'
UNION
SELECT * FROM employees WHERE department = 'Tester')
INTERSECT
SELECT * FROM employees WHERE city = 'Hyderabad';


-- 9. Employees in Hyderabad OR earn > 50,000 BUT exclude Managers (EXCEPT + UNION)

(SELECT * FROM employees WHERE city = 'Hyderabad'
UNION
SELECT * FROM employees WHERE salary > 50000)
EXCEPT
SELECT * FROM employees WHERE department = 'Manager';


-- 10. Employees who are Developers OR Testers OR Managers (UNION)


SELECT * FROM employees WHERE department = 'Developer'
UNION
SELECT * FROM employees WHERE department = 'Tester'
UNION
SELECT * FROM employees WHERE department = 'Manager';
