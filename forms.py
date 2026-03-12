from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField
from wtforms.validators import DataRequired, Length, Email
from wtforms import HiddenField
from wtforms import StringField, SelectField



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



class CursoForm(FlaskForm):
    nombre = StringField("Nombre del Curso", validators=[DataRequired()])
    descripcion = StringField("Descripción", validators=[DataRequired()])
    maestro_id = SelectField("Maestro", coerce=int, validators=[DataRequired()])



class InscripcionForm(FlaskForm):
    id = HiddenField()  
    alumno_id = SelectField(
        "Alumno",
        coerce=int,  
        validators=[DataRequired()]
    )
    curso_id = SelectField(
        "Curso",
        coerce=int,
        validators=[DataRequired()]
    )