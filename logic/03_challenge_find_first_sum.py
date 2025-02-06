"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

#bloque anidado de for esto se puede mejorar con un diccionario
def find_sum(nums:int, target:int) -> list:
    if len(nums) == 0: return None
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return[i,j]
    return None

def find_sum_diccionary(nums, target):
    seen = {}#diccionario para guardar el numero e indice
    for index, value in enumerate(nums):
        missing = target - value
        if missing in seen:return [seen[missing],index]
        seen[value]= index  # esto es para guardar los valores vistos en el diccionario para que se pueda guardar y verificar
    return None

nums = [4,5,6,2]
target = 8
print(find_sum_diccionary(nums, target))
