## What is a relational database?

A relational database is a type of database that organizes data into rows and columns, which collectively form a table where the data points are related to each other.

Data is typically structured across multiple tables, which can be joined together via a primary key. These unique identifiers demonstrate the different relationships which exist between tables. Analysts use SQL queries to combine different data points and summarize business performance, allowing organizations to gain insights, optimize workflows, and identify new opportunities.

For example, imagine a company maintains a database table with customer information, which contains company data at the account level. There may also be a different table, which describes all the individual transactions that align to that account. Together, these tables can provide information about the different industries that purchase a specific software product.

The columns (or fields) for the customer table might be _Customer ID_, _Company Name_, _Company Address_, _Industry_ etc.; the columns for a transaction table might be _Transaction Date_, _Customer ID_, _Transaction Amount_, _Payment Method_, etc. The tables can be joined together with the common _Customer ID_ field. You can, therefore, query the table to produce valuable reports, such as a sales reports by industry or company, which can inform messaging to prospective clients.

Relational databases are also typically associated with transactional databases, which execute commands, or transactions, collectively. A popular example that is used to illustrate this is a bank transfer. A defined amount is withdrawn from one account, and then it is deposited within another. The total amount of money is withdrawn and deposited, and this transaction cannot occur in any kind of partial sense. Transactions have specific properties. Represented by the acronym, **ACID**, ACID properties are defined as:
- **Atomicity:** All changes to data are performed as if they are a single operation. That is, all the changes are performed, or none of them are.
- **Consistency:** Data remains in a consistent state from state to finish, reinforcing data integrity.
- **Isolation:** The intermediate state of a transaction is not visible to other transactions, and as a result, transactions that run concurrently appear to be serialized.
- **Durability:** After the successful completion of a transaction, changes to data persist and are not undone, even in the event of a system failure.

While a relational database organizes data based off a relational data model, a relational database management system ([[RDBMS]]) is a more specific reference to the underlying database software that enables users to maintain it.

Structured Query Language (SQL) is the standard programming language for interacting with relational database management systems, allowing database administrator to add, update, or delete rows of data easily. 

Originally known as SEQUEL, it was simplified to SQL due to a trademark issue. SQL queries also allows users to retrieve data from databases using only a few lines of code. Given this relationship, it’s easy to see why relational databases are also referred to as “SQL databases” at times.

## Some of The Most Important SQL Commands
- `SELECT` - extracts data from a database
- `UPDATE` - updates data in a database
- `DELETE` - deletes data from a database
- `INSERT INTO` - inserts new data into a database
- `CREATE DATABASE` - creates a new database
- `ALTER DATABASE` - modifies a database
- `CREATE TABLE` - creates a new table
- `ALTER TABLE` - modifies a table
- `DROP TABLE` - deletes a table

Here are some more:  [[SQL Commands Cheat Sheet]]

Here's a comprehensive list of common **SQL [[Data Types]]**, organized by category. These types are supported across most databases (like PostgreSQL, MySQL, SQLite, and SQL Server), with some variation.
