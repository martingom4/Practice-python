#aca vamos hacer la conexion a la base de datos para poder guardar y manipular los datos piola
from flask_sqlalchemy import SQLAlchemy #indispensable para la conexion a la base de datos

class DataBase: #clase que se encargara de la conexion a la base de datos unica para toda la aplicacion
    _instance = None #variable que se encargara de verificar si la conexion ya fue hecha
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.db = SQLAlchemy()
        self.is_initialized = False # Inicialmente no está inicializado

    def init_app(self, app): # esta funcion es para poder inicializar la conexion a la base de datos
        """Vincula la aplicación Flask con la base de datos."""
        if self.is_initialized: # verifica si la conexion ya fue hecha
            raise RuntimeError("La base de datos ya fue inicializada.")
        self.db.init_app(app)  # Conecta SQLAlchemy con la app Flask
        self.is_initialized = True # y cambia el estado a inicializado o True

# Instancia global del Singleton
db_instance = DataBase() #instancia de la clase DataBase
db = db_instance.db #variable que se encargara de la conexion a la base de datos


