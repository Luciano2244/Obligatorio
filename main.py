
from entities.especialidad import Especialidad
from entities.socio import Socio
from entities.medico import Medico
from entities.consulta_medica import Consulta_medica
from datetime import datetime
import os

class Policlinica:
    def __init__(self):
        self.especialidades = []
        self.socios = []
        self.medicos = []
        self.consultas = []

    def alta_especialidad(self):
        nombre = input("Ingrese el nombre de la especialidad: ")
        precio_fijo = input("Ingrese el precio asociado: ")
        while True:
            try:
                precio_fijo = float(precio_fijo)
                if not nombre.strip().isalpha():  # Verifica si el nombre contiene solo letras     #strip() elimina los espacios en blanco al principio y al final. .isalpha devuelve True si todos los caracteres en la cadena son letras del alfabeto                                                     # isinstance checks if object belongs to a particular type
                    raise TypeError
                elif precio_fijo <= 0:
                    raise ValueError
                else:
                    especialidad_nueva = Especialidad(nombre, precio_fijo)
                    self.especialidades.append(especialidad_nueva)
                    print("La especialidad se a creado con éxito!")
                    break
            except TypeError:
                nombre = input("El nombre de la especialidad es incorrecto, ingréselo nuevamente: ")
            except ValueError:
                precio_fijo = input("El precio de la especialidad es incorrecto, ingréselo nuevamente: ")

    def alta_socio(self):
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        cedula = input("Ingrese la cédula de identidad: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento en formato aaaa-mm-dd: ")
        fecha_ingreso = input("Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd: ")
        celular = input("Ingrese el número de celular: ")
        tipo = input("Ingrese el tipo de socio: 1- Bonificado 2- No bonificado ")
        while True:
            try:
                if not nombre.strip().isalpha():                                                        # isinstance checks if object belongs to a particular type
                    raise TypeError
                else:
                    break
            except TypeError:
                nombre = input("No es un nombre válido, ingréselo de nuevo: ")
        
        while True:
            try:
                if not apellido.strip().isalpha():                                                         # isinstance checks if object belongs to a particular type
                    raise TypeError
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
                if len(str(celular)) != 8 and str(celular)[0:] != "09":
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
        
        socio_nuevo = Socio(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular, tipo)
        self.socios.append(socio_nuevo)
        print("El socio se a creado con éxito!")
            
    def alta_medico(self):
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        cedula = input("Ingrese la cédula de identidad: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento en formato aaaa-mm-dd: ")
        fecha_ingreso = input("Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd: ")
        celular = input("Ingrese el número de celular: ")
        especialidad = input("Ingrese la especialidad: ")
        while True:
            try:
                if not nombre.strip().isalpha():                                                        # isinstance checks if object belongs to a particular type
                    raise TypeError
                else:
                    break
            except TypeError:
                nombre = input("No es un nombre válido, ingréselo de nuevo: ")
        
        while True:
            try:
                if not apellido.strip().isalpha():                                                         # isinstance checks if object belongs to a particular type
                    raise TypeError
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
                if len(str(celular)) != 8 and str(celular)[0:] != "09":
                    celular = int(input("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX: "))
                else:
                    break
            except ValueError:
                celular = input("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX: ")

        while True:
            try:                                                                                          # try If an exception occurs during the execution of the try block, Python raises that exception. Searches for the exception and executes code inside the block
                if not especialidad.strip().isalpha():                                                        # isinstance checks if object belongs to a particular type
                    raise TypeError
                else:
                    break
            except TypeError:
                especialidad = input("La especialidad debe ser un string: ")

        while True:
            try:
                if especialidad not in self.especialidades:
                    print("""\nEsta especialidad no está dada de alta elija una opción::

                1- Volver a ingresar la especialidad
                2- Dar de alta esta especialidad """)
                    opcion_especialidad = input("Opción: ")
                    if opcion_especialidad != "1" and opcion_especialidad != "2":
                        raise ValueError
                    elif opcion_especialidad == "1":
                        especialidad = input("Ingrese la especialidad: ")
                    elif opcion_especialidad == "2":
                        self.alta_especialidad()
                else:
                    break
            except ValueError:
                opcion_especialidad = input("La opción seleccionada no es correcta, vuelva a intentar con otra opción: ")
        
        medico_nuevo = Medico(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular, especialidad)
        self.medicos.append(medico_nuevo)
        print("El medico se a creado con éxito!")

    def alta_consulta_medica(self):
        especialidad = input("Ingrese la especialidad: ")
        nombre_medico = input("Ingrese el nombre del médico: ")
        fecha_consulta = input("Ingrese la fecha de consulta: ")
        cantidad_pacientes_atenderan = input("Ingrese la cantidad de pacientes que se atenderán: ") 
        while True:
            try:                                                                                          # try If an exception occurs during the execution of the try block, Python raises that exception. Searches for the exception and executes code inside the block
                if not especialidad.strip().isalpha():                                                        # isinstance checks if object belongs to a particular type
                    raise TypeError
                else:
                    break
            except TypeError:
                especialidad = input("La especialidad debe ser un string: ")

        while True:
            try:
                if especialidad not in self.especialidades:
                    print("""\nEsta especialidad no está dada de alta elija una opción::

                1- Volver a ingresar la especialidad
                2- Dar de alta esta especialidad """)
                    opcion_especialidad = input("Opción: ")
                    if opcion_especialidad != "1" and opcion_especialidad != "2":
                        raise ValueError
                    elif opcion_especialidad == "1":
                        especialidad = input("Ingrese la especialidad: ")
                    elif opcion_especialidad == "2":
                        self.alta_especialidad()
                else:
                    break
            except ValueError:
                opcion_especialidad = input("La opción seleccionada no es correcta, vuelva a intentar con otra opción: ")

        while True:
            try:
                if not nombre_medico.strip().isalpha():                                                        # isinstance checks if object belongs to a particular type
                    raise TypeError
                else:
                    break
            except TypeError:
                nombre_medico = input("No es un nombre válido, ingréselo de nuevo: ")

        while True:
            try:
                if nombre_medico not in self.medicos:
                    print("""\nEste médico no está dada de alta elija una opción::

                1- Volver a ingresar el médico
                2- Dar de alta el médico """)
                    opcion_medico = input("Opción: ")
                    if opcion_medico != "1" and opcion_medico != "2":
                        raise ValueError
                    elif opcion_medico == "1":
                        nombre_medico = input("Ingrese el médico: ")
                    elif opcion_medico == "2":
                        self.alta_medico()
                else:
                    break
            except ValueError:
                opcion_medico = input("La opción seleccionada no es correcta, vuelva a intentar con otra opción: ")

        while True:
            try:
                fecha_consulta = datetime.strptime(fecha_consulta, "%Y-%m-%d")
                if not isinstance(fecha_consulta, datetime):
                    fecha_consulta = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd: ")
                else:
                    break
            except ValueError:
                fecha_consulta = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd: ")

        while True:
            try:
                cantidad_pacientes_atenderan = int(cantidad_pacientes_atenderan)
                if cantidad_pacientes_atenderan <= 0:
                    cantidad_pacientes_atenderan = int(input("No es una cantidad válida, ingrese nuevamente: "))
                else:
                    break
            except ValueError:
                cantidad_pacientes_atenderan = input("No es una cantidad válida, ingrese nuevamente: ")

        consulta_medica_nueva = Consulta_medica(especialidad, nombre_medico, fecha_consulta, cantidad_pacientes_atenderan)
        self.consultas.append(consulta_medica_nueva)
        print("La consulta se a creado con éxito!")

        


    


                
        

            



    def menu_principal(self):
        while True:
                os.system("cls") #funcion para limpiar pantalla
                print("""\nMenú principal:

                1. Dar de alta una especialidad
                2. Dar de alta un socio
                3. Dar de alta un médico
                4. Dar de alta una consulta médica
                5. Emitir un ticket de consulta
                6. Realizar consultas
                7. Salir del programa""")

                opcion = input("Opción: ")
                if opcion == "1":
                    self.alta_especialidad()
                elif opcion == "2":
                    self.alta_socio()
                elif opcion == "3":
                    self.alta_medico()
                elif opcion == "4":
                    self.alta_consulta_medica()
                elif opcion == "5":
                    self.emitir_ticket_consulta()
                elif opcion == "6":
                    self.realizar_consulta()
                elif opcion == "7":
                    print("Saliendo del programa...")
                    break
                else:
                    print("La opción seleccionada no es correcta, vuelva a intentar con otra opción: ")

if __name__ == "__main__":
    programa = Policlinica()  # Instanciar un objeto de la clase Policlinica
    programa.menu_principal()
