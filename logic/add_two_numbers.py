'''
vale la logica es que tengo que sumar los dos strings. Como asi? tengo dos arreglos tengo que comparar los dos indices y sumarlos, si la suma es mayor a 10 tengo que llevarme el 1 al siguiente indice y asi sucesivamente.
'''


list1 = [2,4,3]
list2 = [2,6,3]

rev1 = reversed(list1)
rev2 = reversed(list2)

reversed(list1) #
carry = 0
result = []
for i in range(len(rev1)):
    if rev1[i] + rev2[i] >= 10:
        sum = rev1[i] + rev2[i] + carry
        result[i] = carry % sum
        carry = sum // 10 #1
        print(result)
        print(carry)

    else:
        rev1[i] = rev1[i] + rev2[i]
        print(rev1)
