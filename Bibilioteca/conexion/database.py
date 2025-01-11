from sqlalchemy import Column, Integer, String
from conexion.singletonConexion import db

class Usuario(db.Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)

    def __repr__(self):
        return f"<Usuario(id={self.id}, nombre='{self.nombre}')>"





