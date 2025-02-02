#aca vamos a tener la clase de una tarea
#esto nos va a permitir crear una tarea con un nombre, descripcion, estado e id y guardarlo solo en un arreglo de tareas
class TaskManager:
    def __init__(self):
        self.tasks = []

    def addTask(self,task):
        self.tasks.append(task)

    def getTask(self):
        return self.tasks

    def remove_task(self,task):
        self.tasks.remove(task)


