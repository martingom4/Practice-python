"""
Clase: Biblioteca
+ catalogo_libros: list[Libro]
+ usuarios: list[Usuario]
+ agregar_libro()ya
+ registrar_usuario()ya
+ prestar_libro()ya
+ devolver_libro()ya
+ buscar_libro()ya
+ listar_libros_disponibles() ya
+ listar_libros_prestados() ya
"""
from modules.Libro import libro
from modules.Usuario import usuario

class biblioteca:
    def __init__(self):
        self.catalogo_libros = [] # aca vamos a trear los libros que se definieron en la clase libro
        self.usuarios = [] # aca vamos a trear los usuarios que se definieron en la clase usuario

    def agregar_libro(self, titulo, autor, codigo): #metodo para agregar un libro al catalogo
        agregar = libro(titulo, autor,codigo, True)
        self.catalogo_libros.append(agregar)

    def registrar_usuario(self, nombre):
        agregar = usuario(nombre)
        self.usuarios.append(agregar)

    def prestar_libro(self, id_usuario, codigo):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                for libro in self.catalogo_libros:
                    if libro.codigo == codigo:
                        if libro.disponible:
                            libro.change_disponible()
                            usuario.prestar_libro(libro.titulo, libro.autor, libro.codigo)
                            print("Libro prestado")
                        else:
                            print("Libro no disponible")
                    else:
                        print("Libro no encontrado")
            else:
                print("Usuario no encontrado")

    def devolver_libro(self, id_usuario, codigo):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                usuario.devolver_libro(codigo)
            else:
                print("Usuario no encontrado")


    def listar_libros(self):
        for libro in self.catalogo_libros:
            print(libro)

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)

    def buscar_libro(self,codigo):
        for libro in self.caltalogo_libros:
            if libro.codigo == codigo:
                print(libro)
            else:
                print("Libro no encontrado")

    def listar_disponibles(self):
        for libro in self.catalogo_libros:
            if libro.disponible:
                print(libro)

    def listar_prestados(self):
        for libro in self.catalogo_libros:
            if not libro.disponible:
                print(libro)

    def historial_prestamos(self):
        #aca debemos recorrer la lista de usuarios y mostrar el historial de prestamos de cada uno
        for usuario in self.usuarios:
            usuario.ver_historial() # debe de devolver el historial de prestamos de cada usuario
