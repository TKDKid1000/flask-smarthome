from flask import Flask, request, render_template, flash, redirect, url_for
from flask_login import login_required, current_user

import traceback
import os
import json

@login_required
def home():
    return render_template("index.html", user=current_user.id)

@login_required
def lights():
    with open("lights.json") as f:
        lights = json.load(f)
    if request.method == "GET":
        return render_template("lights.html", lights=lights)
    switch = request.form["lightswitch"]
    if switch in lights:
        print(switch + " activated")
        return redirect(url_for("lights"))
    else:
        print(switch + " not valid")
        return redirect(url_for("lights"))

@login_required
def shell():
    if request.method == "GET":
        return render_template("shell.html", user=current_user.id)
    if request.form["cmd"] == None or request.form["cmd"].strip() == "":
        return render_template("shell.html", output="No command entered", user=current_user.id)
    else:
        stream = os.popen(request.form["cmd"])
        output = stream.read()
        return render_template("shell.html", output=output, user=current_user.id)


@login_required
def pythononline():
    default = '''print("hello world")'''
    if request.method == "GET":
        return render_template("pythononline.html", user=current_user.id, default=default)
    if request.form["script"] == None or request.form["script"].strip() == "":
        return render_template("pythononline.html", output="No command entered", user=current_user.id)
    else:
        with open("pyonline.py", "w") as f:
            f.write(request.form["script"])
        stream = os.popen("py pyonline.py")
        return render_template("pythononline.html", output=stream.read(), user=current_user.id, default=request.form["script"])
