from datetime import datetime
import os
import time
from Objetos.socio import Socio
from Objetos.medico import Medico

class Policlínica: 

    def __init__(self):
        self.especialidades = {}
        self.medicos = {}
        self.socios = {}
        self.consultas = []
        #INICIALIZAMOS LOS ARRAY DE LA POLICLINICA
    def alta_especialidad(self):
        while True:
            try:
                nombre = input("Ingrese el nombre de la especialidad: ")
                if nombre.isdigit() or nombre == " ":
                    #VEFICA SI ES DE SOLO NUMEROS EL STRING  Y VUELVE AL INICIO
                    print("El nombre de la especialidad es incorrecto, ingréselo nuevamente.")
                    continue

                precio = float(input("Ingrese el precio asociado: "))
                if precio <= 0:
                    print("El precio de la especialidad es incorrecto, ingréselo nuevamente.")
                    continue

                self.especialidades[nombre] = precio
                #ACCEDEMOS A LA CLAVE "NOMBRE" ASIGNANDOLE EL VALOR DEL PRECIO
                #Y ASI, SE PUEDE INGRESAR COMO POR EJEMPLO= "ALBERTO"[NOMBRE]: 1200[PRECIO]
                print("La especialidad se ha creado con éxito.")
                time.sleep(2)
                #ESTA FUNCION HACE QUE LA TERMINAL ESTE EN PAUSA PARA MOSTRAR EL PRINT
                break
            except ValueError:
                print("El precio de la especialidad es incorrecto, ingréselo nuevamente.")

    def alta_socio(self):
        while True:
            try:
                nombre = input("Ingrese el nombre: ")
                if not nombre.isalpha() or nombre == " ":
                    #LA FUNCION ISALPHA HACE QUE RETORNE FALSO SI EL STRING TIENE NUMERICOS
                    print("No es un nombre válido, ingréselo de nuevo.")
                    continue

                apellido = input("Ingrese el apellido: ")
                if not apellido.isalpha() or apellido == " ":
                    print("No es un apellido válido, ingréselo de nuevo.")
                    continue

                cedula = input("Ingrese la cédula de identidad: ")
                if not cedula.isdigit() or len(cedula) != 8:
                    print("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")
                    continue

                fecha_nacimiento = input("Ingrese la fecha de nacimiento en formato (YYYY-MM-DD): ")
                fecha_ingreso = input("Ingrese la fecha de ingreso a la institución en formato (YYYY-MM-DD): ")

                celular = input("Ingrese el número de celular: ")
                if not celular.isdigit() or len(celular) != 9 or not celular.startswith("09"):
                    #USAMOS STARTSWITH PARA QUE LA VARIABLE CELULAR EMPIECE CON 09 EN LAS PRIMERAS POSICIONES
                    print("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX.")
                    continue

                tipo = input("Ingrese el tipo de socio (1- Bonificado, 2- No bonificado): ")
                if tipo not in ["1", "2"]:
                    print("El valor ingresado no es correcto, elige la opción 1 o 2.")
                    continue

                socio = Socio(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular, tipo)
                #AGREGAMOS LOS VALORES A LA CLASE SOCIO
                self.socios[cedula] = socio
                #Y LO AGREGAMOS AL ARRAY DE SOCIOS COMO CEDULA CLAVE
                print("El socio se ha creado con éxito.")
                time.sleep(2)
                break
            except ValueError:
                print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")

    def alta_medico(self):
        while True:
            try:
                nombre = input("Ingrese el nombre: ")
                if not nombre.isalpha() or nombre == " ":
                    print("No es un nombre válido, ingréselo de nuevo.")
                    continue

                apellido = input("Ingrese el apellido: ")
                if not apellido.isalpha() or apellido == " ":
                    print("No es un apellido válido, ingréselo de nuevo.")
                    continue

                cedula = input("Ingrese la cédula de identidad: ")
                if not cedula.isdigit() or len(cedula) != 8:
                    print("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")
                    continue

                fecha_nacimiento = input("Ingrese la fecha de nacimiento en formato (YYYY-MM-DD): ")
                fecha_ingreso = input("Ingrese la fecha de ingreso a la institución en formato (YYYY-MM-DD): ")

                celular = input("Ingrese el número de celular: ")
                if not celular.isdigit() or len(celular) != 9 or not celular.startswith("09"):
                    print("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX.")
                    continue

                especialidad = input("Ingrese la especialidad: ")
                if especialidad.isdigit() or especialidad == " ":
                    #VEFICA SI ES DE SOLO NUMEROS EL STRING  Y VUELVE AL INICIO
                    print("El nombre de la especialidad es incorrecto, ingréselo nuevamente.")
                    continue

                if especialidad not in self.especialidades:
                    print("""\nEsta especialidad no está dada de alta elija una opción::

                1- Volver a ingresar la especialidad
                2- Dar de alta esta especialidad """)
                    opcion = input("Opción: ")
                    if opcion == "1":
                        self.alta_medico()
                    elif opcion == "2":
                        self.alta_especialidad()
                        #AL QUERER DARLO DE ALTA SE VA A LA FUNCION DE ESPECIALIDAD Y LUEGO VUELVE A ESTA
                    else:
                        continue

                medico = Medico(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular, especialidad)
                self.medicos[cedula] = medico
                print("El médico se ha creado con éxito.")
                time.sleep(2)
                break
            except ValueError:
                print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")

    def alta_consulta_medica(self):
        while True:
            especialidad = input("Ingrese la especialidad: ")
            if especialidad.isdigit() or especialidad == " ":
                print("El nombre de la especialidad es incorrecto, ingréselo nuevamente.")
                continue
            if especialidad not in self.especialidades:
                #BUSCA SI LA ESPECIALIDAD ESTA EN EL ARRAY DE ESPECIALIDADES
                print("""\nEsta especialidad no está dada de alta elija una opción::

                1- Volver a ingresar la especialidad
                2- Dar de alta esta especialidad """)
                opcion = input("Opción: ")
                if opcion == "1":
                    self.alta_consulta_medica()
                elif opcion == "2":
                    self.alta_especialidad()
                else:
                    break

            medico_nombre = input("Ingrese el nombre del médico: ")
            if medico_nombre.isdigit() or medico_nombre == " ":
                print("El nombre del médico es incorrecto, ingréselo nuevamente.")
                continue
            encontrado = False
            #BUSCA SI EL MEDICO ESTA EN EL ARRAY DE MEDICOS
            #USAMOS LA VARIABLE ENCONTRADO PARA SABER SI NO LO ENCONTRAMOS LE DAMOS LA OPCION DE DARLO DE ALTA
            for medico in self.medicos.values():
                if medico.nombre == medico_nombre:
                    encontrado = True
                    break
            if not encontrado:
                print("""\nEste médico no está dada de alta elija una opción::

                1- Volver a ingresar el médico
                2- Dar de alta el médico """)
                opcion = input("Opción: ")
                if opcion == "1":
                    self.alta_consulta_medica()
                elif opcion == "2":
                    self.alta_medico()
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
                }) #SE GUARDAN LOS VALORES PARA LA CONSULTA MEDICA
                print("La consulta se ha creado con éxito.")
                time.sleep(2)
                break
            except ValueError:
                print("Por favor, ingrese los datos correctamente.")

    def emitir_ticket_consulta(self):
        especialidad = input("Ingrese la especialidad: ")
        if especialidad not in self.especialidades:
            print("""\nEsta especialidad no está dada de alta elija una opción::

                1- Volver a ingresar la especialidad
                2- Dar de alta esta especialidad """)
            opcion = input("Opción: ")
            if opcion == "1":
                self.emitir_ticket_consulta()
            elif opcion_socio == "2":
                self.alta_especialidad()
            return
        
        consultas_especialidad = [c for c in self.consultas if c["especialidad"] == especialidad]
        #RECORRE EL ARRAY DE CONSULTAS PARA VER SI HAY UNA ESPECIALIDAD 
        if not consultas_especialidad:
            print("No hay consultas disponibles para esta especialidad.")
            return

        print(f"Consultas disponibles para la especialidad {especialidad}:")
        for i, consulta in enumerate(consultas_especialidad, 1):
            print(f"{i}. Médico: {consulta['medico']}, Fecha: {consulta['fecha'].date()}")
            #IMPRIME EL NOMBRE DEL MEDICO CON LA FECHA DE CONSULTAS DISPONIBLE ACORDE A LA ESPEPCIALIDAD
        while True:
            try:
                opcion = int(input("Seleccione el número de atención deseado: "))
                if 1 <= opcion <= len(consultas_especialidad):
                    consulta_seleccionada = consultas_especialidad[opcion - 1]
                    #-1 POR QUE LOS ARRAY EMPIEZAN DE 0 Y SELECCIONA EL VALOR INDICADO
                    print(f"Ha seleccionado la consulta del médico {consulta_seleccionada['medico']} el {consulta_seleccionada['fecha'].date()}.")
                    #ELIGE LA CONSULTA EXITOSAMENTE CON EL NOMBRE DEL MEDICO Y LA FECHA DE LA CONSULTA
                    time.sleep(2)
                    break
                else:
                    print(f"La opción ingresada no es válida. Debe ser un número entre 1 y {len(consultas_especialidad)}.")
                    #CANTIDAD DE CONSULTAS MEDICAS DISPONIBLES EN ESA FECHA SEGUN LA ESPECIALIDAD
            except ValueError:
                print("Por favor, ingrese un número válido.")

        cedula_socio = input("Ingrese cédula de identidad del socio: ")
        if cedula_socio not in self.socios:
            print("""Este socio no está dado de alta, elija una opción:
                1 - Volver a ingresar el socio
                2 - Dar de alta el socio""")
            opcion_socio = input("Opción: ")
            if opcion_socio == "1":
                self.emitir_ticket_consulta()
            elif opcion_socio == "2":
                self.alta_socio()
            else:
                print("Opción no válida.")
                return
        
        print("Ticket de consulta emitido con éxito.")
        time.sleep(2)
    
    def realizar_consultas(self): 
        while True:
            print("""Seleccione una opción:
            1. Obtener todos los médicos asociados a una especialidad específica.
            2. Obtener el precio de una consulta de una especialidad en específico.
            3. Listar todos los socios con sus deudas asociadas en orden ascendente.
            4. Realizar consultas respecto a cantidad de consultas entre dos fechas.
            5. Realizar consultas respecto a las ganancias obtenidas entre dos fechas.
            6. Salir de consultas.""")

            opcion = input("Opción: ")

            if opcion == "1":
                especialidad = input("Ingrese la especialidad: ")
                medicos = self.obtener_medicos_por_especialidad(especialidad)
                if medicos:
                    for medico in medicos:
                        print(f"Nombre: {medico['nombre']} {medico['apellido']}, Celular: {medico['celular']}")
                else:
                    print("No hay médicos asociados a esta especialidad.")

            elif opcion == "2":
                especialidad = input("Ingrese la especialidad: ")
                precio = self.obtener_precio_especialidad(especialidad)
                print(f"Precio de la especialidad {especialidad}: {precio}")

            elif opcion == "3":
                socios = self.listar_socios_con_deudas()
                for cedula, datos in socios:
                    print(f"Cédula: {cedula}, Nombre: {datos['nombre']} {datos['apellido']}, Deuda: {datos['deuda']}")

            elif opcion == "4" or opcion == "5":
                try:
                    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
                    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
                    fecha_final = input("Ingrese la fecha final (YYYY-MM-DD): ")
                    fecha_final = datetime.strptime(fecha_final, "%Y-%m-%d")

                    if opcion == "4":
                        consultas = self.consultas_entre_fechas(fecha_inicio, fecha_final)
                        print(f"Cantidad de consultas entre {fecha_inicio.date()} y {fecha_final.date()}: {len(consultas)}")

                    elif opcion == "5":
                        ganancias = self.ganancias_entre_fechas(fecha_inicio, fecha_final)
                        print(f"Ganancias obtenidas entre {fecha_inicio.date()} y {fecha_final.date()}: {ganancias}")

                except ValueError:
                    print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")

            elif opcion == "6":
                break

            else:
                print("Opción no válida. Por favor, ingrese una opción del 1 al 6.")

    def menu_principal(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            #IMPORT OS PERMITE INTERACTUAR CON LA TERMINAL 
            #PARA HACER EL COMANDO DE CLS PARA LIMPAR PANTALLA
            print("""\nMenú principal:

            1. Dar de alta una especialidad
            2. Dar de alta un socio
            3. Dar de alta un médico
            4. Dar de alta una consulta médica
            5. Emitir un ticket de consulta
            6. Realizar Consultas
            7. Salir del programa""")
            #MENU PRINCIPAL PARA INICIALIZAR LAS FUNCIONES DE LA POLICLINICA Y/O SALIR DEL PROGRAMA
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
                self.realizar_consultas()
            elif opcion == "7":
                print("Saliendo...")
                time.sleep(1)
                break
            else:
                print("Opción no válida. Por favor, ingrese una opción del 1 al 6.")

if __name__ == "__main__":
    poli = Policlínica()
    #INICIALIZAMOS LA CLASE POLICLINICA CON EL VALOR DE POLI
    poli.menu_principal()
    #INICIALIZAMOS EL MENU PRINCIPAL
