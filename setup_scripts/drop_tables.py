#!/usr/bin/python3

import os 
import MySQLdb 


def drop_tables(db, cursor):

    fk_disable_sql = "SET FOREIGN_KEY_CHECKS=0;"
    cursor.execute(fk_disable_sql)
    drop_messages_sql = "DROP TABLE messages;"
    cursor.execute(drop_messages_sql)
    drop_users_sql = "DROP TABLE users;"
    cursor.execute(drop_users_sql)
    drop_jobs_sql = "DROP TABLE jobs;"
    cursor.execute(drop_jobs_sql)
    fk_enable_sql = "SET FOREIGN_KEY_CHECKS=1;"
    cursor.execute(fk_enable_sql)
    #db.commit()

    return 



def main():

    # connect to the database
    db = MySQLdb.connect(host=os.environ["mysql_ip"], user=os.environ["mysql_user"], passwd=os.environ["mysql_pw"], database="api_sql_redis")
    cursor = db.cursor()
    drop_tables(db, cursor)
    db.close()



if __name__ == "__main__":
    main()

