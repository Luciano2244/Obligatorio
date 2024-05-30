class Especialidad:
    def __init__(self, nombre, precio_fijo):
        self.__nombre = nombre
        self.__precio_fijo = precio_fijo

    @property
    def nombre(self):
        return self.__nombre
     
    @property
    def precio_fijo(self):
        return self.__precio_fijo
    


