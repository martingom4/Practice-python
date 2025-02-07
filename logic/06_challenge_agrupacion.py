"""


### Desafío: Reorganización de Datos por Categoría

**Enunciado:**

Tienes un diccionario en el que las claves son nombres de personas y los valores son sus edades. Tu reto es escribir una función en Python que reciba este diccionario y devuelva un nuevo diccionario donde las claves sean las edades y los valores sean listas de nombres de las personas que tienen esa edad.

La función debería retornar:

```python
{
    25: ["Ana", "María"],
    30: ["Luis", "Pedro", "Lucía"],
    40: ["Jorge"]
}
```

**Requisitos:**

1. La función debe funcionar para cualquier diccionario con el formato (clave: nombre, valor: edad).
2. Debes utilizar diccionarios y listas para agrupar correctamente los nombres según su edad.
3. Considera usar métodos de diccionarios como `get()` para facilitar la actualización del nuevo diccionario sin errores.

**Pista:**

- Recorre cada par clave-valor en el diccionario original.
- Para cada edad, verifica si ya existe como clave en el nuevo diccionario. Si no existe, inicializa esa clave con una lista vacía.
- Agrega el nombre correspondiente a la lista asociada a la edad.

"""
from collections import defaultdict

personas = {
    "Ana": 25,
    "Luis": 30,
    "María": 25,
    "Pedro": 30,
    "Jorge": 40,
    "Lucía": 30
}


def agrupacion(diccionario):
    edades = defaultdict(list) #creo un diccionario vacio con listas
    for nombre, edad in diccionario.items(): #se iteran los elementos del diccionario
        edades[edad].append(nombre)#se agrega el nombre a la lista de edades
    print(f"edad:\n{dict(edades)}")#se imprime el diccionario


agrupacion(personas)
