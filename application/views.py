from application import app, db
from flask import redirect, render_template, request, url_for
from application.tasks.models import Task
from application.auth.models import User

@app.route('/')
def index():
    return render_template("index.html", needs_tasks=User.find_users_with_no_tasks())


