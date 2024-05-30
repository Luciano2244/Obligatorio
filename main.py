from entities.medico import Medico
from entities.especialidad import Especialidad
from datetime import datetime
import os

class Policlinica:
    def __init__(self):
        self.especialidades = []
        self.medicos = []
        self.socios = []
        self.consultas = []

    def alta_especialidad(self):
        nombre = input("Ingrese el nombre de la especialidad: ")
        precio_fijo = input("Ingrese el precio asociado: ")
        while True:
            try:
                precio_fijo = float(precio_fijo)
                if not nombre.strip().isalpha():  # Verifica si el nombre contiene solo letras                                                          # isinstance checks if object belongs to a particular type
                    raise TypeError
                elif precio_fijo <= 0:
                    raise ValueError
                else:
                    especialidad_nueva = Especialidad(nombre, precio_fijo)
                    self.especialidades.append(especialidad_nueva)
                    print("La especialidad se a creado con éxito")
                    break
            except TypeError:
                nombre = input("El nombre de la especialidad es incorrecto, ingréselo nuevamente: ")
            except ValueError:
                precio_fijo = input("El precio de la especialidad es incorrecto, ingréselo nuevamente: ")

    def alta_socio(self):
        

            



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
