from flask_wtf import FlaskForm # base class helps to create the class
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    name=StringField("FullName", validators=[DataRequired(message="Name required")])
    email=StringField("Email", validators=[DataRequired(message="Email required"), Email(message="That doesn't look like a valid email")])
    password=PasswordField("Password", validators=[DataRequired(message="Password is required"), Length(min=6,message="Password must consists special charcter")])
    submit=SubmitField("Register")
    