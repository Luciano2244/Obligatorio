from datetime import datetime
import os
import time
from Objetos.socio import Socio
from Objetos.medico import Medico
from Objetos.consulta_medica import Consulta_medica



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
                if nombre.isdigit() or nombre == " ":
                    #LA FUNCION ISALPHA HACE QUE RETORNE FALSO SI EL STRING TIENE NUMERICOS
                    print("No es un nombre válido, ingréselo de nuevo.")
                    continue

                apellido = input("Ingrese el apellido: ")
                if apellido.isdigit() or apellido == " ":
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
                if tipo not in ["1","2"]:
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
                if nombre.isdigit() or nombre == " ":
                    print("No es un nombre válido, ingréselo de nuevo.")
                    continue

                apellido = input("Ingrese el apellido: ")
                if apellido.isdigit() or apellido == " ":
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

                while True:
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
                            continue
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
                break
            except ValueError:
                print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")

    def alta_consulta_medica(self):
        while True:
            especialidad = input("Ingrese la especialidad: ")
            if especialidad.isdigit() or especialidad.strip() == "":
                print("El nombre de la especialidad es incorrecto, ingréselo nuevamente.")
                continue
            
            if especialidad not in self.especialidades:
                # La especialidad no está registrada, se ofrecen opciones
                print("""\nEsta especialidad no está dada de alta, elija una opción:

                1- Volver a ingresar la especialidad
                2- Dar de alta esta especialidad """)
                opcion = input("Opción: ")
                if opcion == "1":
                    continue
                elif opcion == "2":
                    self.alta_especialidad()
                    continue
                else:
                    break
            
            while True:
                medico_nombre = input("Ingrese el nombre del médico: ")
                if medico_nombre.isdigit() or medico_nombre.strip() == "":
                    print("El nombre del médico es incorrecto, ingréselo nuevamente.")
                    continue
                
                
                encontrado = False
                for medico in self.medicos.values():
                    if medico.nombre_completo == medico_nombre:
                        encontrado = True
                        break
                
                if not encontrado:
                    print("""\nEste médico no está dado de alta, elija una opción:

                    1- Volver a ingresar el nombre del médico
                    2- Dar de alta el médico """)
                    opcion = input("Opción: ")
                    if opcion == "1":
                        continue
                    elif opcion == "2":
                        self.alta_medico()
                        continue
                    else:
                        break
                else:
                    break
            
            try:
                fecha = input("Ingrese la fecha de la consulta (YYYY-MM-DD): ")
                fecha = datetime.strptime(fecha, "%Y-%m-%d")
                cantidad_pacientes = int(input("Ingrese la cantidad de pacientes que se atenderán: "))
                consulta = Consulta_medica(especialidad, medico_nombre, fecha, cantidad_pacientes, precio=self.especialidades[especialidad])
                self.consultas.append(consulta)
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
            elif opcion == "2":
                self.alta_especialidad()
            return
        
        consultas_especialidad = []
        for consulta in self.consultas:
            if consulta.especialidad == especialidad:
                consultas_especialidad.append(consulta)

        #RECORRE EL ARRAY DE CONSULTAS PARA VER SI HAY UNA ESPECIALIDAD 
        if not consultas_especialidad:
            print("No hay consultas disponibles para esta especialidad.")
            return

        print(f"Consultas disponibles para la especialidad {especialidad}:")
        for i, consulta in enumerate(consultas_especialidad, 1):
            print(f"{i}. Médico: {consulta.nombre_medico}, Fecha: {consulta.fecha_consulta.date()}")
            #IMPRIME EL NOMBRE DEL MEDICO CON LA FECHA DE CONSULTAS DISPONIBLE ACORDE A LA ESPEPCIALIDAD
        while True:
            try:
                opcion = int(input("Seleccione el número de atención deseado: "))
                if 1 <= opcion <= len(consultas_especialidad):
                    consulta_seleccionada = consultas_especialidad[opcion - 1]
                    #-1 POR QUE LOS ARRAY EMPIEZAN DE 0 Y SELECCIONA EL VALOR INDICADO
                    print(f"Ha seleccionado la consulta del médico {consulta_seleccionada.nombre_medico} el {consulta_seleccionada.fecha_consulta.date()}.")
                    break
                else:
                    print(f"La opción ingresada no es válida. Debe ser un número entre 1 y {len(consultas_especialidad)}.")
                    #CANTIDAD DE CONSULTAS MEDICAS DISPONIBLES EN ESA FECHA SEGUN LA ESPECIALIDAD
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        if consulta.elegir_numero_atencion_disponible() == "1":
            print("No hay números disponibles para esta consulta")
            time.sleep(2)
            self.menu_principal()

        while True:
            cedula_socio = input("Ingrese cédula de identidad del socio: ")
            if cedula_socio not in self.socios:
                print("""Este socio no está dado de alta, elija una opción:
                    1 - Volver a ingresar el socio
                    2 - Dar de alta el socio""")
                opcion_socio = input("Opción: ")
                if opcion_socio == "1":
                    continue
                elif opcion_socio == "2":
                    self.alta_socio()
                else:
                    print("Opción no válida.")
                    return
            break
        
        if cedula_socio in self.socios:
            socio = self.socios[cedula_socio]
        else:
            print("La cedula ingresada no es de ningun socio")
            self.emitir_ticket_consulta()
        precio=self.especialidades[especialidad]
        if socio.tipo == "1":
            costo_consulta = precio * 0.8
        else:
            costo_consulta = precio
        socio.deuda += costo_consulta

        print("Ticket de consulta emitido con éxito.")
        time.sleep(2)

    

    def realizar_consultas(self):
        while True:
            print("""\nSeleccione una opción:
                    1. Obtener todos los médicos asociados a una especialidad específica.
                    2. Obtener el precio de una consulta de una especialidad en específico.
                    3. Listar todos los socios con sus deudas asociadas en orden ascendente.
                    4. Realizar consultas respecto a cantidad de consultas entre dos fechas
                    5. Realizar consultas respecto a las ganancias obtenidas entre dos fechas.
                    6. Volver a Menu Principal """)
            opcion = input("Opcion: ")
            if opcion == "1":
                self.medicos_asociados_especialidad()
            elif opcion == "2":
                self.precio_especialidad()
            elif opcion == "3":
                self.deudas_socios()
            elif opcion == "4":
                self.consultas_entre_fechas()
            elif opcion == "5":
                self.ganancia_entre_fechas()
            elif opcion == "6":
                self.menu_principal()
                time.sleep(1)
                break
            else:
                print("Opción no válida. Por favor, ingrese una opción del 1 al 6.")

    def medicos_asociados_especialidad(self):
        especialidad = input("Ingrese la especialidad: ")
        if especialidad not in self.especialidades:
            print("Esta especialidad no está registrada.")
            return

        medicos_asociados = []
        for medico in self.medicos.values():
            if medico.especialidad == especialidad:
                medicos_asociados.append(medico)

        if not medicos_asociados:
            print("No hay médicos asociados a esta especialidad.")
            return

        print(f"Médicos asociados a la especialidad '{especialidad}':")
        for medico in medicos_asociados:
            print(f"Medico: {medico.nombre} {medico.apellido}, Cédula: {medico.cedula}")
        time.sleep(2)

    def precio_especialidad(self):
        especialidad = input("Ingrese la especialidad: ")
        if especialidad not in self.especialidades:
            print("Esta especialidad no está registrada.")
            return

        precio = self.especialidades[especialidad]
        print(f"El precio de una consulta de la especialidad '{especialidad}' es: {precio}")
        time.sleep(1)
    
    def deudas_socios(self):
        socios_ordenados = sorted(self.socios.items(), key=lambda x: x[1].deuda)
        for cedula, socio in socios_ordenados:
            print(f"Socio: {socio.nombre} {socio.apellido}, Cédula: {cedula}, Deuda: {socio.deuda}")
        return
    
    def consultas_entre_fechas(self):
        while True:
            fecha_inicio =input("Ingrese la fecha de inicio en formato (YYYY-MM-DD): ")
            fecha_fin = input("Ingrese la fecha de fin en formato (YYYY-MM-DD): ")
            try:
                fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
                fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
                break
            except ValueError:
                print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd: ")
        
        consultas_realizadas_entre_fechas = 0
        for consulta in self.consultas:
            if fecha_inicio <= consulta.fecha_consulta <= fecha_fin:
                consultas_realizadas_entre_fechas += 1

        print(f"Se realizaron {consultas_realizadas_entre_fechas} consultas entre {fecha_inicio.date()} y {fecha_fin.date()}.")

    def ganancia_entre_fechas(self):
        while True:
            fecha_inicio =input("Ingrese la fecha de inicio en formato (YYYY-MM-DD): ")
            fecha_fin = input("Ingrese la fecha de fin en formato (YYYY-MM-DD): ")
            try:
                fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
                fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
                break
            except ValueError:
                print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd: ")

        ganancia_total_entre_fechas = 0
        for consulta in self.consultas:
            if fecha_inicio <= consulta.fecha_consulta <= fecha_fin:
                ganancia_total_entre_fechas += consulta.precio

        print(f"Se obtuvo una ganancia total de {ganancia_total_entre_fechas} entre {fecha_inicio.date()} y {fecha_fin.date()}.")
        
        

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
                time.sleep(2)
                break
            else:
                print("Opción no válida. Por favor, ingrese una opción del 1 al 7.")

if __name__ == "__main__":
    poli = Policlínica()
    #INICIALIZAMOS LA CLASE POLICLINICA CON EL VALOR DE POLI
    poli.menu_principal()
    #INICIALIZAMOS EL MENU PRINCIPAL
