from flask_sqlalchemy import SQLAlchemy

class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.db = SQLAlchemy()
        self.is_initialized = False # Inicialmente no está inicializado

    def init_app(self, app):
        """Vincula la aplicación Flask con la base de datos."""
        if self.is_initialized:
            raise RuntimeError("La base de datos ya fue inicializada.")
        self.db.init_app(app)  # Conecta SQLAlchemy con la app Flask
        self.is_initialized = True # Ahora está inicializado

# Instancia global del Singleton
db_instance = Database()
db = db_instance.db
