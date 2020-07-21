from flask import *
from app import app, controller, models

@app.route('/', methods =['GET'])
@app.route('/index', methods =['GET'])
def route_home():
    return render_template("index.html")

@app.route('/user', methods =['GET'])
def route_user_info():
    if controller.is_login() == 0:
        return json.dumps({"error" : "you must be logged in"})
    return render_template("user_info.html",
                            content = models.show_user)

@app.route('/user/task', methods =['GET'])
def route_user_tasks():
    if controller.is_login() == 0:
        return json.dumps({"error" : "you must be logged in"})
    return render_template("user_task.html")

@app.route('/user/task/<id>', methods =['GET'])
def route_user_task_id_get(id):
    if controller.is_login() == 0:
        return json.dumps({"error" : "you must be logged in"})
    return render_template("user_task_id.html", id = id)

@app.route('/register', methods =['GET', 'POST'])
def route_register():
    if controller.is_login() == 0:
        return json.dumps({"error" : "you must be logged in"})
    if request.method == 'POST':
        return render_template("registration.html",
                                content = controller.register())
    else:
        return render_template("registration.html")


@app.route('/signin', methods =['GET', 'POST'])
def route_sign_in():
    if request.method == 'POST':
        return render_template("signin.html",
                                content = controller.signin())
    else:
        return render_template("signin.html")

@app.route('/signout', methods =['POST'])
def route_sign_out():
    if controller.is_login() == 0:
        return json.dumps({"error" : "you must be logged in"})
    controller.signout()

# @app.route('/user/task/<id>', methods =['POST'])
# def route_user_task_id_post(id):
#     return "Hello user task id post\n"

# @app.route('/user/task/add', methods =['POST'])
# def route_user_task_add():
#     return "Hello user task add\n"

# @app.route('/user/task/del/<id>', methods =['POST'])
# def route_user_task_del_id(id):
#     return "Hello user task del id\n"
