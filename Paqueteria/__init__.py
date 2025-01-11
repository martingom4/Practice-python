from flask import Flask
from Paqueteria.database import db

def create_app():
    '''se encarga de crear e inicilizar la aplicacion flask'''

    app = Flask(__name__) # instancia de flask

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:1234@localhost:5432/Prueba"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # para que no se muestren las modificaciones

    # inicializar la base de datos
    db.init_app(app)

    #Para poder registar rutas
    from Paqueteria.routes import paquete_bp
    app.register_blueprint(paquete_bp, url_prefix="api/paquetes") # se registra la ruta

    return app# se retorna la aplicacion


