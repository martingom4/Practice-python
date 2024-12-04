from models.tarea import Tarea
from models.gestor_tarea import gestorTarea

gestor = gestorTarea()

def main():
    print("Bienvenido a la lista de tareas")
    mantener = True
    while mantener:
        valor = int(input("1. Agregar tarea\n2. Ver tareas\n3. Completar tarea\n4. Eliminar tarea\n5. Guardar datos \n6. Cargar tareas\n7. Salir\n"))
        match valor:
            case 1:
                titulo = input("Ingrese el título de la tarea: ")
                descripcion = input("Ingrese la descripción de la tarea: ")
                gestor.agregarTarea(titulo, descripcion)
            case 2:
                gestor.listar_tareas()
            case 3:
                gestor.completar_tarea(int(input("Ingrese el id de la tarea a completar: ")))
            case 4:
                gestor.eliminar_tarea(int(input("Ingrese el id de la tarea que quiere eliminar:")))
            case 5:
                gestor.guardar_datos("to-do-list/tareas.json")
            case 6:
                gestor.cargar_tareas("to-do-list/tareas.json")
            case 7:
                mantener = False
            case _:
                print("Opción no válida")


if __name__ == "__main__":
    main()
