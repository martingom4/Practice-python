"""
    crear una funcion que reciba una cadena de texto y contar cuantas veces aparaece cada letra en la cadena


"""

def check_is_balanced(text):
    text = text.upper()
    count_r = text.count('R') # cuanta la cantidad de veces que aparezca la R
    count_j = text.count('J') # cuanta la cantidad de veces que aparezca la J

    print(f"count_r: {count_r} count_j: {count_j}")
    return count_r == count_j # retorna True si la cantidad de R es igual a la cantidad de J

print(check_is_balanced("RRJJ")) # count_r: 1 count_j: 1
print(check_is_balanced("afdsafaafa")) # count_r: 2 count_j: 2
print(check_is_balanced("RRJJj")) # count_r: 1 count_j: 1
