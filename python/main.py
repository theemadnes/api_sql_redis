#!/usr/bin/python3


#####################################
###
### API implementation of a user board 
### users - models individual users
### jobs - info on the jobs people have
### messages - posts they used on the website
###
#####################################

from flask import Flask, request, jsonify, abort
import MySQLdb
import os
import time
import datetime


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

@app.errorhandler(404)
def not_found(error=None):
    message= {
        'status': 404,
        'message': 'Not found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

# GET user(s)
@app.route("/v1/users", methods=["GET"])
def get_users():

    try:
        db = MySQLdb.connect(host=os.environ["mysql_ip"], user=os.environ["mysql_user"], passwd=os.environ["mysql_pw"], database="api_sql_redis")
        cursor = db.cursor()
        sql = "select * from users;"
        cursor.execute(sql)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        
        return resp

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        db.close()

@app.route("/v1/users/<int:u_id>", methods=["GET"])
def get_user(u_id):

    try:
        db = MySQLdb.connect(host=os.environ["mysql_ip"], user=os.environ["mysql_user"], passwd=os.environ["mysql_pw"], database="api_sql_redis")
        cursor = db.cursor()
        sql = "select * from users where u_id = {};".format(u_id)
        cursor.execute(sql)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        
        return resp

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        db.close()

    



# GET message(s)
@app.route("/v1/messages", methods=["GET"])
def get_messages():

    try:
        db = MySQLdb.connect(host=os.environ["mysql_ip"], user=os.environ["mysql_user"], passwd=os.environ["mysql_pw"], database="api_sql_redis")
        cursor = db.cursor()
        sql = "select * from messages;"
        cursor.execute(sql)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        
        return resp

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        db.close()

@app.route("/v1/messages/<int:m_id>", methods=["GET"])
def get_message(m_id):

    try:
        db = MySQLdb.connect(host=os.environ["mysql_ip"], user=os.environ["mysql_user"], passwd=os.environ["mysql_pw"], database="api_sql_redis")
        cursor = db.cursor()
        sql = "select * from messages where m_id = {};".format(m_id)
        cursor.execute(sql)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        
        return resp

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        db.close()

# GET job(s)
@app.route("/v1/jobs", methods=["GET"])
def get_jobs():

    try:
        db = MySQLdb.connect(host=os.environ["mysql_ip"], user=os.environ["mysql_user"], passwd=os.environ["mysql_pw"], database="api_sql_redis")
        cursor = db.cursor()
        sql = "select * from jobs;"
        cursor.execute(sql)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        
        return resp

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        db.close()

@app.route("/v1/jobs/<int:j_id>", methods=["GET"])
def get_job(j_id):

    try:
        db = MySQLdb.connect(host=os.environ["mysql_ip"], user=os.environ["mysql_user"], passwd=os.environ["mysql_pw"], database="api_sql_redis")
        cursor = db.cursor()
        sql = "select * from jobs where j_id = {};".format(j_id)
        cursor.execute(sql)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        
        return resp

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        db.close()

# POST user
@app.route("/v1/users", methods=["POST"])
def create_user():

    if not request.json:
        abort(400)

    try:
        db = MySQLdb.connect(host=os.environ["mysql_ip"], user=os.environ["mysql_user"], passwd=os.environ["mysql_pw"], database="api_sql_redis")
        cursor = db.cursor()
        sql = "INSERT INTO users(name,address,j_id) VALUES ('{}','{}',{});".format(request.json["name"],request.json["address"],request.json["j_id"])
        print(sql)
        cursor.execute(sql)
        db.commit()
        resp = jsonify("User '{}' added".format(request.json["name"]))
        resp.status_code = 200
        
        return resp

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        db.close()

@app.route("/v1/users/<int:u_id>", methods=["DELETE"])
def delete_user(u_id):

    try:
        db = MySQLdb.connect(host=os.environ["mysql_ip"], user=os.environ["mysql_user"], passwd=os.environ["mysql_pw"], database="api_sql_redis")
        cursor = db.cursor()
        sql = "delete from users where u_id = {};".format(u_id)
        cursor.execute(sql)
        resp = jsonify("User u_id {} deleted".format(u_id))
        resp.status_code = 200
        db.commit()
        
        return resp

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        db.close()


# POST job
@app.route("/v1/jobs", methods=["POST"])
def create_job():

    if not request.json:
        abort(400)

    try:
        db = MySQLdb.connect(host=os.environ["mysql_ip"], user=os.environ["mysql_user"], passwd=os.environ["mysql_pw"], database="api_sql_redis")
        cursor = db.cursor()
        sql = "INSERT INTO jobs(name) VALUES ('{}');".format(request.json["name"])
        print(sql)
        cursor.execute(sql)
        db.commit()
        resp = jsonify("Job '{}' added".format(request.json["name"]))
        resp.status_code = 200
        
        return resp

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        db.close()

@app.route("/v1/jobs/<int:j_id>", methods=["DELETE"])
def delete_job(j_id):

    try:
        db = MySQLdb.connect(host=os.environ["mysql_ip"], user=os.environ["mysql_user"], passwd=os.environ["mysql_pw"], database="api_sql_redis")
        cursor = db.cursor()
        sql = "delete from jobs where j_id = {};".format(j_id)
        cursor.execute(sql)
        resp = jsonify("Job j_id {} deleted".format(j_id))
        resp.status_code = 200
        db.commit()
        
        return resp

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        db.close()

# POST message
@app.route("/v1/messages", methods=["POST"])
def create_message():

    if not request.json:
        abort(400)

    try:
        db = MySQLdb.connect(host=os.environ["mysql_ip"], user=os.environ["mysql_user"], passwd=os.environ["mysql_pw"], database="api_sql_redis")
        cursor = db.cursor()
        
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        sql = "INSERT INTO messages(body,timestamp,u_id) VALUES ('{}','{}',{});".format(request.json["body"],timestamp,request.json["u_id"])
        print(sql)
        cursor.execute(sql)
        db.commit()
        resp = jsonify("Message '{}' added".format(request.json["body"]))
        resp.status_code = 200
        
        return resp

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        db.close()

@app.route("/v1/messages/<int:m_id>", methods=["DELETE"])
def delete_message(m_id):

    try:
        db = MySQLdb.connect(host=os.environ["mysql_ip"], user=os.environ["mysql_user"], passwd=os.environ["mysql_pw"], database="api_sql_redis")
        cursor = db.cursor()
        sql = "delete from messages where m_id = {};".format(m_id)
        cursor.execute(sql)
        resp = jsonify("Message m_id {} deleted".format(m_id))
        resp.status_code = 200
        db.commit()
        
        return resp

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        db.close()

# JOIN example
@app.route("/v1/messages/detail", methods=["GET"])
def get_messages_detail():

    try:
        db = MySQLdb.connect(host=os.environ["mysql_ip"], user=os.environ["mysql_user"], passwd=os.environ["mysql_pw"], database="api_sql_redis")
        cursor = db.cursor()
        sql = ("SELECT M.body,M.timestamp,U.name,U.address,J.name " 
                "FROM messages M JOIN users U ON M.u_id = U.u_id "
                "JOIN jobs J ON J.j_id = U.j_id ORDER BY M.timestamp;"
                )
        cursor.execute(sql)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        
        return resp

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        db.close()

if __name__ == "__main__":

    app.run(debug=True)