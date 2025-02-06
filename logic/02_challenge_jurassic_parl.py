"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""

# Para ver si un número es par
# siempre usamos el módulo %
# nos da el resto de la división: eggs % 2 == 2

def count_carnivore_dinosaurs_eggs(egg_list)->int:
    """
    Esta funcion recibe una lista de numeros enteros que representan la catidad de huevos que han puesto los diferentes dinosourios
    en el parque jurasico y los de numero par son de carnivoros
    """
    total_canivore_eggs = 0
    for eggs in egg_list:
        if eggs % 2 == 0:
            total_canivore_eggs += eggs

    return total_canivore_eggs

egg_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(count_carnivore_dinosaurs_eggs(egg_list)) # 30
