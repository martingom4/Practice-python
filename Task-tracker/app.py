# Flujo principal de la aplicación
from Factory.Agregar import Agregar
from Factory.Actualizar import Update
from Factory.Eliminar import Eliminar
from Factory.task_manager import TaskManager

def main():
    print("Bienvenido a Task-tracker")
    task_manager = TaskManager()
    while True:
        print("1. Agregar tarea")
        print("2. Actualizar tarea")
        print("3. Eliminar tarea")
        print("4. Salir")
        option = int(input("Ingrese la opcion que desea realizar: "))
        if option == 1:
            agregar = Agregar(task_manager)
            agregar.addTask()
        elif option == 2:
            update = Update(task_manager)
            update.updateTask()
        elif option == 3:
            delete = Eliminar(task_manager)
            delete.deleteTask()
        elif option == 4:
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    main()
