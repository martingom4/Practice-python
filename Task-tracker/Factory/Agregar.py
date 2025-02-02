from Factory.task_manager import TaskManager
from Factory.task import Task

class Agregar:
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def addTask(self):
        name = input("Ingrese el nombre de la tarea: ")
        description = input("Ingrese la descripcion de la tarea: ")
        id = len(self.task_manager.get_tasks()) + 1
        task = Task(name, description, "Pendiente", id)
        self.task_manager.add_task(task)
        print("Tarea agregada con exito")
