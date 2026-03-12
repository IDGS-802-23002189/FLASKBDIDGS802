import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Inscripcion(db.Model):
    __tablename__ = 'inscripciones'

    id = db.Column(db.Integer, primary_key=True)
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumnos.id'), nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'), nullable=False)

 
    __table_args__ = (
        db.UniqueConstraint('alumno_id', 'curso_id', name='unique_inscripcion'),
    )

class Alumnos(db.Model):
    __tablename__ = 'alumnos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), unique=True)
    telefono = db.Column(db.String(100))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)

    cursos = db.relationship(
        'Cursos',
        secondary='inscripciones',
        back_populates='alumnos'
    )


class Maestros(db.Model):
    __tablename__ = 'maestros'

    matricula = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(200), nullable=False)
    especialidad = db.Column(db.String(200))
    email = db.Column(db.String(100), unique=True)

 
    cursos = db.relationship('Cursos', back_populates='maestro')


class Cursos(db.Model):
    __tablename__ = 'cursos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200))
    maestro_id = db.Column(db.Integer, db.ForeignKey('maestros.matricula'))

    maestro = db.relationship('Maestros', back_populates='cursos')
    alumnos = db.relationship(
        'Alumnos',
        secondary='inscripciones',
        back_populates='cursos'
    )