from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField
from wtforms.validators import DataRequired, Length, Email
from wtforms import HiddenField


class UserForm(FlaskForm):
    id = HiddenField()
    nombre = StringField('Nombre', validators=[DataRequired()])
    apaterno = StringField('Apaterno', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])