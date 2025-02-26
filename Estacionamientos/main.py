from logic.estacionamiento import Estacionamiento
def main():
    estacionamiento = Estacionamiento(5).definir_espacios()
    print("Bienvenido al estacionamiento de carros")
    print("Estos son los espacios disponibles")
    print(estacionamiento)

    agregar = Estacionamiento.agregar_carro(estacionamiento,1,'carro1','1234')
    print(agregar)
    print(Estacionamiento.ver_estado(agregar))
    

if __name__ == "__main__":
    main()
