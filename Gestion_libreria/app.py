from modules.Biblioteca import biblioteca

inventario = biblioteca()#instanciamos la clase biblioteca para poder usar sus metodos

def main():
    mantener = True
    print("Bienvenido a la gestion de tu libreria \n")

    while mantener:
        print("que deseas hacer?\n")
        valor =int(input("1. Agregar un libro\n2. Registra un usuario\n3. prestar libro\n4. Buscar un libro\n5. Listar libros disponibles\n6. Listar usuario\n7. devolver libro\n8. ver historial de prestamo\n 9. Salir\n"))
        match valor:
            case 1:
                titulo = input("ingrese el titulo del libro: ")
                autor = input("ingrese el autor del libro: ")
                codigo = input("ingrese el codigo del libro: ")
                inventario.agregar_libro(titulo, autor, codigo)
            case 2:
                nombre = input("ingrese el nombre del usuario: ")
                inventario.registrar_usuario(nombre)
            case 3:
                id_usuario = int(input("ingrese el id del usuario: "))
                codigo = input("ingrese el codigo del libro: ")
                inventario.prestar_libro(id_usuario, codigo)
            case 4:
                codigo = input("ingrese el codigo del libro: ")
                inventario.buscar_libro(codigo)
            case 5:
                inventario.listar_libros()
            case 6:
                inventario.listar_usuarios()
            case 7:
                id_usuario = int(input("ingrese el id del usuario: "))
                codigo = input("ingrese el codigo del libro: ")
                inventario.devolver_libro(id_usuario, codigo)
            case 8:
                inventario.historial_prestamos()
            case 9:
                print("Gracias por usar la aplicacion")
                mantener = False
            case _:
                print("opcion no valida")





if __name__ == "__main__":
    main()


