from datetime import datetime

class Socio:
    def __init__(self, nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular, tipo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        self.__fecha_ingreso = datetime.strptime(fecha_ingreso, "%Y-%m-%d")
        self.__celular = celular
        self.__tipo = tipo
        self.__deuda = 0

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def cedula(self):
        return self.__cedula

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

    @property
    def fecha_ingreso(self):
        return self.__fecha_ingreso

    @property
    def celular(self):
        return self.__celular
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def deuda(self):
        return self.__deuda
    
    @deuda.setter
    def deuda(self, nuevo_valor):
        self.__deuda += nuevo_valor

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    
