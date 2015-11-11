from flask_wtf import Form 
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
	username = TextField('Usename', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])

	