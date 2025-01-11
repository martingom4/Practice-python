class PaqueteBuilder:
    def __init__(self):
        self.paquete = {"descripcion": None, "peso": None, "estado": "pendiente"} #ya tenemos inicializado el paquete que con el que vamos a trabajar

    def set_descrpcion(self, descripcion):
        self.paquete["decripcion"] = descripcion # esta es la que el usuario va a ingresar
        return self # esto porque vamos a hacer un metodo encadenado y vamos a retornar el objeto mismo para poder seguir trabajando con el

    def set_peso(self, peso):
        self.paquete["peso"]= peso
        return self

    def set_estado(self, estado):
        self.paquete["estado"] = estado
        return self

    def build(self):
        return self.paquete # se retorna el paquete que ya esta construido y listo para ser usado
