from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate

from config import DevelopmentConfig
from models import db, Alumnos
from maestros.routes import maestros_bp
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# Inicializaciones (SOLO UNA VEZ)
db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)

# Registrar blueprint
app.register_blueprint(maestros_bp, url_prefix="/maestros")


@app.route("/",methods=['GET','POST'])
@app.route("/index")
def index():
    create_form=forms.UserForm(request.form)
    alumno=Alumnos.query.all()

    return render_template("index.html",form=create_form,alumno=alumno)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route("/Alumnos", methods=["GET", "POST"])
def alumnos():
    create_form = forms.UserForm()

    if request.method == "POST":
        if create_form.validate():
            alum = Alumnos(
                nombre=create_form.nombre.data,
                apellidos=create_form.apellidos.data,
                telefono=create_form.telefono.data,
                email=create_form.email.data
            )
            db.session.add(alum)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template("agregar.html", form=create_form)

@app.route("/detalles",methods=["GET","POST"])
def detalles():
    if request.method=='GET':
        id = request.args.get('id')
        alum= db.session.query(Alumnos).filter(Alumnos.id==id).first()
        nombre = alum.nombre
        apellidos = alum.apellidos
        telefono = alum.telefono
        email = alum.email
    return render_template("detalles.html",alum=alum,nombre=nombre, apellidos = apellidos,telefono=telefono, email=email)

@app.route("/modificar",methods=["GET","POST"])
def modificar():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
        id = request.args.get('id')
        alum= db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data=alum.nombre
        create_form.apellidos.data=alum.apellidos
        create_form.telefono.data=alum.telefono
        create_form.email.data=alum.email
    if request.method=='POST':
        id = create_form.id.data
        alum= db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum.id = id
        alum.nombre = str.rstrip(create_form.nombre.data)
        alum.apellidos = create_form.apellidos.data
        alum.telefono = create_form.telefono.data
        alum.email = create_form.email.data
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("modificar.html",form=create_form,nombre=create_form.nombre.data, apellidos = create_form.apellidos.data, email=create_form.email.data)

@app.route("/eliminar",methods=["GET","POST"])
def eliminar():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
        id = request.args.get('id')
        alum= db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data=alum.nombre
        create_form.apellidos.data=alum.apellidos
        create_form.telefono.data=alum.telefono
        create_form.email.data=alum.email
    if request.method=='POST':
        id = create_form.id.data
        alum= db.session.query(Alumnos).get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("eliminar.html",form=create_form)


if __name__ == '__main__':
    
    with app.app_context():
        db.create_all()
    app.run()
