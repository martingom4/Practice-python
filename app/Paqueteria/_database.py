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
        self.is_initialized = True #para que solo se inicialice una ves y el self.is_initialized significa que ya se inicializo

    def init_app(self, app):
        """Vincula la aplicación Flask con la base de datos."""
        if not self.is_initialized:
            raise RuntimeError("La base de datos ya fue inicializada.")
        self.db.init_app(app)  # Conecta SQLAlchemy con la app Flask

# Instancia global del Singleton
db_instance = Database()
db = db_instance.db
