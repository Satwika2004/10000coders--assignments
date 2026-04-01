-- 1. Students Table

CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    age INT NOT NULL CHECK (age > 17),
    gender ENUM('M','F')
);


-- 2. Courses Table

CREATE TABLE IF NOT EXISTS courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    fees DECIMAL(10,2) CHECK (fees > 0),
    duration INT DEFAULT 6 -- months
);


-- 3. Enrollments Table

CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enroll_date DATE NOT NULL,
    CONSTRAINT fk_enroll_student FOREIGN KEY (student_id) 
        REFERENCES students(student_id),
    CONSTRAINT fk_enroll_course FOREIGN KEY (course_id)
        REFERENCES courses(course_id),
    CONSTRAINT uc_student_course UNIQUE (student_id, course_id)
);


-- 4. Employees Table

CREATE TABLE IF NOT EXISTS departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    phone_number VARCHAR(15) UNIQUE,
    salary DECIMAL(10,2) CHECK (salary > 10000),
    department_id INT,
    city VARCHAR(50),
    CONSTRAINT fk_employee_dept FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
        ON DELETE CASCADE
);

-- 5. Orders Table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_amount DECIMAL(10,2) CHECK (order_amount > 500),
    order_date DATE DEFAULT CURRENT_DATE,
    CONSTRAINT fk_order_customer FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
        ON UPDATE CASCADE
);


-- 6. Authors and Books Tables

CREATE TABLE IF NOT EXISTS authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(50),
    email VARCHAR(100) UNIQUE
);

CREATE TABLE IF NOT EXISTS books (
    book_id INT PRIMARY KEY,
    book_name VARCHAR(100),
    author_id INT,
    price DECIMAL(10,2) CHECK (price > 100),
    CONSTRAINT fk_books_author FOREIGN KEY (author_id)
        REFERENCES authors(author_id)
);
