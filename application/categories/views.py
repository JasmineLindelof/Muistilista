from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.categories.models import Category
from application.categories.forms import CategoryForm

@app.route("/categories/", methods=["GET"])
def categories_index():
   return render_template("categories/list.html", categories = Category.query.all())


  
@app.route("/categories/new/")
@login_required
def categories_form():
    return render_template("categories/new.html", form = CategoryForm(), categories = Category.get_categories_by_account(current_user.id))


@app.route("/categories/delete/<category_id>/", methods=["POST"])
@login_required
def categories_delete(category_id):

    c = Category.query.get(category_id)
    if c.account_id != current_user.id:

        return login_manager.unauthorized()

    db.session().delete(c)
    db.session().commit()
  
    return redirect(url_for("categories_create"))   

@app.route("/categories/new/", methods=["POST"])
@login_required
def categories_create():
    form = CategoryForm(request.form)
  
    if not form.validate():
        return render_template("categories/new.html", form = form)
  
    c = Category(form.name.data)
    
    c.account_id = current_user.id

    db.session().add(c)
    db.session().commit()
    return redirect(url_for("categories_create"))

       