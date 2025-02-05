from Factory.task_manager import TaskManager
from Factory.task import Task

class Agregar:
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def addTask(self):
        name = input("Ingrese el nombre de la tarea: ")
        description = input("Ingrese la descripcion de la tarea: ")
        id = len(self.task_manager.getTask()) + 1  # Generar ID automáticamente
        task = Task(name, description, "Pendiente", id)
        self.task_manager.addTask(task)
        print("Tarea agregada con exito")
        
