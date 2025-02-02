import jwt
import datetime
from flask import current_app # current_app es un objeto que representa la aplicación Flask actual y se puede usar para acceder a la configuración de la aplicación, a los registros y a otros objetos.

class JWTmanager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.secret_key = None # La clave secreta que se usará para firmar el token
        return cls._instance

    def secret_key(self, secretkey):
        self.secret_key = secretkey # Asignamos la clave secreta que se usará para firmar el token

    def create_token(self, data, expires_in = 3600): #funcion para crear el jwt token con la data que se le pase y el tiempo de expiracion del token

        if not self.secret_key:
            raise Exception("Secret key not set") # Si no se ha asignado una clave secreta, lanzamos una excepción

        pyload = {
            "data": data,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_in)
        } # Creamos el payload del token, que contendrá la información que queremos que lleve el token y la fecha de expiración
        return jwt.encode(pyload, self.secret_key, algorithm="HS256") # Devolvemos el token firmado con la clave secreta asignada

    def decode_token(self, token):
        if not self.secret:
            raise ValueError("El secreto no está inicializado")
        try:
            return jwt.decode(token, self.secret, algorithms=["HS256"]) # Decodificamos el token con la clave secreta asignada y el algoritmo HS256
        except jwt.ExpiredSignatureError:# Excepción que se lanza cuando el token ha expirado
            raise ValueError("El token ha expirado")
        except jwt.InvalidTokenError:# Excepción que se lanza cuando el token no es válido por alguna razón
            raise ValueError("El token no es válido")


jwt1_manager = JWTmanager() # Creamos una instancia de la clase JWTmanager
