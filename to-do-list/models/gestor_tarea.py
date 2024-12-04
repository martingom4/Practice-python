from models.tarea import Tarea
import json # Importamos la librería json para poder guardar y cargar los datos en un archivo json
class gestorTarea:
    def __init__(self):
        self.tareas= []

    def agregarTarea(self, titulo:str , descripcion:str):
        nueva_tarea = Tarea(titulo, descripcion)
        self.tareas.append(nueva_tarea)

    def listar_tareas(self):
        for tarea in self.tareas:
            print(tarea)

    def buscar_id(self, id:int):
        for tarea in self.tareas:
            if tarea.id == id:
                return tarea

    def completar_tarea(self, id_tarea:int):
        tarea = self.buscar_id(id_tarea)
        if tarea:
            tarea.completar()
        else:
            print("Tarea no encontrada")

    def eliminar_tarea(self, id_tarea:int):
        tarea = self.buscar_id(id_tarea)
        if tarea:
            self.tareas.remove(tarea) # remove() elimina el elemento que coincida con el argumento id_tarea en la lista
        else:
            print("Tarea no encontrada")
    def guardar_datos(self , archivo:str):
        datos = []
        for tarea in self.tareas:
            datos.append({"id":tarea.id, "titulo":tarea.titulo, "descripcion":tarea.descripcion, "estado":tarea.estado})
        with open(archivo, "w") as file:
            json.dump(datos, file, indent=4)

    def cargar_tareas(self, archivo:str):
        try:
            with open(archivo, "r") as file:
                datos = json.load(file)
                for tarea in datos:
                    '''todo este bloque formatea el codigo para que se pueda cargar en el programa'''
                    nueva_tarea = Tarea(tarea["titulo"], tarea["descripcion"])
                    nueva_tarea.id = tarea["id"]
                    nueva_tarea.estado = tarea["estado"]
                    self.tareas.append(nueva_tarea)
        except:
            print("No se encontraron tareas guardadas")
