from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate

from config import DevelopmentConfig
from models import db


from maestros.routes import maestros_bp
from alumnos.routes import alumnos_bp
from cursos.routes import cursos_bp
from inscripcion.routes import inscripcion_bp

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)

app.register_blueprint(maestros_bp, url_prefix="/maestros")
app.register_blueprint(alumnos_bp, url_prefix="/alumnos")

app.register_blueprint(cursos_bp, url_prefix="/cursos")
app.register_blueprint(inscripcion_bp, url_prefix="/inscripcion")


@app.route("/")
def index():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.run()
