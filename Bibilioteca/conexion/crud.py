from conexion.database import Usuario
from conexion.singletonConexion import db



def crear_usuario(nombre):
    session = db.SessionLocal()
    try:
        nuevo_usuario = Usuario(nombre=nombre)
        session.add(nuevo_usuario)
        session.commit()
        session.refresh(nuevo_usuario)
        print(f"Usuario creado: {nuevo_usuario}")
    except Exception as e:
        print(f"Error al crear usuario: {e}")
        session.rollback()
    finally:
        session.close()

def obtener_usuarios():
    session = db.SessionLocal()
    try:
        usuarios = session.query(Usuario).all()
        return usuarios
    except Exception as e:
        print(f"Error al obtener usuarios: {e}")
        return []
    finally:
        session.close()
