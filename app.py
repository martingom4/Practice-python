from models.board import Board

def main():
    activo = True
    size = Board(5, 5)  # Crear una instancia del tablero
    print("Bienvenido a Battleship")

    while activo:
        try:
            # Solicitar la opción del usuario
            value = int(input("Ingrese la opción deseada:\n1. Crear tablero\n2. Salir\n3. Cambiar valor de ejemplo\n"))

            match value:
                case 1:
                    print("Crear tablero")
                    # No es necesario usar una variable Botin aquí, ya está en self.botin
                    for row in size.botin:
                        print(row)
                case 2:
                    print("Salir")
                    activo = False
                case 3:
                    print("Cambiar valor de ejemplo")
                    size.change_example()  # Llamamos al método para cambiar el valor y mostrar el tablero
                case _:
                    print("Opción no válida")
        except ValueError:
            print("Por favor, ingresa un número válido.")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido. Saliendo...")
            activo = False

if __name__ == "__main__":
    main()
