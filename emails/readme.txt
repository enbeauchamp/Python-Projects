This program is written by Eric Beauchamp using Python 2.7.8 and SQLite 3.8.2 database.

Assignment
----------
Given a table 'mailing':

CREATE TABLE mailing (
	addr VARCHAR(255) NOT NULL
);

The mailing table will initially be empty.  New addresses will be added on a daily basis.  It is expected that the table will store at least 10,000,000 email addresses and 100,000 domains.

Write a perl script that updates another table which holds a daily count of email addresses by their domain name.

Use this table to report the top 50 domains by count sorted by percentage growth of the last 30 days compared to the total.

Note about the files provided:
------------------------------

1. To run this program, type in "./run.sh" into a terminal.
2. The main program is found in "main.py"
3. Input files emails1.csv, emails2.csv, and emails3.csv were used as mailing tables.
4. Output is written to "report.csv"
5. Schema of database created ("test.db") and used is found in "schema.txt"
6. Tables from test.db were dumped to csv files for easier viewing (dataTable.csv, reportTable.csv)

