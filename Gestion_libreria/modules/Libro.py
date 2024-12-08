"""
Clase: Libro
+ titulo: str
+ autor: str
+ codigo: str
+ disponible: bool
+ cambiar_disponibilidad()
"""

class libro:
    def __init__(self, titulo, autor, codigo, disponible =True):
      self.titulo = titulo
      self.autor = autor
      self.codigo = codigo
      self.disponible = disponible

    def __str__(self):
        return f"El libro {self.titulo} de {self.autor} con codigo {self.codigo} esta disponible: {self.disponible}"

    def change_disponible(self):
        self.disponible = not self.disponible



