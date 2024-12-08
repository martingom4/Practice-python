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
from modules.Libro import libro
class usuario:
    ultimo_id = 0
    def __init__(self, nombre):
        usuario.ultimo_id += 1
        self.id_usuario = usuario.ultimo_id
        self.nombre = nombre
        self.libros_prestados = []
        self.historial_prestamos = []

    def __str__(self):
        return f"El usuario {self.nombre} con id {self.id_usuario}"

    def prestar_libro(self,titulo, autor, codigo):
        #lo que tengo que hacer aca es agregar el libro prestado a libros_prestados y agregar el libro al historial de prestamos
        prestamo = libro(titulo, autor, codigo)
        # prestamo = #aca pondre el libro que se presto y el usuario que lo presto pero antes debo de recuperar toda la informacion del libro
        self.libros_prestados.append(prestamo)
        self.historial_prestamos.append(prestamo)

    def devolver_libro(self, codigo):
        for libro in self.libros_prestados:
            if libro.codigo == codigo:
                self.libros_prestados.remove(libro)
                libro.change_disponible()
                print("Libro devuelto")
            else:
                print("Libro no encontrado")

    def ver_historial(self):
        for prestamo in self.historial_prestamos:
            print(prestamo)

