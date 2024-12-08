"""
    Clase: Usuario
+ id_usuario: str
+ nombre: str
+ libros_prestados: list
+ historial_prestamos: list
+ prestar_libro()
+ devolver_libro()
+ ver_historial()
"""

class usuario:
    ultimo_id = 0
    def __init__(self, nombre):
        usuario.ultimo_id += 1
        self.id_usuario = usuario.ultimo_id
        self.nombre = nombre
        self.libros_prestados = []
        self.historial_prestamos = []

    def prestar_libro(self):
        pass

    def devolver_libro(self):
        pass

    def ver_historial(self):
        pass

