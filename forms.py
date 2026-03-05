from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField
from wtforms.validators import DataRequired, Length, Email
from wtforms import HiddenField


class UserForm(FlaskForm):
    id = HiddenField()
    nombre = StringField('Nombre', validators=[DataRequired(),Length(min=2, max=50)])
    apellidos = StringField('Apellidos', validators=[DataRequired(),Length(min=2, max=50)])
    email = EmailField('Email', validators=[DataRequired(), Email(),Length(min=2, max=50)])
    telefono = StringField('Telefono', validators=[DataRequired(),Length(min=2, max=50)])


class MaestroForm(FlaskForm):
    

    nombre = StringField(
        'Nombre',
        validators=[
            DataRequired(),
            Length(min=2, max=50)
        ]
    )

    apellidos = StringField(
        'Apellidos',
        validators=[
            DataRequired(),
            Length(min=2, max=200)
        ]
    )

    especialidad = StringField(
        'Especialidad',
        validators=[
            DataRequired(),
            Length(min=2, max=200)
        ]
    )

    email = EmailField(
        'Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )