## Data Definition Language (DDL)

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);

DROP TABLE table_name;

ALTER TABLE table_name
ADD column_name datatype;

ALTER TABLE table_name
DROP COLUMN column_name;
```

---

## Data Manipulation Language (DML)

```sql
INSERT INTO table_name (col1, col2)
VALUES (val1, val2);

UPDATE table_name
SET column1 = value1
WHERE condition;

DELETE FROM table_name
WHERE condition;
```

---

## Data Query Language (DQL)

```sql
SELECT column1, column2
FROM table_name
WHERE condition
ORDER BY column ASC|DESC
LIMIT number OFFSET number;
```

---

## Joins

### INNER JOIN

Returns rows with matching values in both tables.

```sql
SELECT *
FROM A
INNER JOIN B ON A.id = B.a_id;
```

### LEFT JOIN

Returns all rows from the left table, matched rows from the right.

```sql
SELECT *
FROM A
LEFT JOIN B ON A.id = B.a_id;
```

### RIGHT JOIN

Returns all rows from the right table, matched rows from the left.

```sql
SELECT *
FROM A
RIGHT JOIN B ON A.id = B.a_id;
```

### FULL OUTER JOIN

Returns all rows when there is a match in one of the tables.

```sql
SELECT *
FROM A
FULL OUTER JOIN B ON A.id = B.a_id;
```

---

## GROUPING & AGGREGATION

```sql
SELECT column, COUNT(*), SUM(column), AVG(column), MIN(column), MAX(column)
FROM table_name
GROUP BY column;

-- Filtering grouped rows:
SELECT column, COUNT(*)
FROM table_name
GROUP BY column
HAVING COUNT(*) > 1;
```

---

## Filtering with WHERE and LIKE

```sql
SELECT *
FROM table_name
WHERE column = 'value';

-- Using LIKE:
SELECT *
FROM table_name
WHERE column LIKE 'A%';    -- starts with A

SELECT *
FROM table_name
WHERE column LIKE '%A';    -- ends with A

SELECT *
FROM table_name
WHERE column LIKE '%A%';   -- contains A

-- Case insensitive (Postgres):
WHERE column ILIKE '%abc%';
```

---

## Subqueries

```sql
SELECT name
FROM users
WHERE id IN (
    SELECT user_id
    FROM orders
    WHERE total > 100
);
```

---

## Constraints & Keys

```sql
PRIMARY KEY (column)
FOREIGN KEY (col) REFERENCES other_table(id)
UNIQUE (column)
NOT NULL
DEFAULT value
CHECK (condition)
```

---

## Other Useful Commands

```sql
-- Rename column:
ALTER TABLE table_name RENAME COLUMN old_name TO new_name;

-- Rename table:
ALTER TABLE old_name RENAME TO new_name;

-- Create index:
CREATE INDEX idx_name ON table_name (column);

-- Drop index:
DROP INDEX idx_name;
```

---

## 📝 Notes

- SQL is not case-sensitive, but common practice is to write keywords in uppercase.
- Always back up your data before running destructive commands like DELETE or DROP.
- Use `LIMIT` during testing to avoid returning huge result sets.
