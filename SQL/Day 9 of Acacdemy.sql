-- --Ex 1:
-- SELECT FirstName + ' ' + LastName AS 'Employee Name'
-- FROM Employees;

-- --Ex 2: SELECT THE SIX COUNTRIES...
-- SELECT DISTINCT Country
-- FROM Customers
-- WHERE Region IS NOT NULL;

-- --Ex 3: add a new col to show the net total
-- SET QUOTED_IDENTIFIER OFF;
-- SELECT UnitPrice, Quantity, Discount,
-- UnitPrice * Quantity AS "Gross Total",
-- UnitPrice*Quantity*(1-Discount) AS "Net Total"
-- FROM [Order Details]
-- --Eg 4:
-- ORDER BY "Net Total" DESC;

-- --Ex 5: use CHARINDEX
-- SET QUOTED_IDENTIFIER OFF;
-- SELECT ProductName 
-- FROM Products
-- WHERE CHARINDEX("'",ProductName) >= 1;

-- --Ex 6: Output a list of employees to incl their name amd age
-- SET QUOTED_IDENTIFIER OFF;
-- SELECT  FirstName + " " + LastName AS "Employee",
--     DATEDIFF(d, BirthDate, GETDATE())/365.25  AS "Age", 
-- --Ex 7: add a column to use a case statement -> this will be called "Retirement Status"
--     CASE
--         WHEN DATEDIFF(d, BirthDate, GETDATE())/365.25 > 65.0 THEN "Retired"
--         WHEN DATEDIFF(d, BirthDate, GETDATE())/365.25 > 60.0 THEN "Retirement due"
--         ELSE "More than 5 years to go"
--     END AS "Retirement Status"
-- FROM Employees
-- ORDER BY 'Age' DESC;

-- --Eg 8: GROUP BY AND AGGREGATE FUNCTIONS
-- SELECT SUM(UnitsOnOrder) AS 'Total',
--     AVG(UnitsOnOrder) AS 'Avg',
--     MIN(UnitsOnOrder) AS 'Min',
--     MAX(UnitsOnOrder) AS 'Max',
--     SupplierID
-- FROM Products
-- GROUP BY SupplierID;
-- --Ex 8: What's the highest Avg Reorder Level?
-- SELECT CategoryID,
--     AVG(ReorderLevel) AS 'Avg'
-- FROM Products
-- GROUP BY CategoryID
-- ORDER BY 'Avg' DESC;
-- -- The highest Average Reorder Level is 22, which came from Category 5.

-- --Eg 9: Filter -> use HAVING
-- SELECT CategoryID,
--     AVG(ReorderLevel) AS 'Avg'
-- FROM Products
-- GROUP BY CategoryID
-- HAVING AVG(ReorderLevel) > 11
-- ORDER BY 'Avg' DESC;

-- --Ex 10.1: JOINS!!! Need tables Orders and Customers
-- SELECT * 
-- FROM Orders o
-- INNER JOIN Customers c
-- ON o.CustomerID = c.CustomerID
-- WHERE Country = 'Brazil'; 

-- --Ex 10.2: Products, (GROUP BY) Supplier Name
-- SELECT p.SupplierID, CompanyName, 
--     AVG(UnitsOnOrder) AS 'Avg Units on Order'
-- FROM Products p
-- INNER JOIN Suppliers s ON p.SupplierID = s.SupplierID
-- GROUP BY p.SupplierID, CompanyName;

--What if we want ALL data from the 1st table regardless of matches in the JOINED table?
--LEFT (OUTER) JOIN
-- 2ND TABLE? RIGHT JOIN...but not needed -> just swap the names and use LEFT JOIN

-- List Orders, JOIN to Customers and Employess tables
-- incl customer Name (compName) and Employee (1st and last name)
--SELECT OrderID, OrderDate,
--Freight,
--CompanyName, FirstName+' '+LastName AS "Employee Name"
--FROM Orders o
--INNER JOIN Employees e
--ON o.EmployeeID = e.EmployeeID
--INNER JOIN Customers c
--ON o.CustomerID = c.CustomerID
--GROUP BY OrderID;
--SELECT * FROM Orders;

-- --Subquery
-- SELECT CompanyName AS "Customer"
-- FROM Customers 
-- WHERE CustomerID NOT IN
--    (SELECT CustomerID FROM Orders);

-- What DJ would do:
--SELECT

--SELECT OrderID, ProductID, UnitPrice, Quantity, Discount,
 --   (SELECT MAX(UnitPrice) FROM [Order Details] od) AS "Max Price"
--FROM [Order Details]

-- inline view
--SELECT Quantity, sq1.ProductID, sq1[total amount] FROM [Order Details] od INNER JOIN (
  --  SELECT ProductID, SUM(UnitPrice) AS "total amount" FROM [Order Details] GROUP BY Products
--) sq1 ON sq1.ProductID = od.ProductID 

--Ex:
--SELECT COUNT(*) FROM [Order Details] 
--WHERE ProductID IN (SELECT ProductID FROM Products
  --   WHERE Discontinued = 1)
--;
-- Same ex but putting subquery in Inner Join clause instead of Where
-- we want the orders of products that have been discontinued
-- SELECT COUNT(*)
-- FROM [Order Details] od
-- INNER JOIN (
--     SELECT ProductID FROM Products
--     WHERE Discontinued = 1
--     ) sq1 
-- ON od.ProductID = sq1.ProductID;

-- SELECT EmployeeID AS "Employee/Supplier"
-- FROM Employees
-- UNION ALL
-- SELECT SupplierID
-- FROM Suppliers;

