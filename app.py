from flask import Flask, render_template,request,redirect,url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms
from models import db
from models import Alumnos
from flask_migrate import Migrate



app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate=Migrate(app,db)

csrf = CSRFProtect(app)

@app.route("/",methods=['GET','POST'])
@app.route("/index")
def index():
    create_form=forms.UserForm(request.form)
    alumno=Alumnos.query.all()

    return render_template("index.html",form=create_form,alumno=alumno)



@app.route("/Alumnos",methods=["GET","POST"])
def alumnos():
    create_form=forms.UserForm(request.form)
    if request.method=='POST':
        alum = Alumnos(
            nombre = create_form.nombre.data,
            apellido = create_form.aPaterno.data,
            email = create_form.email.data,
            telefono = create_form.telefono.data
        )
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("alumnos.html",form=create_form)

@app.route("/detalles", methods=['GET', 'POST'])
def detalles():
    create_form = forms.UserForm(request.form)

    if request.method=='GET':
        id=request.args.get('id')
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        id=request.args.get('id')
        nombre=alum1.nombre
        apellidos=alum1.apellidos
        email=alum1.email
        

    return render_template("detalles.html", nombre=nombre, apellidos=apellidos, email=email)

@app.route("/modificar", methods=["GET", "POST"])
def modificar():
    create_form = forms.UserForm(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()

        create_form.id.data = alum.id
        create_form.nombre.data = alum.nombre
        create_form.apellidos.data = alum.apellidos
        create_form.email.data = alum.email

        return render_template("modificar.html", form=create_form)

    if request.method == 'POST':
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()

        alum.nombre = create_form.nombre.data.rstrip()
        alum.apellidos = create_form.apellidos.data
        alum.email = create_form.email.data

        db.session.commit()

        return redirect("/modificar?id=" + str(id))
    

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route("/eliminar", methods=["GET", "POST"])
def eliminar():
    create_form = forms.UserForm(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        alum = Alumnos.query.get(id)

        if not alum:
            return redirect(url_for('index'))

        create_form.id.data = alum.id
        create_form.nombre.data = alum.nombre
        create_form.apellidos.data = alum.apellidos
        create_form.email.data = alum.email

        return render_template("eliminar.html", form=create_form)

    elif request.method == 'POST':
        id = create_form.id.data
        alum = Alumnos.query.get(id)

        if alum:
            db.session.delete(alum)
            db.session.commit()

        return redirect(url_for('index'))

    return redirect(url_for('index'))

if __name__ == '__main__':
    
    with app.app_context():
        db.create_all()
    app.run()
