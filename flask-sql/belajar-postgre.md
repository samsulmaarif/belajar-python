

```
(3.7.3) samsul@piccolo:~/Publik/python/flask-sql> bash run-postgres.sh 
14636e28b2150b45f3e6095034e564523b8c678596aa877e5f92c1f8a9fb5622
(3.7.3) samsul@piccolo:~/Publik/python/flask-sql> docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
14636e28b215        postgres:alpine     "docker-entrypoint.s…"   4 seconds ago       Up 2 seconds        0.0.0.0:5432->5432/tcp   postgres-db
(3.7.3) samsul@piccolo:~/Publik/python/flask-sql> docker exec -it postgres-db sh
/app # pwd
/app
/app # ls
create.sql       run-postgres.sh
/app # su - postgres
  \password [USERNAME]   securely change the password for a user

Operating System
  \cd [DIR]              change the current working directory
  \setenv NAME [VALUE]   set or unset environment variable
  \timing [on|off]       toggle timing of commands (currently off)
  \! [COMMAND]           execute command in shell or start interactive shell

Variables
  \prompt [TEXT] NAME    prompt user to set internal variable
  \set [NAME [VALUE]]    set internal variable, or list all if no parameters
  \unset NAME            unset (delete) internal variable

Large Objects
  \lo_export LOBOID FILE
  \lo_import FILE [COMMENT]
  \lo_list
  \lo_unlink LOBOID      large object operations

~
postgres=# INSERT INTO flights 
postgres-#     (origin, destination, duration)
postgres-#     VALUES ('New York', 'London', 415);
INSERT 0 1
postgres=# INSERT INTO flights (origin, destination, duration) VALUES ('Cilacap', 'London', 2314);
INSERT 0 1
postgres=# INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'Jakarta', 666);
INSERT 0 1
postgres=# INSERT INTO flights (origin, destination, duration) VALUES ('Cilacap', 'London', 987);
General
  \copyright             show PostgreSQL usage and distribution terms
  \crosstabview [COLUMNS] execute query and display results in crosstab
  \errverbose            show most recent error message at maximum verbosity
  \g [FILE] or ;         execute query (and send results to file or |pipe)
  \gdesc                 describe result of query, without executing it
  \gexec                 execute query, then execute each value in its result
  \gset [PREFIX]         execute query and store results in psql variables
  \gx [FILE]             as \g, but forces expanded output mode
  \q                     quit psql
  \watch [SEC]           execute query every SEC seconds

Help
  \? [commands]          show help on backslash commands
  \? options             show help on psql command-line options
  \? variables           show help on special variables
  \h [NAME]              help on syntax of SQL commands, * for all commands

Query Buffer
  \e [FILE] [LINE]       edit the query buffer (or file) with external editor
postgres=# SELECT * FROM flights
postgres-# ;
 id |  origin  | destination | duration 
----+----------+-------------+----------
  1 | New York | London      |      415
  2 | Cilacap  | London      |     2314
  3 | New York | Jakarta     |      666
  4 | Cilacap  | London      |      987
  5 | Malang   | Jakarta     |      415
  6 | New York | Jakarta     |      231
  7 | New York | London      |      415
  8 | Cilacap  | Denpasar    |      415
  9 | Malang   | London      |      111
(9 rows)

postgres=# SELECT AVG(dutation) FROM flights;
ERROR:  column "dutation" does not exist
LINE 1: SELECT AVG(dutation) FROM flights;
                   ^
HINT:  Perhaps you meant to reference the column "flights.duration".
postgres=# SELECT AVG(duration) FROM flights;
         avg          
----------------------
 663.2222222222222222
(1 row)

postgres=# SELECT AVG(duration) FROM flights WHERE origin = 'Cilacap';
          avg          
-----------------------
 1238.6666666666666667
(1 row)

postgres=# SELECT COUNT(*) FROM flights;
 count 
-------
     9
(1 row)

postgres=# SELECT COUNT(*) FROM flights WHERE origin = 'Malang';
 count 
-------
     2
(1 row)

postgres=# SELECT MIN(duration) FROM flights;
 min 
-----
 111
(1 row)

postgres=# 
postgres=# select * from flights;
 id |  origin  | destination | duration 
----+----------+-------------+----------
  1 | New York | London      |      415
  2 | Cilacap  | London      |     2314
  3 | New York | Jakarta     |      666
  4 | Cilacap  | London      |      987
  5 | Malang   | Jakarta     |      415
  6 | New York | Jakarta     |      231
  7 | New York | London      |      415
  8 | Cilacap  | Denpasar    |      415
  9 | Malang   | London      |      111
(9 rows)

postgres=# UPDATE flights SET duration = 4512 WHERE destination = 'Denpasar' AND origin = 'New York';
UPDATE 0
postgres=# select * from flights;
 id |  origin  | destination | duration 
----+----------+-------------+----------
  1 | New York | London      |      415
  2 | Cilacap  | London      |     2314
  3 | New York | Jakarta     |      666
  4 | Cilacap  | London      |      987
  5 | Malang   | Jakarta     |      415
  6 | New York | Jakarta     |      231
  7 | New York | London      |      415
  8 | Cilacap  | Denpasar    |      415
  9 | Malang   | London      |      111
(9 rows)

postgres=# UPDATE flights SET duration = 4512 destination = 'Denpasar' WHERE id = 1;
ERROR:  syntax error at or near "destination"
LINE 1: UPDATE flights SET duration = 4512 destination = 'Denpasar' ...
                                           ^
postgres=# UPDATE flights SET duration = 4512 SET destination = 'Denpasar' WHERE id = 1;
ERROR:  syntax error at or near "SET"
LINE 1: UPDATE flights SET duration = 4512 SET destination = 'Denpas...
                                           ^
postgres=# UPDATE flights SET duration = 4512 WHERE id = 1;
UPDATE 1
postgres=# UPDATE flights SET destination = 'Denpasar' WHERE id = 1;
UPDATE 1
postgres=# select * from flights;
 id |  origin  | destination | duration 
----+----------+-------------+----------
  2 | Cilacap  | London      |     2314
  3 | New York | Jakarta     |      666
  4 | Cilacap  | London      |      987
  5 | Malang   | Jakarta     |      415
  6 | New York | Jakarta     |      231
  7 | New York | London      |      415
  8 | Cilacap  | Denpasar    |      415
  9 | Malang   | London      |      111
  1 | New York | Denpasar    |     4512
(9 rows)

postgres=# select * from flights ORDER BY duration ASC;
 id |  origin  | destination | duration 
----+----------+-------------+----------
  9 | Malang   | London      |      111
  6 | New York | Jakarta     |      231
  5 | Malang   | Jakarta     |      415
  7 | New York | London      |      415
  8 | Cilacap  | Denpasar    |      415
  3 | New York | Jakarta     |      666
  4 | Cilacap  | London      |      987
  2 | Cilacap  | London      |     2314
  1 | New York | Denpasar    |     4512
(9 rows)

postgres=# select * from flights ORDER BY duration ASC LIMIT 3;
 id |  origin  | destination | duration 
----+----------+-------------+----------
  9 | Malang   | London      |      111
  6 | New York | Jakarta     |      231
  5 | Malang   | Jakarta     |      415
(3 rows)

postgres=# SELECT origin, COUNT(*) FROM flights GROUP BY origin;
  origin  | count 
----------+-------
 Cilacap  |     3
 Malang   |     2
 New York |     4
(3 rows)

postgres=# 

```