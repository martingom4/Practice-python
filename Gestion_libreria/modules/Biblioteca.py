"""
Clase: Biblioteca
+ catalogo_libros: list[Libro]
+ usuarios: list[Usuario]
+ agregar_libro()
+ registrar_usuario()
+ prestar_libro()
+ devolver_libro()
+ buscar_libro()
+ listar_libros_disponibles()
+ listar_libros_prestados()
"""
from modules.Libro import libro
from modules.Usuario import usuario

class biblioteca:
    def __init__(self):
        self.catalogo_libros = [] # aca vamos a trear los libros que se definieron en la clase libro
        self.usuarios = [] # aca vamos a trear los usuarios que se definieron en la clase usuario

    def agregar_libro(self, titulo, autor, codigo): #metodo para agregar un libro al catalogo
        agregar = libro(titulo, autor, codigo, True)
        self.catalogo_libros.append(agregar)

    def registrar_usuario(self, nombre):
        agregar = usuario(nombre)
        self.usuarios.append(agregar)


