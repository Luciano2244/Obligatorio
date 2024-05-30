from datetime import datetime
import os
import time

class Policlínica: 

    def __init__(self):
        self.especialidades = {}
        self.medicos = {}
        self.socios = {}
        self.consultas = []

    def alta_especialidad(self):
        while True:
            try:
                nombre = input("Ingrese el nombre de la especialidad: ")
                if nombre.isdigit():
                    print("El nombre de la especialidad es incorrecto, ingréselo nuevamente.")
                    continue

                precio = float(input("Ingrese el precio asociado: "))
                if precio <= 0:
                    print("El precio de la especialidad es incorrecto, ingréselo nuevamente.")
                    continue

                self.especialidades[nombre] = precio
                print("La especialidad se ha creado con éxito.")
                time.sleep(2)
                break
            except ValueError:
                print("El precio de la especialidad es incorrecto, ingréselo nuevamente.")

    def alta_socio(self):
        while True:
            try:
                nombre = input("Ingrese el nombre: ")
                if not nombre.isalpha():
                    print("No es un nombre válido, ingréselo de nuevo.")
                    continue

                apellido = input("Ingrese el apellido: ")
                if not apellido.isalpha():
                    print("No es un apellido válido, ingréselo de nuevo.")
                    continue

                cedula = input("Ingrese la cédula de identidad (8 dígitos, sin puntos ni guiones): ")
                if not cedula.isdigit() or len(cedula) != 8:
                    print("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")
                    continue

                fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
                fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")

                fecha_ingreso = input("Ingrese la fecha de ingreso (YYYY-MM-DD): ")
                fecha_ingreso = datetime.strptime(fecha_ingreso, "%Y-%m-%d")

                celular = input("Ingrese el número de celular (9 dígitos, sin espacio): ")
                if not celular.isdigit() or len(celular) != 9 or not celular.startswith("09"):
                    print("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX.")
                    continue

                tipo = input("Ingrese el tipo de socio (1- Bonificado, 2- No bonificado): ")
                if tipo not in ["1", "2"]:
                    print("El valor ingresado no es correcto, elige la opción 1 o 2.")
                    continue
                tipo = "Bonificado" if tipo == "1" else "No bonificado"

                self.socios[cedula] = {
                    "nombre": nombre, 
                    "apellido": apellido,
                    "fecha_nacimiento": fecha_nacimiento,
                    "fecha_ingreso": fecha_ingreso,
                    "celular": celular,
                    "tipo": tipo,
                    "deuda": 0   
                }
                print("El socio se ha creado con éxito.")
                time.sleep(2)
                break
            except ValueError:
                print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")

    def alta_medico(self):
        while True:
            try:
                nombre = input("Ingrese el nombre: ")
                if not nombre.isalpha():
                    print("No es un nombre válido, ingréselo de nuevo.")
                    continue

                apellido = input("Ingrese el apellido: ")
                if not apellido.isalpha():
                    print("No es un apellido válido, ingréselo de nuevo.")
                    continue

                cedula = input("Ingrese la cédula de identidad (8 dígitos, sin puntos ni guiones): ")
                if not cedula.isdigit() or len(cedula) != 8:
                    print("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")
                    continue

                fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
                fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")

                fecha_ingreso = input("Ingrese la fecha de ingreso (YYYY-MM-DD): ")
                fecha_ingreso = datetime.strptime(fecha_ingreso, "%Y-%m-%d")

                celular = input("Ingrese el número de celular (9 dígitos, sin espacio): ")
                if not celular.isdigit() or len(celular) != 9 or not celular.startswith("09"):
                    print("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX.")
                    continue

                especialidad = input("Ingrese la especialidad: ")
                if especialidad not in self.especialidades:
                    print("La especialidad no está dada de alta.")
                    opcion = input("¿Desea dar de alta esta especialidad? (s/n): ")
                    if opcion.lower() == "s":
                        self.alta_especialidad()
                        especialidad = input("Ingrese la especialidad: ")
                    else:
                        continue

                self.medicos[cedula] = {
                    "nombre": nombre,
                    "apellido": apellido,
                    "fecha_nacimiento": fecha_nacimiento,
                    "fecha_ingreso": fecha_ingreso,
                    "celular": celular,
                    "especialidad": especialidad
                }
                print("El médico se ha creado con éxito.")
                time.sleep(2)
                break
            except ValueError:
                print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")

    def alta_consulta_medica(self):
        while True:
            especialidad = input("Ingrese la especialidad: ")
            if especialidad not in self.especialidades:
                print("La especialidad no está dada de alta.")
                opcion = input("¿Desea dar de alta esta especialidad? (s/n): ")
                if opcion.lower() == "s":
                    self.alta_especialidad()
                    especialidad = input("Ingrese la especialidad: ")
                else:
                    break

            medico_nombre = input("Ingrese el nombre del médico: ")
            encontrado = False
            for medico in self.medicos.values():
                if medico["nombre"] == medico_nombre:
                    encontrado = True
                    break
            if not encontrado:
                print("Este médico no está dado de alta.")
                opcion = input("¿Desea dar de alta este médico? (s/n): ")
                if opcion.lower() == "s":
                    self.alta_medico()
                    medico_nombre = input("Ingrese el nombre del médico: ")
                else:
                    break

            try:
                fecha = input("Ingrese la fecha de la consulta (YYYY-MM-DD): ")
                fecha = datetime.strptime(fecha, "%Y-%m-%d")
                cantidad_pacientes = int(input("Ingrese la cantidad de pacientes que se atenderán: "))
                self.consultas.append({
                    "especialidad": especialidad,
                    "medico": medico_nombre,
                    "fecha": fecha,
                    "cantidad_pacientes": cantidad_pacientes
                })
                print("La consulta se ha creado con éxito.")
                break
            except ValueError:
                print("Por favor, ingrese los datos correctamente.")

    def emitir_ticket_consulta(self):
        especialidad = input("Ingrese la especialidad: ")
        if especialidad not in self.especialidades:
            print("La especialidad no está dada de alta.")
            opcion = input("¿Desea dar de alta esta especialidad? (s/n): ")
            if opcion.lower() == "s":
                self.alta_especialidad()
            return
        
        consultas_especialidad = [c for c in self.consultas if c["especialidad"] == especialidad]
        if not consultas_especialidad:
            print("No hay consultas disponibles para esta especialidad.")
            return

        print(f"Consultas disponibles para la especialidad {especialidad}:")
        for i, consulta in enumerate(consultas_especialidad, 1):
            print(f"{i}. Médico: {consulta['medico']}, Fecha: {consulta['fecha'].date()}")

        while True:
            try:
                opcion = int(input("Seleccione el número de atención deseado: "))
                if 1 <= opcion <= len(consultas_especialidad):
                    consulta_seleccionada = consultas_especialidad[opcion - 1]
                    print(f"Ha seleccionado la consulta del médico {consulta_seleccionada['medico']} el {consulta_seleccionada['fecha'].date()}.")
                    break
                else:
                    print(f"La opción ingresada no es válida. Debe ser un número entre 1 y {len(consultas_especialidad)}.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def menu_principal(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("""\nMenú principal:

            1. Dar de alta una especialidad
            2. Dar de alta un socio
            3. Dar de alta un médico
            4. Dar de alta una consulta médica
            5. Emitir un ticket de consulta
            6. Salir del programa""")

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
                break
            else:
                print("Opción no válida. Por favor, ingrese una opción del 1 al 6.")

if __name__ == "__main__":
    policlinica = Policlínica()
    policlinica.menu_principal()
