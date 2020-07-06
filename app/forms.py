from flask_wtf import FlaskForm
from wtforms import PasswordField, SelectField, StringField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, NumberRange


class LoginForm(FlaskForm):
    email = StringField(
        "Email", validators=[DataRequired(), Email("Enter a valid email address")]
    )
    password = PasswordField("Password", validators=[DataRequired()])

class RegisterForm(FlaskForm):
    email = StringField(
        "Email", validators=[DataRequired(), Email("Enter a valid email address")]
    )
    password = PasswordField("Password", validators=[DataRequired()])

