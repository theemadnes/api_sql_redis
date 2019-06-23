# api_sql_redis
a basic CRUD API that uses MySQL &amp; redis

This assumes that you have an existing MySQL database and Redis cache up and running, accessible via public IP addresses (since we're going to assume you're running your code locally).

To access the MySQL & redis endpoints, we're going to use environment variables, so you'll need to have those set up ahead of time, from the following vars:

MySQL IP address: `mysql_ip`
redis IP address: `redis_ip`


### Set up virtualenv
`python3 -m venv ../api_sql_redis`

`source bin/activate`

### Install libraries

`pip3 install -r requirements.txt`




