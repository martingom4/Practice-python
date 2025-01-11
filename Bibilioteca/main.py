from conexion.singletonConexion import db
from conexion.crud import crear_usuario, obtener_usuarios

if __name__ == "__main__":
    # Crear las tablas en la base de datos
    print("Creando tablas...")
    db.Base.metadata.create_all(bind=db.engine)
    print("Tablas creadas exitosamente")

    # Pruebas CRUD
    print("Creando usuarios...")
    crear_usuario("Juan")
    crear_usuario("Ana")

    print("Obteniendo usuarios...")
    usuarios = obtener_usuarios()
    for usuario in usuarios:
        print(usuario)
