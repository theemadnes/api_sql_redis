#!/usr/bin/python3

import os 
import MySQLdb 


def create_db(db, cursor):

    sql = "CREATE DATABASE IF NOT EXISTS api_sql_redis"
    cursor.execute(sql)
    ###db.commit()

def create_tables(db, cursor):

    sql_jobs = ("CREATE TABLE IF NOT EXISTS jobs (j_id INT AUTO_INCREMENT PRIMARY KEY, "
                "name VARCHAR(255)) ENGINE=InnoDB;"
                )
    cursor.execute(sql_jobs)
    ##db.commit()

    sql_users = ("CREATE TABLE IF NOT EXISTS users (u_id INT AUTO_INCREMENT PRIMARY KEY, "
                "name VARCHAR(255), address VARCHAR(255), j_id INT NOT NULL, "
                "FOREIGN KEY fk_job(j_id) REFERENCES jobs(j_id) ON UPDATE CASCADE "
                "ON DELETE RESTRICT) ENGINE=InnoDB;"               
                )
    cursor.execute(sql_users)
    ##db.commit()
    
    sql_messages = ("CREATE TABLE IF NOT EXISTS messages (m_id INT AUTO_INCREMENT PRIMARY KEY, "
                "body VARCHAR(255), timestamp TIMESTAMP, u_id INT NOT NULL, "
                "FOREIGN KEY fk_user(u_id) REFERENCES users(u_id) ON UPDATE CASCADE "
                "ON DELETE CASCADE) ENGINE=InnoDB;"               
                )
    cursor.execute(sql_messages)
    ##db.commit()

def populate_tables(db, cursor):

    sql_jobs = ("INSERT INTO jobs(name) "
                "VALUES ('engineer'),('accountant'),('manager'),('hr')"
                )

    

    cursor.execute(sql_jobs)
    #db.commit()

    sql_users = ("INSERT INTO users(name,address,j_id) "
                "VALUES ('Bob T','123 Fake St',1),"
                "('Jamie Z','456 Fake St',1),"
                "('Erin L','1234 North Ave',2),"
                "('Luke B','500 New Cr',2),"
                "('Chris I','311 S Myrtle',2),"
                "('Alex M','100 Happy Way',4),"
                "('Jamie Q','999 Maple Dr',3)"
                )

    cursor.execute(sql_users)
    #db.commit()

    sql_messages = ("INSERT INTO messages(body,timestamp,u_id) "
                "VALUES ('0_0','2018-01-01 09:00:01',1),"
                "('l33t','2008-05-01 00:00:01',1),"
                "('this is interesting','2004-01-01 00:54:01',2),"
                "('Whatz up','2015-02-01 00:00:01',2),"
                "('Hello world?','2019-01-01 03:00:01',2),"
                "('abcdef','2018-12-31 00:01:01',3),"
                "('testing 123','2018-12-21 00:02:01',4),"
                "('Oh HIIIII','2018-12-15 00:03:01',4),"
                "('It is getting late','2018-12-14 00:04:01',4),"
                "('Whatz on TV tonight?','2018-12-13 00:05:01',4),"
                "('Hey u up?','2018-12-12 00:06:01',5),"
                "('go cubs','2018-12-11 00:07:01',6),"
                "('go bulls!!!!','2018-12-10 00:08:01',6),"
                "('Good morning!','2018-12-09 02:09:01',3),"
                "('testing testing','2018-12-20 00:10:01',4),"
                "('on my way','2018-12-21 05:00:01',4),"
                "('blah blah blah','2018-12-11 06:00:01',4),"
                "('check check','2018-12-10 07:00:01',5),"
                "('Is this thing on?','2018-12-16 09:00:01',6),"
                "('Wheeee','2017-05-15 12:00:01',6)"
                )

    cursor.execute(sql_messages)
    db.commit()

def main():

    # connect to the database

    db = MySQLdb.connect(host=os.environ["mysql_ip"], user=os.environ["mysql_user"], passwd=os.environ["mysql_pw"])
    cursor = db.cursor()
    create_db(db, cursor)
    db.close()

    # recreate db connection to talk to api_sql_redis
    db = MySQLdb.connect(host=os.environ["mysql_ip"], user=os.environ["mysql_user"], passwd=os.environ["mysql_pw"], database="api_sql_redis")
    cursor = db.cursor()
    create_tables(db, cursor)
    populate_tables(db, cursor)
    db.close()
    #print("hi")


if __name__ == "__main__":
    main()

