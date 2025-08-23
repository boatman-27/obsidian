## 1. Numeric Data Type

| Type                              | Description                          | Example           |
| --------------------------------- | ------------------------------------ | ----------------- |
| `INT` / `INTEGER`                 | Whole numbers                        | `42`, `-7`        |
| `SMALLINT`                        | Smaller integers (less storage)      | `120`, `-32768`   |
| `BIGINT`                          | Very large integers                  | `9223372036854775807` |
| `DECIMAL(p, s)` / `NUMERIC(p, s)`| Fixed precision (e.g. money)         | `DECIMAL(10,2)` → `12345.67` |
| `FLOAT`                           | Approximate numeric (floating-point) | `3.14`, `2.71e-5` |
| `REAL`                            | Single precision float               | `1.23`, `-0.004`  |
| `DOUBLE PRECISION`                | Double precision float               | `3.1415926535`    |
| `SERIAL` (Postgres)               | Auto-incrementing integer            | `1`, `2`, `3`, ...|

## 2. Date & Time Types

| Type          | Description                        | Example                        |
| ------------- | ---------------------------------- | ------------------------------ |
| `DATE`        | Calendar date (YYYY-MM-DD)         | `2025-07-20`                   |
| `TIME`        | Time of day (HH:MM:SS)             | `14:35:00`                     |
| `TIMESTAMP`   | Date + time (YYYY-MM-DD HH:MM:SS)  | `2025-07-20 14:35:00`         |
| `TIMESTAMPTZ` | Timestamp with timezone (Postgres) | `2025-07-20 14:35:00+04`      |
| `INTERVAL`    | A time span (e.g. '1 day')         | `INTERVAL '2 days 3 hours'`   |

## 3. String/Text Types

| Type         | Description                       | Example                    |
| ------------ | --------------------------------- | -------------------------- |
| `CHAR(n)`    | Fixed-length string (padded)      | `'HELLO     '` (CHAR(10))  |
| `VARCHAR(n)` | Variable-length string            | `'hello'`, `'world123'`    |
| `TEXT`       | Unbounded string (Postgres/MySQL) | `'This is a long message'` |
| `UUID`       | Universally unique identifier     | `'550e8400-e29b-41d4-a716-446655440000'` |

## 4. Boolean & Logical Types

| Type               | Description   | Example   |
| ------------------ | ------------- | --------- |
| `BOOLEAN` / `BOOL` | True or false | `TRUE`, `FALSE`, `NULL` |

## 5. Binary & Misc

| Type       | Description                        | Example                                     |
| ---------- | ---------------------------------- | ------------------------------------------- |
| `BYTEA`    | Binary data (Postgres)             | `E'\\xDEADBEEF'`                            |
| `BLOB`     | Binary Large Object (MySQL/SQLite) | Image or PDF binary data                    |
| `JSON`     | JSON data (Postgres, MySQL 5.7+)   | `'{"name": "Alice", "age": 30}'`            |
| `JSONB`    | Binary JSON (Postgres only)        | `'{"active": true}'::jsonb`                 |
| `ENUM`     | Custom list of allowed values      | `'small'`, `'medium'`, `'large'`            |
| `ARRAY`    | Array of values (Postgres only)    | `ARRAY[1, 2, 3]` or `'{apple,banana}'`      |
| `XML`      | XML data                           | `'<note><to>Bob</to><from>Alice</from></note>'` |
| `GEOMETRY` | Spatial data (PostGIS, MySQL)      | `POINT(30 10)`, `LINESTRING(0 0, 1 1, 2 2)`  |

## 6. Special Purpose (Mostly PostgreSQL)

| Type                  | Description                                | Example                          |
| --------------------- | ------------------------------------------ | -------------------------------- |
| `CIDR`, `INET`        | IP address types                           | `'192.168.1.0/24'`, `'10.0.0.1'` |
| `MACADDR`             | MAC address                                | `'08:00:2b:01:02:03'`            |
| `TSVECTOR`, `TSQUERY` | Full-text search types                     | `'fat:2,4 cat:3'`, `'fat & cat'` |
| `MONEY`               | Currency with formatting (not recommended) | `'$1,000.00'`, `'€99.95'`        |
## Notes

- Use `VARCHAR` if you want to limit string length, or `TEXT` for flexibility.
- Use `NUMERIC` or `DECIMAL` instead of `FLOAT` when you need **precise** decimal values (like currency).
- PostgreSQL is the most flexible with JSON, arrays, and custom types.