from modules.Biblioteca import biblioteca

biblioteca = biblioteca()#instanciamos la clase biblioteca para poder usar sus metodos

def main():
    print("Bienvenido a la gestion de tu libreria \n")
    print("que deseas hacer?\n")
    valor =int(input("1. Agregar un libro\n2. Registra un usuario\n3. Devolver un libro\n4. Buscar un libro\n5. Listar libros disponibles\n6. Listar libros prestados\n7. Salir\n"))
    match valor:
        case 1:
            titulo = input("ingrese el titulo del libro: ")
            autor = input("ingrese el autor del libro: ")
            codigo = input("ingrese el codigo del libro: ")
            biblioteca.agregar_libro(titulo, autor, codigo)
        case 2:
            nombre = input("ingrese el nombre del usuario: ")
            biblioteca.registrar_usuario(nombre)
        case _:
            print("opcion no valida")





if __name__ == "__main__":
    main()


