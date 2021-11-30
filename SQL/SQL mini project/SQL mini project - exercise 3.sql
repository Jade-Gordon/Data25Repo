-- Exercise 3: Northwind Data Analysis linked to Excel
--3.1: List all Employees from the Employees table and who they report to. (No Excel)
-- -- My answer:
-- SELECT FirstName + ' ' + LastName AS "Employee Name", ReportsTo FROM Employees;
-- -- Now I need to know the IDs of the reportees
-- -- Answer: Uses a SELF JOIN
-- SELECT e.FirstName + ' ' + e.LastName AS "Employee Name",
--             b.FirstName + ' ' + b.LastName AS "Reports To"
--      FROM Employees e
--      LEFT JOIN Employees b ON e.ReportsTo = b.EmployeeID
--     ORDER BY "Reports To", "Employee Name";

-- -- I don't understand

-- --3.2: List all Suppliers with total sales over $10,000 in the Order Details table. 
-- --     Include the Company Name from the Suppliers Table and present as a bar chart as below.
-- -- I need the Suppliers (s) and [Order Details] (od) tables.
-- -- These don't have a relationship between them...but the Products table has a SupplierID field
-- -- So, we can use the Products table can link the two 
-- -- SELECT * FROM Suppliers -- s can join p on SupplierID
-- SELECT s.CompanyName, SUM(od.UnitPrice * Quantity * (1-Discount)) AS "Supplier Total" FROM [Order Details] od
-- -- od can join p on ProductID
-- INNER JOIN Products p ON od.ProductID = p.ProductID
-- INNER JOIN Suppliers s ON p.SupplierID = s.SupplierID
-- GROUP BY s.CompanyName
-- HAVING SUM(od.UnitPrice * Quantity * (1-Discount))> 10000
-- ORDER BY SUM(od.UnitPrice * Quantity * (1-Discount));
-- -- I used the answer to guide me

--3.3: List the Top 10 Customers YTD for the latest year in the Orders file.
--     Based on total value of orders shipped. (No Excel)
-- Table(s) needed: Customers, Orders (shipping)

--3.4: Plot the Average Ship Time by month for all data in the Orders Table using a line chart as below.(Excel)
-- Shipping details are in the Orders table
-- SELECT AVG(DATEDIFF(d, MONTH(OrderDate), MONTH(ShippedDate))) AS " Avg Ship Time by Month" FROM Orders
-- -- -- ShipTime = ShippedDate - OrderDate
-- GROUP BY DATEDIFF(d, MONTH(OrderDate), MONTH(ShippedDate))
-- ORDER BY DATEDIFF(d, MONTH(OrderDate), MONTH(ShippedDate)) DESC
-- -- SELECT MONTH(OrderDate) AS "Order Month",  FROM Orders
-- I've no idea what i'm doing

-- ANS:
SELECT MONTH(OrderDate) Month, YEAR(OrderDate) Year, AVG(CAST(DATEDIFF(d, OrderDate, ShippedDate) AS DECIMAL (10, 2))) AS ShipTime
FROM Orders
WHERE ShippedDate IS NOT NULL
GROUP BY YEAR(OrderDate), MONTH(OrderDate)
ORDER BY Year, MONTH;