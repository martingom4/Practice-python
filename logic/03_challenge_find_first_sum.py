"""
    dado un array de numeros y un numero objetivo, encontrar los indices de los dos numeros que suman el numero objetivo
    y devuelve sus indices. Si no existe tal combinacion, devuelve None

    nums = [4,6,6,2]
    target = 8
"""
#bloque anidado de for esto se puede mejorar con un diccionario
def find_sum(nums:int, target:int) -> list:
    if len(nums) == 0: return None
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return[i,j]
    return None


nums = [4,5,6,2]
goal = 8

print(find_sum(nums,goal))
