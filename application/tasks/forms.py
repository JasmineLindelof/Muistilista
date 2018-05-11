from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField,  StringField, validators, SelectMultipleField

class TaskForm(FlaskForm):
    name = StringField("Tehtävä", [validators.Length(min=2)])
    category = SelectMultipleField("Kategoria", coerce=int)
    #done = BooleanField("Tehty")
    importance = SelectField("Tärkeys", choices = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
  
    class Meta:
        csrf = False

