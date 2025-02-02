# Aca vamos a poder eliminar una tarea de la lista

from Factory.task import Task

class Eliminar:
    def __init__(self):
        self.tasks = []

    def deleteTask(self):
        id = int(input("Ingrese el id de la tarea que desea eliminar: "))
        task_found = False
        for task in self.tasks:
            if task.getId() == id:
                self.tasks.remove(task)
                print("Tarea eliminada con exito")
                task_found = True
                break
        if not task_found:
            print("No se encontro la tarea")
