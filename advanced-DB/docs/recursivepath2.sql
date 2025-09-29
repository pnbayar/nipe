--CREATE DATABASE recursive_path_db;
-- 1. Create the edges table
-- CREATE TABLE edges (
--     src TEXT,
--     dst TEXT
-- );

-- -- 2. Insert sample data
-- INSERT INTO edges (src, dst) VALUES
-- ('a', 'b'),
-- ('b', 'c'),

-- ('c', 'd'),
-- ('b', 'e');

-- 3. Recursive CTE to find transitive closure
WITH RECURSIVE path(src, dst) AS (
    SELECT src, dst FROM edges            -- base case
    UNION
    SELECT p.src, e.dst
    FROM path p
    JOIN edges e ON p.dst = e.src         -- recursive step
)
--SELECT * FROM path
--ORDER BY src, dst;
-- 4. Query to find all reachable nodes from 'a'
SELECT dst FROM path WHERE src = 'b';