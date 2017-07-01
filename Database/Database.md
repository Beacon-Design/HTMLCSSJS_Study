# Database

## What is a database?

A program that stores and retrieves ( large amounts structured ) data



## Types of databases

Relational(SQL)

- PostgreSQL ( reddit, hipmunk) free
- MySQL ( Facebook, everybody ) free
- SQLite ( lightweight simple database ) free
- Orical

Google App Engine's Datastore

Amazon - Dynamo

NoSQL ( mongo, couch)



## SQL

Structured Query Language

( invented in the 1970s )

**Example :** 

```
SELECT * FROM links WHERE id = 5 ;
------------------------------------
SELECT : fetch data 	
* 	   : all columns			(Example: url, title)
links  : table
id = 5 : constraint which rows to return
```