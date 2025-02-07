"""

**Problema: El misterio del tesoro escondido**

Imagina que has encontrado un antiguo mapa del tesoro, pero la información está dividida en varias pistas. Estas pistas están almacenadas en un diccionario llamado `pistas`, donde cada clave es un número que indica el orden correcto en el que debe leerse la pista, y cada valor es una cadena de texto con la pista en sí.


**Tu tarea es la siguiente:**

1. **Ordenar las pistas:** Reorganiza el diccionario según las claves (de menor a mayor) para obtener el orden correcto de las pistas.

2. **Extraer pistas clave:** Recorre el diccionario ordenado y extrae la primera letra de cada cadena de pista.

3. **Formar la palabra secreta:** Concatena todas las letras extraídas para formar una palabra secreta.

4. **Imprimir la solución:** Muestra en pantalla la palabra secreta resultante.

---

**Ejemplo con el diccionario anterior:**

- Claves ordenadas: 1, 2, 3, 4.
- Pistas en orden:
  - Clave 1: `"La primera pista comienza donde nace el río"` → Primera letra: `'L'`
  - Clave 2: `"Avanza con cuidado hacia la llanura"` → Primera letra: `'A'`
  - Clave 3: `"El camino se abre ante el valle"` → Primera letra: `'E'`
  - Clave 4: `"Busca donde el sol se oculta"` → Primera letra: `'B'`
- Palabra secreta resultante: `"LAEB"`

---

**Requerimientos:**

- Utiliza estructuras de datos y funciones propias de Python.
- No se permite modificar las pistas originales, solo trabajar sobre ellas para deducir la palabra secreta.
- Recuerda que el diccionario puede tener un número variable de pistas.

**Sugerencia de pasos a seguir en tu programa:**

1. Obtener una lista de las claves ordenadas usando la función `sorted()`.
2. Recorrer las claves ordenadas y, para cada una, extraer la primera letra de la pista correspondiente.
3. Concatenar las letras en una cadena.
4. Imprimir la cadena resultante.
"""

pistas = {
    4: "Busca donde el sol se oculta",
    1: "La primera pista comienza donde nace el río",
    3: "El camino se abre ante el valle",
    2: "Avanza con cuidado hacia la llanura"
}

def sorted_pista(diccionario):
    sorted_dic = sorted(diccionario)
    palabra_secreta = ""#aca se guardara la palabra decodificada
    for clave in sorted_dic:
        palabra_secreta += diccionario[clave][0]
    print(f"La palabra secreta es: {palabra_secreta}")

def other_method(diccionario):
    sorted_dic = sorted(diccionario)
    palabra_secreta = "".join([diccionario[clave][0] for clave in sorted_dic])
    print(palabra_secreta)
sorted_pista(pistas)
other_method(pistas)
