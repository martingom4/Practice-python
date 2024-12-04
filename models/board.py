class Board:

    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho
        self.botin = self.create_board()  # Inicializa el tablero aquí

    def create_board(self):
        # Crear y devolver un tablero (matriz) de tamaño alto x ancho
        return [[0 for _ in range(self.ancho)] for _ in range(self.alto)]

    def change_example(self):
        # Cambia un valor específico en el tablero (ejemplo en la posición [0][1])
        self.botin[0][1] = 1
        print("Tablero después de cambiar un valor:")
        for row in self.botin:
            print(row)





























