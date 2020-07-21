import pymysql as sql
from flask import *
from config import Databaseparams

db = Databaseparams()

def connect_db():
    try:
        connect = sql.connect(host = db.host,
            unix_socket = db.unix_socket, user = db.user,
            password = db.password, db = db.name)
        return (connect)
    except Exception as error:
        print(error)
        raise

def create_user(username, password):
    try:
        connect = connect_db()
        cursor = connect.cursor()
        values = (username, password)
        cursor.execute("insert into user(username, password) values(%s, password(%s))", values)
        connect.commit()
        cursor.close()
        connect.close()
        return (0)
    except Exception as error:
        print(error)
        return (84)

def check_user(username, password):
    try:
        connect = connect_db()
        cursor = connect.cursor()
        values = (username, password)
        cursor.execute("select * from user where username = %s and password = password(%s)", values)
        fetch = cursor.fetchall()
        if len(fetch) == 0:
            return (42)
        elif len(fetch) == 1:
            return (0)
        else:
            return (42)
    except Exception as error:
        print(error)
        return(84)

def show_user():
    try:
        connect = connect_db()
        cursor = connect.cursor()
        values = (session['username'])
        cursor.execute("select * from user where username = %s", values)
        fetch = cursor.fetch
        return (fetch[0])
    except Exception as error:
        print(error)
        return (84)