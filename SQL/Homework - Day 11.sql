--HOMEWORK
-- SELECT ProductName, UnitPrice, CategoryID,
--     CUME_DIST() OVER (PARTITION BY CategoryID ORDER BY UnitPrice DESC)
--         AS 'Row Number'
-- FROM Products
-- --

-- SELECT ProductName, UnitPrice, CategoryID,
--     PERCENT_RANK() OVER (PARTITION BY CategoryID ORDER BY UnitPrice DESC)
--         AS 'Row Number'
-- FROM Products
-- -- COMPUTES THE RANK AS A PROPORTION. IT'S LIKE AN INVERSE OF THE ABOVE

-- SELECT ProductName, UnitPrice, CategoryID,
--     PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY UnitPrice DESC)
--     OVER(PARTITION BY CategoryID)
--         AS 'Row Number'
-- FROM Products
-- -- DO CODE AGAIN -> saying that the func isn't allowed...

-- SELECT ProductName, UnitPrice, CategoryID,
--     PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY UnitPrice DESC)
--     OVER(PARTITION BY CategoryID)
--         AS 'Row Number'
-- FROM Products
-- -- same as above
-- don't worry about it