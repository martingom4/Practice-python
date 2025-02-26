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
    int_value = 0
    for i in range(len(roman)):
        if i > 0 and roman_values[roman[i]] > roman_values[roman[i-1]]:
            int_value += roman_values[roman[i]] - 2 * roman_values[roman[i-1]]
        else:
            int_value += roman_values[roman[i]]
    return int_value

print(roman_to_int('III'))
print(roman_to_int('IV'))
print(roman_to_int('IX'))
print(roman_to_int('LVIII'))  
