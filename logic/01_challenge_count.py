"""
¿Está en Equilibrio la Alianza entre Reed Richards y Johnny Storm?

En el universo de los 4 Fantásticos, la unión y el equilibrio entre los poderes es fundamental para enfrentar cualquier desafío. En este problema, nos centraremos en dos de sus miembros:

Reed Richards (Mr. Fantastic), representado por la letra R.
Johnny Storm (La Antorcha Humana), representado por la letra J.

Objetivo:

Crea una función en Python que reciba una cadena de texto. Esta función debe contar cuántas veces aparece la letra R (para Reed Richards) y cuántas veces aparece la letra J (para Johnny Storm) en la cadena.

- Si la cantidad de R y la cantidad de J son iguales, se considera que la alianza entre la mente y el fuego está en equilibrio y la función debe retornar True.
- Si las cantidades no son iguales, la función debe retornar False.
- En el caso de que no aparezca ninguna de las dos letras en la cadena, se entiende que el equilibrio se mantiene (0 = 0), por lo que la función debe retornar True.
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
