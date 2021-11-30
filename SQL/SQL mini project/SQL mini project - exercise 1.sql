-- Exercise 1: Northwind Queries

-- -- 1.1: Write a query that lists all Customers in either Paris or London. Include Customer ID, Company Name, and all the address fields
--  SELECT CustomerID, CompanyName, Address FROM Customers
--  WHERE City IN ('Paris', 'London');

-- --1.2: List all Products stored in bottles
-- SELECT * FROM Products
-- WHERE QuantityPerUnit LIKE '%bottle%';

-- -- 1.3: Repeat 1.2, but add in the Supplier Name and Country
-- SELECT ProductName, QuantityPerUnit, CompanyName, Country FROM Products p
-- INNER JOIN Suppliers s ON p.SupplierID = s.SupplierID 
-- WHERE QuantityPerUnit LIKE '%bottle%'


-- -- 1.4: Write a SQL statement that shows how many products there are in each category 
-- --      Incl CategoryName in the result set and list the highest number first 
-- SELECT c.CategoryName "Category Name", COUNT(*) AS "No. of Products" FROM Categories c
-- INNER JOIN Products p ON c.CategoryID = p.CategoryID
-- GROUP BY c.CategoryName
-- ORDER BY COUNT(*) DESC
-- -- Need to practice this to understand the process!

-- -- 1.5: List all UK employees using CONCATENATION to join their title of courtesy, FirstName and LastName together. 
-- --      Also, inlcude their city of residence
-- SELECT TitleOfCourtesy + ' ' + FirstName + ' ' + LastName AS "Employee", City
-- FROM Employees 
-- WHERE Country = 'UK';


-- -- 1.6: List Sales Totals for all Sales Regions (via the Territories table, using 4 JOINS) 
-- --      with Sales Total greater than 1,000,000. Use rounding or FORMAT to present the numbers.
-- SELECT * FROM Territories t
-- INNER JOIN Region r ON  t.RegionID = r.RegionID
-- -- JOIN t with EmployeeTerritories (et) on TerritoryID
-- INNER JOIN EmployeeTerritories et ON t.TerritoryID = et.TerritoryID

-- -- Sales totals: SUM, Need quantity from Order Details, * UnitPrice
-- SELECT Quantity * UnitPrice * (1-Discount) "Sales Total" FROM [Order Details] od
--WHERE (Quantity * UnitPrice) > 1000000.00;

-- JOIN on Region ID
-- SELECT * FROM [Order Details]


-- --1.7: Count how many Orders have a Freight amount greater than 100.00
-- --     and either USA or UK as Ship Country.
-- SELECT COUNT(*) AS "Orders that have a freight amount > 100.00" FROM Orders 
-- WHERE Freight > 100.00 AND ShipCountry IN ('USA', 'UK');
--  -- I initially overcomplicated by using the Group BY  clause and calling the ShipCountry col


-- --1.8: Write an SQL statement to identify the Order Number of the Order with the highest amount of discount applied to that order.
-- -- Highest amount -> MAX
-- -- Need OrderID from Order Details table as discount is mentioned 
-- -- Highest amount of discount applied to order
-- SELECT OrderID AS "Order Number", Quantity, UnitPrice, MAX(Discount) AS "Discount" FROM [Order Details]
-- GROUP BY OrderID, Quantity, UnitPrice
-- ORDER BY Discount DESC
-- -- Looking at the answer, I need to FORMAT
