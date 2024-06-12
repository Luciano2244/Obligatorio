from entities.persona import Persona
from datetime import datetime

class Socio(Persona):
    def __init__(self, nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular, tipo):              #deuda no se agrega como atributo porque empieza en 0 para todos
        super().__init__(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular)             #super().__init__  Usa los atributos de la clase puesta adentro de () mas arriba (esto se llama herencia)
        self.__deuda = 0
        
    @property
    def deuda(self):
        return self.__deuda
    
    @property
    def tipo(self):
        return self.__tipo


