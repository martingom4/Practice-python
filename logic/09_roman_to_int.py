#tengo que convertir un numero romano a numero enter

#que es lo que pense es hacer un diccionario con los valores de los numeros romanos y luego recorrer el string y sumar los valores de los numeros romanos

def roman_to_int(roman:str) -> int:
    roman_values = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    int_value = 0 # primer valor lo inicializamos en 0
    for i in range(len(roman)): #leemos entre al diccionario de los valores de los numeros romanos
        if i > 0 and roman_values[roman[i]] > roman_values[roman[i-1]]: #i-1??
            int_value += roman_values[roman[i]] - 2 * roman_values[roman[i-1]]
        else:
            int_value += roman_values[roman[i]]
    return int_value


'''
roman: es el valor que ingresa el usuario
despues hacemos la condicion para saber si el valor de la letra actual es mayor que el valor de la letra anterior
si es asi, restamos el valor de la letra actual menos el doble del valor de la letra anterior
si no, sumamos el valor de la letra actual

para verlo de manera mas grafica:
    si el valor de la letra actual es mayor que el valor de la letra anterior
    sumamos el valor de la letra actual menos el doble del valor de la letra anterior
    si no
    sumamos el valor de la letra actual

'''
