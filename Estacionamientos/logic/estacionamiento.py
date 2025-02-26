'''
voy hacer un estacionamiento de carros en python, todo sera por consola inicialmente


tendre un estacionamiento que sera una lista de espacios de estacionamiento que seran listas de dos elemenos
el primer elemento sera el numero de espacio y el segundo sera el estado del espacio, si esta ocupado o no

tendre una funcion que permita agregar un carro al estacionmiento y otra que permita sacar un carro del estacionamiento
tendre una funcion que permita poner el nombre y la placa del carro en el espacio de estacionamiento
tendre una funcion que permita ver el estado del estacionamiento
tendre una funcion que permita ver el estado de un espacio en especifico
tengo que imprimir mensajes de error si el espacio esta ocupado o si el espacio no existe
'''

class Estacionamiento:
    def __init__(self, espacios):
        self.espacios = []
        for i in range(espacios):
            self.espacios.append([i+ 1 , 'libre'])
    def definir_espacios(self):
        return self.espacios

    def agregar_carro(self,espacio,nombre,placa):
        espacio = espacio -1 # para que el espacio sea el correcto porque la lista empieza en 0 pero los espacios en 1
        for i in range(len(self.espacios)): # aca lo tengo que obtener es los atributos de la lista de espacios y no la lista de espacios
            if self.espacios[espacio][i] == 'libre':
                self.espacios[espacio][i] = 'ocupado'
                self.espacios[espacio].append(nombre)
                self.espacios[espacio].append(placa)
                return self.espacios
            else:
                return "El espacio ya esta ocupado"
        else:
            return "El espacio no existe"
    def sacar_carro(self,espacio):
        espacio = espacio -1
        if espacio < len(self.espacios):
            if self.espacios[espacio][1] == 'ocupado':
                self.espacios[espacio][1] = 'libre'
                self.espacios[espacio].pop()
                self.espacios[espacio].pop()
                return self.espacios
            else:
                return "El espacio ya esta libre"
        else:
            return "El espacio no existe"
    def ver_estado(self):
        return self.espacios
    def ver_estado_espacio(self,espacio):
        espacio = espacio -1
        if espacio < len(self.espacios):
            return self.espacios[espacio]
        else:
            return "El espacio no existe"



