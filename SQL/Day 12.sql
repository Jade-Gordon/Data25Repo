-- -- subquery in an inner join
-- SELECT ProductName 
-- FROM Products p
-- INNER JOIN (SELECT CategoryID FROM Products 
-- GROUP BY CategoryID
-- HAVING  AVG(UnitPrice) > 30) m
-- ON  p.CategoryID = m.CategoryID

-- --alternatively
-- SELECT ProductName 
-- FROM Products p
-- WHERE CategoryID IN (SELECT CategoryID FROM Products 
-- GROUP BY CategoryID
-- HAVING  AVG(UnitPrice) > 30) m
-- ON  p.CategoryID = m.CategoryID
-- -- look at recording

-- WITH MeanAbove 30 AS (
--     SELECT Category ID FROM Products
-- )

-- Temp tables
-- SELECT CategoryID INTO #MeanAbove30 
-- FROM Products
-- GROUP BY CategoryID HAVING AVG(UnitPrice) > 30;

-- SELECT ProductName FROM Products p
-- INNER JOIN...

--Pivot table 
-- SELECT CompanyName, ContactType
-- FROM Customers
-- UNPIVOT 
SELECT OrderID, Date, DateType
FROM Orders
UNPIVOT(Date FOR DateType IN (OrderDate, RequiredDate, ShippedDate)) 
