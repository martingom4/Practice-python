'''
vale la logica es que tengo que sumar los dos strings. Como asi? tengo dos arreglos tengo que comparar los dos indices y sumarlos, si la suma es mayor a 10 tengo que llevarme el 1 al siguiente indice y asi sucesivamente.
'''


l1 = [2, 4, 3]
l2 = [2, 6, 3]

carry = 0
result = []

# Recorremos los índices de derecha a izquierda
for i in range(len(l1) - 1, -1, -1):
    total = l1[i] + l2[i] + carry
    digit = total % 10      # Dígito que se queda en la posición actual
    carry = total // 10     # Acarreo que se llevará a la siguiente suma
    result.insert(0, digit) # Insertamos el dígito al inicio del resultado

# Si al final todavía hay un acarreo, lo agregamos al inicio
if carry:
    result.insert(0, carry)

print(result)  # Esto mostrará [4, 0, 6]
