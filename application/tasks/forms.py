from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField,  StringField, validators

class TaskForm(FlaskForm):
    name = StringField("Tehtävä", [validators.Length(min=2)])
    category = SelectField(u'Group', coerce=int)
    #done = BooleanField("Tehty")
    importance = SelectField("Tärkeys", choices = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
  
    class Meta:
        csrf = False

#def edit_user(request, id):
#    user = User.query.get(id)
#    form.group_id.choices = [(g.id, g.name) for g in categories('name')]
#    form = UserDetails(request.POST, obj=user)