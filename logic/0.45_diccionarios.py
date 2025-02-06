prueba = {
  "nombre": "Martin",
  "edad": "20",
  "trabaja":False,
  "salario":[300,300,300,300]
}
#quiero saber cuanto ha ganado martin con su salario en 3 meses
meses_disponibles = len(prueba["salario"])
target = 3 # los meses que quiero verificar
salarios_3_meses = sum(prueba["salario"][:target])
print(f"el salario de los tres meses es:", salarios_3_meses)



#ahora quiero hacer esto en funcion

def calculate_salary(salario: list, target: int) -> int:
    # vamos a recibir una lista que es el salarios y vamos a hacer el calculo segun el target que el usuario solicite
    #vamos a verificar cuantos meses tenemos disponibles
    len(salario) # esto devolvera un int
    calculo_salario = sum(salario[:target])
    print(f"el salario que se calculo es {calculo_salario}")

meses = prueba["salario"]
goal = 3

calculate_salary(meses,goal)
