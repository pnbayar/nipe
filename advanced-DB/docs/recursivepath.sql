WITH RECURSIVE path(src, dst) AS (
    -- Base case
    SELECT * FROM (VALUES
        ('a','b'),
        ('b','c'),
        ('c','d'),
        ('b','e')
    ) AS edges(src, dst)
    UNION
    -- Recursive step
    SELECT p.src, e.dst
    FROM path p
    JOIN (VALUES
        ('a','b'),
        ('b','c'),
        ('c','d'),
        ('b','e')
    ) AS e(src, dst)
    ON p.dst = e.src
)
SELECT * FROM path
ORDER BY src, dst;
