#aca vamos a poder actualizar el estado de una tarea
from Factory.task_manager import TaskManager
from Factory.task import Task

class Update:
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def updateTask(self):
        id = int(input("Ingrese el id de la tarea que desea actualizar: "))
        for task in self.tasks:
            if Task.getId(task) == id:
                status = input("Ingrese el nuevo estado de la tarea")
                Task.setStatus(task, status)
                print("Tarea actualizada con exito")
                print(task)
            else:
                print("No se encontro la tarea")
                break



