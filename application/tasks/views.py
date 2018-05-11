from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.tasks.models import Task
from application.categories.models import Category
from application.tasks.forms import TaskForm


@app.route("/tasks/", methods=["GET"])
@login_required
def tasks_index():
    return render_template("tasks/list.html", tasks =  Task.get_tasks_by_account(current_user.id))


  
@app.route("/tasks/new/")
@login_required
def tasks_form():
    categories = Category.get_categories_by_account(current_user.id)
    print(categories)
    form = TaskForm()
    form.category.choices = categories
    return render_template("tasks/new.html", form = form)


@app.route("/tasks/<task_id>/", methods=["POST"])
@login_required
def tasks_set_done(task_id):

    t = Task.query.get(task_id)
    if t.account_id != current_user.id:

        return login_manager.unauthorized()

    t.done = True
    db.session().commit()
  
    return redirect(url_for("tasks_index"))


@app.route("/tasks/delete/<task_id>/", methods=["POST"])
@login_required
def tasks_delete(task_id):

    t = Task.query.get(task_id)
    if t.account_id != current_user.id:

        return login_manager.unauthorized()

    db.session().delete(t)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))    
  
@app.route("/tasks/", methods=["POST"])
@login_required
def tasks_create():
    form = TaskForm(request.form)
    form.category.choices = Category.get_categories_by_account(current_user.id)
  
    if not form.validate():
        return render_template("tasks/new.html", form = form)
  
    
    t = Task(form.name.data, form.importance.data, Category.get_all_by_ids(form.category.data))
    t.importance = form.importance.data
    t.account_id = current_user.id
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

"""
@app.route("/tasks/edit/<task_id>/", methods=["POST"])
@login_required
def tasks_edit(task_id):

    t = Task.query.get(task_id)
    if t.account_id != current_user.id:
        return login_manager.unauthorized()

    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("tasks_index"))
"""
   
    

@app.route("/tasks/edit/<task_id>/")
@login_required
def tasks_edit():
    return render_template("tasks/edit.html", form = TaskForm())    
