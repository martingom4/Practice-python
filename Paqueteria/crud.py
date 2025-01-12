from Paqueteria.database import db
from Paqueteria.models import paquete
#piensa que todo esto es para la base de datos y para la tabla paquete que se va a crear en la base de datos nada mas que eso

# se crea un nuevo paquete que se hara en la base de datos
def crear_paquete(descripcion, peso,estado='pendiente'):
    nuevo_paquete = paquete(description=descripcion, peso=peso, estado=estado)
    db.session.add(nuevo_paquete)
    db.session.commit()
    return nuevo_paquete

#listar paquetes
def listar_paquetes():
    return paquete.query.all()

#actualizar estado de un paquete

def actualizar_estado_paquete(id_paquete,nuevo_estado):
    paquete = paquete.query.get(id_paquete)
    if paquete:#si esxiste el paquete
        paquete.estado = nuevo_estado
        db.session.commit()
        return paquete
    return None # si no existe el paquete se retorna None

#eliminar paquete
def eliminar_paquete(id_paquete):
    paquete = paquete.query.get(id_paquete)
    if paquete:# si el paquete existe en la base de datos se elimina el paquete
        db.session.delete(paquete)
        db.session.commit()
        return paquete
    return None # si no se encuentra ningun paquete en la base de datos no se devuelve nada
