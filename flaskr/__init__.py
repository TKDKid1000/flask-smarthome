import os
import json

from flask import Flask, request, render_template, flash, redirect, url_for
from flask_login import LoginManager
import flask_login
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True, template_folder='template')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )
    login_manager = LoginManager()
    login_manager.init_app(app)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    app.url_map.strict_slashes = False

    from . import dash
    app.add_url_rule("/dash", view_func=dash.home)
    app.add_url_rule("/", view_func=dash.home)
    app.add_url_rule("/dash/lights", view_func=dash.lights, methods=["GET", "POST"])
    app.add_url_rule("/dash/shell", view_func=dash.shell, methods=["GET", "POST"])
    app.add_url_rule("/dash/pythononline", view_func=dash.pythononline, methods=["GET", "POST"])

    
    class User(flask_login.UserMixin):
        pass
    with open("accounts.json") as f:
        users = json.load(f)

    @app.errorhandler(404)
    def notfounderror(e):
        return render_template("404.html"), 404

    @app.errorhandler(401)
    def unauthorizederror(e):
        return redirect(url_for("login"))

    @login_manager.user_loader
    def load_user(email):
        if email not in users:
            return
        user = User()
        user.id = email
        return user

    @login_manager.request_loader
    def load_request(request):
        email = request.form.get("email")
        if email not in users:
            return
        user = User()
        user.id = email
        user.is_authenticated = request.form["password"] == users[email]["password"]
        return user
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == "GET":
            return render_template("login.html")
        email = request.form["email"]
        if email in users:
            if request.form["password"] == users[email]:
                user = User()
                user.id = email
                flask_login.login_user(user)
                return redirect(url_for("home"))
            else:
                return f"incorrect password. <a href='{url_for('''login''')}'>Try Again</a>"
        else:
            return f"incorrect email <a href='{url_for('''login''')}'>Try Again</a>"

    @app.route("/logout")
    def logout():
        flask_login.logout_user()
        return redirect(url_for("login"))
    return app
