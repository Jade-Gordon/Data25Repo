--SELECT * FROM Customers
--WHERE City = 'London';

-- How many employees live in London?
SELECT COUNT(*) FROM Employees
WHERE City = 'London';
-- 4

-- Which employee is a doctor?
SELECT * FROM Employees
WHERE TitleOfCourtesy = 'Dr.';

-- How many Products are dicontinued?
SELECT COUNT(*) FROM Products
WHERE Discontinued = 1; 
-- 8

SET QUOTED_IDENTIFIER OFF;
SELECT * FROM Suppliers WHERE Address LIKE "29 King's Way";

SELECT CustomerID, City FROM Customers
WHERE Country = 'France';

SELECT ProductName, UnitPrice FROM Products
WHERE UnitsInStock > 0 OR UnitPrice > 29.99;

SELECT DISTINCT Country FROM Customers
WHERE ContactTitle = 'Owner';

SELECT * FROM Customers WHERE Region IN ('WA', 'SP');
