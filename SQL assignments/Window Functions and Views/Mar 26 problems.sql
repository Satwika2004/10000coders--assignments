

-- 1. Create Student Table
CREATE TABLE IF NOT EXISTS student (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    Marks INT
);


-- 1. Display all students with a row number based on marks descending

SELECT *, ROW_NUMBER() OVER(ORDER BY Marks DESC) AS RowNum
FROM student;


-- 2. Top 3 students department-wise using ROW_NUMBER()
SELECT *
FROM (
    SELECT id, name, department, Marks,
           ROW_NUMBER() OVER(PARTITION BY department ORDER BY Marks DESC) AS RowNum
    FROM student
) AS sub
WHERE RowNum <= 3;


-- 3. Row numbers ordered by name ascending

SELECT *, ROW_NUMBER() OVER(ORDER BY name ASC) AS RowNum
FROM student;


-- 4. Row numbers by marks ascending, row number < 4

SELECT *
FROM (
    SELECT *, ROW_NUMBER() OVER(ORDER BY Marks ASC) AS RowNum
    FROM student
) AS sub
WHERE RowNum < 4;

-- 6. Rank based on marks (highest first)

SELECT *, RANK() OVER(ORDER BY Marks DESC) AS RankNum
FROM student;


-- 7. Rank department-wise

SELECT *, RANK() OVER(PARTITION BY department ORDER BY Marks DESC) AS DeptRank
FROM student;

-- 8. Students with Rank 1 in each department

SELECT *
FROM (
    SELECT *, RANK() OVER(PARTITION BY department ORDER BY Marks DESC) AS DeptRank
    FROM student
) AS sub
WHERE DeptRank = 1;


-- 9. Rank ascending

SELECT *, RANK() OVER(ORDER BY Marks ASC) AS RankAsc
FROM student;


-- 10. Students whose rank <= 2

SELECT *
FROM (
    SELECT *, RANK() OVER(ORDER BY Marks DESC) AS RankNum
    FROM student
) AS sub
WHERE RankNum <= 2;


-- 11. Dense rank highest first

SELECT *, DENSE_RANK() OVER(ORDER BY Marks DESC) AS DenseRank
FROM student;


-- 12. Department-wise dense rank

SELECT *, DENSE_RANK() OVER(PARTITION BY department ORDER BY Marks DESC) AS DeptDenseRank
FROM student;

-
SELECT *
FROM (
    SELECT *, DENSE_RANK() OVER(PARTITION BY department ORDER BY Marks DESC) AS DeptDenseRank
    FROM student
) AS sub
WHERE DeptDenseRank = 2;


-- 14. Dense rank ascending

SELECT *, DENSE_RANK() OVER(ORDER BY Marks ASC) AS DenseRankAsc
FROM student;


-- 15. Top 2 distinct highest marks using DENSE_RANK

SELECT *
FROM (
    SELECT *, DENSE_RANK() OVER(ORDER BY Marks DESC) AS DenseRank
    FROM student
) AS sub
WHERE DenseRank <= 2;


-- 16. View: student name, marks, row number highest first

CREATE OR REPLACE VIEW view_student_rownum AS
SELECT id, name, Marks,
       ROW_NUMBER() OVER(ORDER BY Marks DESC) AS RowNum
FROM student;


-- 17. View: student name and rank based on marks

CREATE OR REPLACE VIEW view_student_rank AS
SELECT id, name, Marks,
       RANK() OVER(ORDER BY Marks DESC) AS RankNum
FROM student;

-- 18. View: department-wise dense rank

CREATE OR REPLACE VIEW view_dept_dense_rank AS
SELECT id, name, department, Marks,
       DENSE_RANK() OVER(PARTITION BY department ORDER BY Marks DESC) AS DeptDenseRank
FROM student;


-- 19. View: top 3 students using ROW_NUMBER()

CREATE OR REPLACE VIEW view_top3_students AS
SELECT *
FROM (
    SELECT *, ROW_NUMBER() OVER( ORDER BY Marks DESC) AS RowNum
    FROM student
) AS sub
WHERE RowNum <= 3;


-- 20. View: students with rank 1

CREATE OR REPLACE VIEW view_rank1_students AS
SELECT *
FROM (
    SELECT *, RANK() OVER(ORDER BY Marks DESC) AS DeptRank
    FROM student
) AS sub
WHERE DeptRank = 1;
