-- What are the names of the product IDs of the products with a unit price below 5.00?
SELECT ProductName, ProductID, UnitPrice FROM Products
WHERE UnitPrice < 5.00;
-- The names are: Guarana Fantastica (unit price = 4.50) and Geitost (unit price = 2.50) 

-- Which categories have a category name with initials beginning with B or S?
SELECT CategoryName FROM Categories;

-- How many orders are there for EmployeeIDs 5 and 7 (the total for both)?
SELECT COUNT(*) FROM Orders
WHERE EmployeeID = 5 OR EmployeeID = 7;
-- In total, Employees 5 and 7 have a total of 114 orders. 