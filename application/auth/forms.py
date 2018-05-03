from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjä")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False
        
class RegisterForm(FlaskForm):
    username = StringField("Käyttäjä")
    password = PasswordField("Salasana")
    passwordconfirmation = PasswordField("Toista salasana")
  
    class Meta:
        csrf = False
                