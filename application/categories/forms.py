from flask_wtf import FlaskForm
from wtforms import  StringField, validators

class CategoryForm(FlaskForm):
    name = StringField("Kategoria", [validators.Length(min=2)])
    
    class Meta:
        csrf = False

