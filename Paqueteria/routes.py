from flask import Blueprint, jsonify, request
from Paqueteria.crud import crear_paquete, listar_paquetes, actualizar_estado_paquete, eliminar_paquete
from Paqueteria.factories import PaqueteFactory
from Paqueteria.builders import PaqueteBuilder

paquete_bp = Blueprint("paquetes", __name__)

@paquete_bp.route("/", methods=["POST"])
def crear():
    '''crear un nuevo paquete'''
    data = request.json # se obtiene la informacion del paquete
    paquete = crear_paquete(data['descripcion'], data['peso'])
    return jsonify({"id": paquete.id, "descripcion": paquete.description, "peso": paquete.peso, "estado": paquete.estado})

@paquete_bp.route("/<int:id_paquete>", methods=["PUT"])
def actualizar(paquete_id):
    '''actualizar el estado de un paquete'''
    data = request.json
    paquete = actualizar_estado_paquete(paquete_id, data['estado']) # se actualiza el estado del paquete con el id dado por el usuario
    if paquete:# si este id existe se devuelve el paquete con el nuevo estado
        return jsonify({"id": paquete.id, "descripcion": paquete.description, "peso": paquete.peso, "estado": paquete.estado})
    return jsonify({"error": "Paquete no encontrado"}), 404 # si no se encuentra el paquete se devuelve un error 404

@paquete_bp.route('/<int:paquete_id>', methods=['DELETE'])
def eliminar(paquete_id):
    paquete = eliminar_paquete(paquete_id)
    if paquete:
        return jsonify({"message": "Paquete eliminado"})
    return jsonify({"error": "Paquete no encontrado"}), 404
