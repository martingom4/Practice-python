#aca vamos a poder actualizar el estado de una tarea
from Factory.task_manager import TaskManager
from Factory.task import Task

class Update:
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def updateTask(self):
        id = int(input("Ingrese el id de la tarea que desea actualizar: "))
        # Buscar tarea por ID
        
