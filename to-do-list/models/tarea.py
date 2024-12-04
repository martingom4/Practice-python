# esta es la clase tarea en la que definimos los atributos de la tarea y metodo de impresion 
class Tarea:
    contador = 0
    def __init__(self, titulo, descripcion):
        self.id = Tarea.contador
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = "pendiente"

        Tarea.contador += 1

    def __str__(self):
        return f"Id:{self.id}\nTarea: [{self.estado.capitalize()}] {self.titulo}\nDescripción: {self.descripcion}"

    def completar(self):
        self.estado = "completada"



