#aca vamos a crear algunos paquetes estandares

class PaqueteFactory:
    @staticmethod
    def crear_paquete(tipo):
        if tipo == "pequeño":
            return {"descripcion": "Paquete pequeño", "peso": 1.0, "estado": "pendiente"}
        elif tipo == 'mediano':
            return {"descripcion": "Paquete mediando", "peso": 6, "estado": "pendiente"}
        elif tipo == 'grande':
            return {"descripcion": "Paquete grande", "peso": 12, "estado": "pendiente"}
        else:
            raise ValueError("Tipo de paquete no valido")

        
