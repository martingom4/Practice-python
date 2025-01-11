from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


#vamos a implementar el patron de diseño singleton para la conexion a la base de datos
class Database ():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        #aca vamos a llamar a la conexion de la base de datos para que se conecte solo una vez
        DATABASE_URL = "postgresql+psycopg2://martingom4:1234@localhost:5432/Prueba"
        self.engine = create_engine(DATABASE_URL)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()
        



