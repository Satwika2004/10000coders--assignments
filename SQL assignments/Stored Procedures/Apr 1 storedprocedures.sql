


-- CREATE TABLE Employees (
--     emp_id INT AUTO_INCREMENT PRIMARY KEY,
--     emp_name VARCHAR(50),
--     department VARCHAR(50),
--     salary DECIMAL(10,2)
-- );

-- 1. Display all records from Employees
DELIMITER $$
CREATE PROCEDURE GetAllEmployees()
BEGIN
    SELECT * FROM Employees;
END$$
DELIMITER ;

-- 2. Get employee details by EmployeeID
DELIMITER $$
CREATE PROCEDURE GetEmployeeByID(IN empID INT)
BEGIN
    SELECT * FROM Employees WHERE emp_id = empID;
END$$
DELIMITER ;

-- 3. Insert a new employee
DELIMITER $$
CREATE PROCEDURE InsertEmployee(
    IN empName VARCHAR(50),
    IN empDept VARCHAR(50),
    IN empSalary DECIMAL(10,2)
)
BEGIN
    INSERT INTO Employees(emp_name, department, salary)
    VALUES (empName, empDept, empSalary);
END$$
DELIMITER ;

-- 4. Update salary of an employee using EmployeeID
DELIMITER $$
CREATE PROCEDURE UpdateSalary(
    IN empID INT,
    IN newSalary DECIMAL(10,2)
)
BEGIN
    UPDATE Employees
    SET salary = newSalary
    WHERE emp_id = empID;
END$$
DELIMITER ;

-- 5. Delete an employee record using EmployeeID
DELIMITER $$
CREATE PROCEDURE DeleteEmployee(IN empID INT)
BEGIN
    DELETE FROM Employees WHERE emp_id = empID;
END$$
DELIMITER ;

-- 6. Display employees with salary greater than input value
DELIMITER $$
CREATE PROCEDURE EmployeesWithSalaryAbove(IN minSalary DECIMAL(10,2))
BEGIN
    SELECT * FROM Employees
    WHERE salary > minSalary;
END$$
DELIMITER ;

-- 7. Calculate average salary of employees
DELIMITER $$
CREATE PROCEDURE AverageSalary()
BEGIN
    SELECT AVG(salary) AS AverageSalary FROM Employees;
END$$
DELIMITER ;

-- 8. Total number of employees in a department
DELIMITER $$
CREATE PROCEDURE CountEmployeesInDept(IN deptName VARCHAR(50))
BEGIN
    SELECT COUNT(*) AS TotalEmployees
    FROM Employees
    WHERE department = deptName;
END$$
DELIMITER ;

-- 9. Find the maximum salary in Employees table
DELIMITER $$
CREATE PROCEDURE MaxSalary()
BEGIN
    SELECT MAX(salary) AS MaximumSalary FROM Employees;
END$$
DELIMITER ;

-- 10. Give 10% bonus to employees whose salary is below 50,000
DELIMITER $$
CREATE PROCEDURE GiveBonus()
BEGIN
    UPDATE Employees
    SET salary = salary * 1.10
    WHERE salary < 50000;
END$$
DELIMITER ;
