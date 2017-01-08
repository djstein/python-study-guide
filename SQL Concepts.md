## SQL Basics

### SQL Joins

INNER JOIN
Intersection of the two tables
```sql
SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.colum_name = table2.colum_name;
```

FULL OUTER JOIN
```sql
SELECT column_name(s)
FROM table1
FULL OUTER JOIN table2
ON table1.column_name=table2.column_name;
```

LEFT JOIN
Returns all rows from the left table, matching rows on the right table
```sql
SELECT column_name(s)
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;
```

RIGHT JOIN
Returns all rows from the right table with matching rows on the left table.
```sql
SELECT column_name(s)
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;
```
