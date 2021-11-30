-- SELECT o.EmployeeID, COUNT(*) AS 'Employee Order Count' 
-- FROM Orders o
-- -- using an inner join and subquery, write a query to shoe the orderID, custID,EmpID, EmpOrderCount, OrderDate
-- INNER JOIN (SELECT EmployeeID, COUNT(*) AS 'Employee Order Count', CustomerID, OrderID, OrderDate 
--     FROM Orders o) sq ON o.OrderID = sq.OrderID
-- GROUP BY o.CustomerID, sq.CustomerID;
--subquery
--SELECT CustomerID, OrderID, OrderDate FROM o 
-- Answer
-- SELECT o.OrderID,
--     o.CustomerID,
--     o.EmployeeID,
--     c.EOCount AS 'Employee Order Count',
--     o.OrderDate
-- FROM Orders o
-- INNER JOIN (
--     SELECT EmployeeID, COUNT(*) AS 'EOCount'
--     FROM Orders
--     GROUP BY EmployeeID
--     ) c ON o.EmployeeID = c.EmployeeID;

-- Partition by, eg
-- SELECT OrderID, EmployeeID, OrderDate,
--     COUNT(*) OVER (PARTITION BY EmployeeID) AS 'Employee Order Count'
-- FROM Orders
-- ORDER BY EmployeeID
-- SELECT ProductID, ProductName, c.CategoryName,
--     COUNT(*) OVER (PARTITION BY c.CategoryID) -1 AS 'No. of Other Products in Same Category'
-- FROM Products p
-- INNER JOIN Categories c ON p.CategoryID = c.CategoryID 
-- ORDER BY ProductID--c.CategoryName;
-- Look at recording

-- SELECT *, COUNT(*) OVER() AS 'Total Count'
-- FROM Products
-- SELECT ProductID, ProductName, c.CategoryName, 
--     COUNT(UnitsOnOrder) OVER (PARTITION BY c.CategoryID) AS 'Total Units on Order for Category'
-- FROM Products p
-- INNER JOIN Categories c ON p.CategoryID = c.CategoryID;

-- ORDER BY
-- SELECT ProductName,
--     UnitPrice,
--     DENSE_RANK() OVER (ORDER BY UnitPrice DESC) AS 'Row Number'
-- FROM Products

-- SELECT ProductName, UnitPrice, CategoryID,
--     ROW_NUMBER() OVER (PARTITION BY CategoryID ORDER BY UnitPrice DESC)
--         AS 'Row Number'
-- FROM Products
-- the row number resets after each category starts
-- SELECT ProductName, UnitPrice, CategoryID,
--     RANK() OVER (PARTITION BY CategoryID ORDER BY UnitPrice DESC)
--         AS 'Row Number'
-- FROM Products
-- -- Also resets but skips after ties
-- SELECT ProductName, UnitPrice, CategoryID,
--     DENSE_RANK() OVER (PARTITION BY CategoryID ORDER BY UnitPrice DESC)
--         AS 'Row Number'
-- FROM Products
-- -- resets but doesn't skip ties

-- -- Rank by OrderDate per Customer
-- SELECT OrderID, CustomerID, OrderDate,
--     RANK() OVER (PARTITION BY CustomerID ORDER BY OrderDate ASC)
--         AS 'OrderDate Rank per Customer'
-- FROM Orders
-- ORDER BY OrderID;

-- SELECT ProductName, UnitPrice,
--     LEAD(ProductName, 1, NULL) OVER (ORDER BY UnitPrice)
--         AS 'Next Product Price'
-- FROM Products;

-- -- Showing the Freight of the previous order (From the Orders table)
-- SELECT OrderID, OrderDate, Freight,
--     LAG(Freight, 1, NULL) OVER (ORDER BY OrderDate ASC)
--         AS 'Freight For Previous Order' 
-- FROM Orders;

-- SELECT ProductName, SupplierID,
--     FIRST_VALUE(UnitsOnOrder) OVER (PARTITION BY SupplierID ORDER BY UnitsOnOrder DESC)
--         AS 'Most Units on Order from Supplier'
-- FROM Products;

-- SELECT OrderID, CustomerID, EmployeeID, OrderDate,
--    DATEDIFF(DAY, FIRST_VALUE(OrderDate) OVER (PARTITION BY CustomerID ORDER BY OrderDate), OrderDate)
--     AS "No. of days since Customer's First Order"
-- FROM Orders 
-- ORDER BY OrderID;
-- -- Look at recording for the actual answer 

-- SELECT OrderID, EmployeeID,
--     LAST_VALUE(OrderID) OVER (PARTITION BY EmployeeID ORDER BY OrderID
--     ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
--         AS 'Last Order for Employee'
-- FROM Orders

-- SELECT OrderID, OrderDate, Freight,
--     AVG(Freight) OVER (ORDER BY OrderDate
--     ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING)
--     AS '3pt Moving Avg'
-- FROM Orders
-- -- MM's code:
-- SELECT o.OrderID, o.OrderDate, [Total Price],
--     AVG([Total Price]) OVER (ORDER BY OrderDate
--     ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING)
--     AS '5pt Moving Avg of Total Price'
-- FROM Orders o
-- INNER JOIN [Order Details] od ON o.OrderID = od.OrderID
-- INNER JOIN (SELECT OrderID, SUM((UnitPrice * Quantity * (1 - Discount))) 
--                 AS 'Total Price'
--             FROM [Order Details] 
--             GROUP BY OrderID) sq
--     ON o.OrderID = sq.OrderID
-- GROUP BY o.OrderID, o.OrderDate, [Total Price]
-- ORDER BY o.OrderID;
-- -- still hard to follow so look at recording from 22/11/21
 