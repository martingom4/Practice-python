from flask import Flask
from Paqueteria.database import db_instance

def create_app():
    '''Se encarga de crear e inicializar la aplicación Flask'''

    app = Flask(__name__)  # Instancia de Flask

    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:1234@localhost:5432/Prueba"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desactiva el seguimiento de modificaciones

    # Inicializar la base de datos
    db_instance.init_app(app)

    # Crear las tablas en la base de datos
    with app.app_context():  # Contexto necesario para operaciones relacionadas con Flask
        db_instance.db.create_all()

    # Registrar rutas
    from Paqueteria.routes import paquete_bp
    app.register_blueprint(paquete_bp, url_prefix="/api/paquetes")  # Se registra la ruta

    return app  # Se retorna la aplicación
