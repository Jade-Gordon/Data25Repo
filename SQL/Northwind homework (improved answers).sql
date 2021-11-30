SELECT ProductName, ProductID, UnitPrice FROM Products
WHERE UnitPrice < 5.00;
-- The names are: Guarana Fantastica (unit price = 4.50) and Geitost (unit price = 2.50) 

-- Which categories have a category name with initials beginning with B or S?
SELECT CategoryName FROM Categories
WHERE CategoryName LIKE 'B%' OR CategoryName LIKE 'S%';
-- Out of the 8 categories, there are 2 that have a category name with intials beginning with B or S: "Beverages" and "Seafood"

-- How many orders are there for EmployeeIDs 5 and 7 (the total for both)?
SELECT COUNT(OrderID) FROM Orders
WHERE EmployeeID = 5 OR EmployeeID = 7;
-- Or right EmployeeID IN (5,7)
-- In total, Employees 5 and 7 have a total of 114 orders. 