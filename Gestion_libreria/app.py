class Libro:
    def __init__(self, titulo, autor, isbn, precio, cantidad):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__precio = precio
        self.__cantidad = cantidad

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        if valor > 0:
            self.__precio = valor
        else:
            print("El precio debe ser mayor a 0")

    def vender(self, cantidad):
        if self.__cantidad >= cantidad:
            self.__cantidad -= cantidad
            return self.__precio * cantidad
        else:
            print("No hay suficiente stock")
            return 0

class LibroFisico(Libro):
    def __init__(self, titulo, autor, isbn, precio, cantidad, peso, tamaño):
        super().__init__(titulo, autor, isbn, precio, cantidad)
        self.peso = peso
        self.tamaño = tamaño

    def detalles(self):
        return f"{self.__titulo} de {self.__autor} - {self.peso}kg, {self.tamaño}cm"

class Cliente:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.libros_comprados = []

    def comprar_libro(self, libro, cantidad):
        precio_total = libro.vender(cantidad)
        if precio_total > 0:
            self.libros_comprados.append((libro, cantidad))
            return precio_total
        return 0

# Uso
libro1 = LibroFisico("Python para Todos", "Juan Pérez", "123456", -30.0,10,0.5, 21)
cliente1 = Cliente("Carlos", "Av. Siempre Viva 123")
precio = cliente1.comprar_libro(libro1, 2)
print(f"Precio total: {precio}")
