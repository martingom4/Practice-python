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
