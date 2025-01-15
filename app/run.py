from Paqueteria import create_app
from flask import Flask
from flask_cors import CORS
from Paqueteria.routes import paquete_bp
from app.Paqueteria._database import db_instance

app = Flask(__name__)
CORS(app)  # Configura CORS globalmente para todas las rutas

# Configura la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:1234@localhost:5432/Prueba'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa la base de datos con la aplicación Flask
db_instance.init_app(app)

app.register_blueprint(paquete_bp, url_prefix='/api/paquetes')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
