# esto es un ejemplo para conectarse a una base de datos con una ORM (SQLAlchemy)
from sqlalchemy import create_engine, Column, Integer, String# esto es para crear la conexion
from sqlalchemy.orm import sessionmaker , declarative_base


DATABASE_URL = "postgresql+psycopg2://postgres:1234@localhost:5432/Prueba" # URL para la conexion a la base de datos


engine  = create_engine(DATABASE_URL) # creamos la conexion con la url

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # creamos la sesion



#esto es para probar todo

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)

    def __repr__(self):
        return f"<Usuario(id={self.id}, nombre='{self.nombre}')>"




if __name__ == "__main__":
    # Crear las tablas en la base de datos
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas exitosamente")
