-- Jade's Northwind query question
--    Write a query to...

-- 1. Write a query to show the total order value for all shipping companies,
--    from highest to lowest.
-- total -> SUM or maybe it's COUNT...MUST FORMAT
-- highest to lowest -> DESC
-- SELECT * FROM Shippers
-- JOIN with Suppliers on CompanyName
-- SELECT * FROM Suppliers
-- SELECT * FROM [Order Details]
-- SELECT * FROM Orders
-- JOIN Orders with Order Details on OrderID
--show shipname



-- 2. Write a query to return the customer ID of who has spent 
--    the most money.
-- SELECT CustomerID FROM Customers c
-- INNER JOIN Orders o ON c.CustomerID = o.CustomerID 
-- SELECT * FROM Orders


-- 3. Use JOIN to display the following info in a table:
--    CustomerID, Address, (Customer) City, EmployeeID, 
--    (Employee) City, (Supplier) City
-- SELECT * FROM Customers
-- this incl City, address, CustomerID
-- SELECT CustomerID, c.Address, c.City, e.EmployeeID, e.City, s.City FROM Customers c
-- INNER JOIN Employees e ON c.City = e.City
-- INNER JOIN Suppliers s ON s.City = e.City

-- 4. Write a query to return employees from the UK with their full name,
--    respective territory description beginning with R and S,
--    Employee ID and Territory ID. Sorted by Territory then Name.


-- 5. Write a query to return which suppliers need to restock a product
--    (exclude any discontinued products). 
--    Incl the Supplier ID, name, and the product name.
-- -- exclude discontinued -> discontinued = 0
-- --SELECT * FROM Products p
-- -- need a join on supplier id-- But who need to restock?
-- -- restock -> UnitsInStock = 0
-- SELECT s.SupplierID, s.CompanyName, p.ProductName FROM Suppliers s
-- INNER JOIN Products p ON s.SupplierID = p.SupplierID
-- WHERE p.Discontinued = 0 AND p.UnitsInStock = 0
-- GROUP BY s.SupplierID, s.CompanyName, p.ProductName;

-- 6. Write a query to show how many orders each employee shipped
--    to Germany.
-- SELECT e.EmployeeID, COUNT(*) AS "No. of Orders",ShipCountry FROM Orders o
-- INNER JOIN Employees e ON o.EmployeeID = e.EmployeeID 
-- -- Now focussing on shipments to Germany
-- WHERE ShipCountry = 'Germany'
-- GROUP BY e.EmployeeID, ShipCountry
