from persona import Persona
from datetime import datetime

class Socio(Persona):
    def __init__(self, nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular, tipo):              #deuda no se agrega como atributo porque empieza en 0 para todos
        super().__init__(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular)             #super().__init__  Usa los atributos de la clase puesta adentro de () mas arriba (esto se llama herencia)
        self.__deuda = 0
        
        while True:
            try:
                if not isinstance(nombre, str):                                                          # isinstance checks if object belongs to a particular type
                    nombre = input("No es un nombre válido, ingréselo de nuevo: ")
                else:
                    break
            except TypeError:
                nombre = input("No es un nombre válido, ingréselo de nuevo: ")

        while True:
            try:
                if not isinstance(apellido, str):                                                          # isinstance checks if object belongs to a particular type
                    apellido = input("No es un apellido válido, ingréselo de nuevo: ")
                else:
                    break
            except TypeError:
                apellido = input("No es un apellido válido, ingréselo de nuevo: ")

        while True:
            try:
                cedula = int(cedula)
                if len(str(cedula)) != 8:
                    cedula = int(input("No es una cedula válida, ingrese nuevamente una cédula de 8 digitos: "))
                else:
                    break
            except ValueError:
                cedula = input("No es una cedula válida, ingrese nuevamente una cédula de 8 digitos: ")

        while True:
            try:
                fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")                                    #datetime importado, .strptime es una funcion que pasa el string de fecha de nacimiento a el tipo de datetime. Si cumple con el formato de %Y-%m-%d hace break.
                if not isinstance(fecha_nacimiento, datetime):
                    fecha_nacimiento = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd: ")
                else:
                    break
            except ValueError:
                fecha_nacimiento = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd: ")

        while True:
            try:
                fecha_ingreso = datetime.strptime(fecha_ingreso, "%Y-%m-%d")
                if not isinstance(fecha_ingreso, datetime):
                    fecha_ingreso = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd: ")
                else:
                    break
            except ValueError:
                fecha_ingreso = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd: ")
        
        while True:
            try:
                celular = int(celular)
                if len(str(celular)) != 9 or str(celular)[:2] != "09":
                    celular = int(input("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX: "))
                else:
                    break
            except ValueError:
                celular = input("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX: ")

        while True:
            try:                                                                                          # try If an exception occurs during the execution of the try block, Python raises that exception. Searches for the exception and executes code inside the block
                tipo = int(tipo)
                if tipo != 1 and tipo != 2:
                    tipo = int(input("El valor ingresado no es correcto, elige la opción 1 o 2: "))
                else:
                    break
            except ValueError:                                                                           #ValueError: Si el usuario ingresa un valor no numérico.
                tipo = input("El valor ingresado no es correcto, elige la opción 1 o 2: ")
        self.__tipo = tipo


    
    @property
    def deuda(self):
        return self.__deuda
    
    @property
    def tipo(self):
        return self.__tipo

socio1 = Socio("juan", "Belgeri", 12348, "2000-01-01", "2004-04-12", 12348, 1)
