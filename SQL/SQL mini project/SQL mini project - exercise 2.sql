-- -- Exercise 2: Create Spartans Table
-- -- 2.1: Spartans Table – include details about all the Spartans on this course.
-- --      Separate Title, First Name and Last Name into separate columns, and include University attended, course taken and mark achieved.
-- --      Add any other columns you feel would be appropriate. 

-- -- DROP DATABASE jade_db;
-- -- CREATE DATABASE jade_db;
-- DROP TABLE Spartans;
-- CREATE TABLE Spartans 
-- (
--     EmployeeID INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
--     Title VARCHAR(20) NOT NULL,
--     FirstName VARCHAR(50) NOT NULL,
--     LastName VARCHAR (50) NOT NULL,
--     SpartaCourse VARCHAR (50) NOT NULL,
--     University VARCHAR (50),
--     UniCourse VARCHAR (50),
--     UniMark VARCHAR (30),
--     StartDate DATE,
--     Trainer VARCHAR (50)
-- );

-- -- 2.2: Write SQL statements to add the details of the Spartans in your course to the table you have created
-- INSERT INTO Spartans 
-- (Title, FirstName, LastName, SpartaCourse, University, UniCourse, UniMark, StartDate, Trainer)
-- VALUES (
--     'Miss', 'Jade', 'Gordon', 'DataEngineering', 'Portsmouth', 'Mathematics', 'Third', '2021-11-08', 'Danny'
-- );
INSERT INTO Spartans
(Title, FirstName, LastName, SpartaCourse, University, UniCourse, StartDate, Trainer)
VALUES 
    ('Miss', 'Sandra', 'Idehen', 'DataEngineering', 'Portsmouth', 'ComputerScience', '2021-11-08', 'Danny'),
    ('Mr', 'Ensty', 'Mathew', 'DataEngineering', 'Uxbridge', 'AerospaceEngineering', '2021-11-08', 'Danny'),
    ('Miss', 'Jeneika', 'Patel', 'DataEngineering', NULL, NULL, '2021-11-08', 'Danny'),
    ('Mr', 'Bartlomiej (Bart)', 'Apanasionok', 'DataEngineering', NULL, NULL, '2021-11-08', 'Danny')
;

SELECT * FROM Spartans;