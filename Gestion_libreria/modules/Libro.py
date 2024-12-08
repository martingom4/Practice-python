"""
Clase: Libro
+ titulo: str
+ autor: str
+ codigo: str
+ disponible: bool ya
+ cambiar_disponibilidad() ya
"""

class libro:
    codigo = 1
    def __init__(self, titulo, autor, disponible =True):
      self.titulo = titulo
      self.autor = autor
      libro.codigo =+ 1
      self.codigo = libro.codigo
      self.disponible = disponible

    def __str__(self):
        return f"El libro {self.titulo} de {self.autor} con codigo {self.codigo} esta disponible: {self.disponible}"

    def change_disponible(self):
        self.disponible = not self.disponible



