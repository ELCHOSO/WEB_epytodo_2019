from flask import *
from app import models

def register():
    try:
        username = request.form['username']
        password = request.form['password']
        if models.create_user(username, password) == 0:
            put_in_session(username)
            return json.dumps({"result" : "account created"})
        else:
            return json.dumps({"error" : "internal error"})
    except KeyError as error:
        print(error)
        return json.dumps({"error" : "internal error"})

def signin():
    username = request.form['username']
    password = request.form['password']
    err = models.check_user(username, password)
    if err == 0:
        put_in_session(username)
        return json.dumps({"result" : "signin successful"})
    elif err == 42:
        return json.dumps({"error" : "login or password does not match"})
    else:
        return json.dumps({"error" : "internal error"})

def put_in_session(username):
    session['username'] = username

def is_login():
    session.permanent = True
    if len(session) == 1:
        return (0)
    else:
        return (84)

def signout():
    session.clear()