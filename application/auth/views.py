from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
   

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                                error = "Käyttäjätunnusta ei ole olemassa")


    login_user(user)
    return redirect(url_for("tasks_index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("tasks_index"))    

@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/registerform.html", form = RegisterForm())

    form = RegisterForm(request.form)


    user = User.query.filter_by(username=form.username.data).first()
    confirmed = form.password.data == form.passwordconfirmation.data
    if user:
        return render_template("auth/registerform.html", form = form,
                                error = "Käyttäjätunnus on varattu")
    if not confirmed:
        return render_template("auth/registerform.html", form = form,
                                error = "Salasanat eivät täsmää")

    x = User(form.username.data, form.password.data)  

    db.session().add(x)
    db.session().commit()                          


    login_user(x)
    return redirect(url_for("index"))