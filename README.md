# api_sql_redis
a basic CRUD API that uses MySQL &amp; redis

This assumes that you have an existing MySQL database and Redis cache up and running, accessible via public IP addresses (since we're going to assume you're running your code locally).

## Use case

This API implements a simple system where there are three tables:

- users
- messages
- jobs

A user has a job (i.e. foreign key constraint), and a message is written by a user, so there is a foreign key constraint between the messages table and the users table.

Redis is used to cache GETs.

### Implementation details

To access the MySQL & redis endpoints, we're going to use environment variables, so you'll need to have those set up ahead of time, from the following vars:

- MySQL IP address: `mysql_ip`
- MySQL user name: `mysql_user`
- MySQL user pw: `mysql_pw`
- redis IP address: `redis_ip`

### Set up virtualenv
`python3 -m venv ../api_sql_redis`

`source bin/activate`

### Install libraries

`pip3 install -r requirements.txt`

I've included `requests` because I have been testing the difference in hitting the database vs redis, as indicated in `python/timer.py`.

### Populate the MySQL database

`python3 setup_scripts/populate_tables.py`

### Reset your MySQL database

`python3 setup_scripts/drop_tables.py`

`python3 setup_scripts/populate_tables.py`





