from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField,  StringField, validators

class TaskForm(FlaskForm):
    name = StringField("Tehtävä", [validators.Length(min=2)])
    category = SelectField("Kategoria", choices = [('1', 'Työ'),('2', 'Koti')])
    #done = BooleanField("Tehty")
  
    class Meta:
        csrf = False

