import datetime
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
                precio = float(input("Ingrese el precio asociado: "))          
                nombre_check= nombre.isdigit()
                precio_check= isinstance(precio, float)
                #checkeo datos
                if nombre_check==False and precio_check==1:
                    self.especialidades[nombre] = precio
                    print("La especialidad se ha creado con éxito.")
                    time.sleep(3)
                    break
                if nombre_check==True:
                    print("Por favor, ingrese un nombre válido.") 
                elif precio_check!=1:
                    print("Por favor, ingrese un precio válido.")
            except ValueError:
                if nombre_check==True:
                    print("Por favor, ingrese un nombre válido.") 
                elif precio_check!=1:
                    print("Por favor, ingrese un precio válido.")

    def alta_socio(self):
        while True:
            try:    
                nombre = input("Ingrese el nombre: ")
                apellido = input("Ingrese el apellido: ")
                cedula = int(input("Ingrese la cédula de identidad: "))
                fecha_nacimiento = datetime(input("Ingrese la fecha de nacimiento (YYYY-MM-DD): "))
                #usamos formato datetime(por defecto) para que quede en formato de fecha
                fecha_ingreso = datetime(input("Ingrese la fecha de ingreso (YYYY-MM-DD): "))
                celular = int(input("Ingrese el número de celular: "))
                tipo = input("Ingrese el tipo de socio (1- Bonificado, 2- No bonificado): ")
                #datos ingresados
                #elegir tipos
                if tipo == "1":
                    tipo = "Bonificado"
                elif tipo == "2":
                    tipo = "No bonificado"
                else:
                    raise ValueError
                
                fecha_nacimiento = datetime.fromisoformat(fecha_nacimiento)
                fecha_ingreso = datetime.fromisoformat(fecha_ingreso)
                #checkeo formato de fechas
                nombre_check= nombre.isdigit()
                apellido_check= apellido.isdigit()
                cedula_check= isinstance(cedula,int)
                celular_check= isinstance(celular,int)
                #checkeo datos, esto va a dar TRUE si es str y 1 si es int

                if nombre_check==False and apellido_check==False and cedula_check==1 and celular_check==1:
                    self.socios[cedula] = {
                        "nombre": nombre, 
                        "apellido": apellido,
                        "fecha_nacimiento": fecha_nacimiento,
                        "fecha_ingreso": fecha_ingreso,
                        "celular": celular,
                        "tipo": tipo,
                        "deuda": 0   
                    }
                    #guardamos valores en el array de self.socios
                    print("El socio se ha creado con éxito.")
                    break
                else:
                    print("Por favor, ingrese valores válidos.")
            except ValueError:
                print("Por favor, ingrese valores válidos.")

    def alta_medico(self):
        while True:
            try:
                nombre = input("Ingrese el nombre: ")
                apellido = input("Ingrese el apellido: ")
                cedula = int(input("Ingrese la cédula de identidad: "))
                fecha_nacimiento = datetime(input("Ingrese la fecha de nacimiento (YYYY-MM-DD): "))
                fecha_ingreso = datetime(input("Ingrese la fecha de ingreso (YYYY-MM-DD): "))
                celular = int(input("Ingrese el número de celular: "))
                especialidad = input("Ingrese la especialidad: ")
                #datos ingresados
                nombre_check=nombre.isdigit()
                apellido_check=apellido.isdigit()
                cedula_check=isinstance(cedula,int)
                celular_check=isinstance(celular,int)
                especialidad_check=especialidad.isdigit()
                fecha_nacimiento = datetime.fromisoformat(fecha_nacimiento)
                fecha_ingreso = datetime.fromisoformat(fecha_ingreso)
                #de nuevo, checkeo datos

                if nombre_check==False and apellido_check==False and cedula_check==1 and celular_check==1 and especialidad_check==False:
                    self.medicos[cedula] = {
                        "nombre": nombre,
                        "apellido": apellido,
                        "fecha_nacimiento": fecha_nacimiento,
                        "fecha_ingreso": fecha_ingreso,
                        "celular": celular,
                        "especialidad": especialidad
                    }
                    #guardamos valores en el array de self.medicos
                    print("El médico se ha creado con éxito.")
                    time.sleep(3)
                    break
                elif nombre_check==True:
                    print("Por favor, ingrese un nombre válido.")
                elif apellido_check==True:
                    print("Por favor, ingrese un apellido válido.")
                elif cedula_check!=1:
                    print("Por favor, ingrese una cedula válida.")
                elif celular_check!=1:
                    print("Por favor, ingrese un numero telefonico válido.")   
                elif especialidad_check!=True:
                    print("Por favor, ingrese una especialidad válida.")     
            except ValueError:
                print("Por favor, ingrese valores válidos.")

    def alta_consulta_medica(self):

        while True:
            especialidad = input("Ingrese la especialidad: ")
            if especialidad not in self.especialidades:
                print("La especialidad no está dada de alta.")
                opcion = input("Desea dar de alta esta especialidad? (s/n): ")
                if opcion.lower() == "s":
                    self.alta_especialidad()
                else:
                    break
            else:
                medico_nombre = input("Ingrese el nombre del médico: ")
                encontrado = False #hacemos "encontrado" para validar si se encontro el medico
                for medico in self.medicos.values():
                    if medico["nombre"] == medico_nombre:
                        encontrado = True
                        break
                if not encontrado:
                    #no se encontro y damos la opcion de darlo de alta
                    print("Este médico no está dado de alta.")
                    opcion = input("Desea dar de alta este médico? (s/n): ")
                    if opcion.lower() == "s":
                        self.alta_medico()
                    else:
                        break
                else:
                    fecha = datetime(input("Ingrese la fecha de la consulta (YYYY-MM-DD): "))
                    cantidad_pacientes = int(input("Ingrese la cantidad de pacientes que se atenderán: "))
                    try:
                        self.consultas.append({
                            "especialidad": especialidad,
                            "medico": medico_nombre,
                            "fecha": fecha,
                            "cantidad_pacientes": cantidad_pacientes
                        })
                        #guardamos en el array de consultas
                        print("La consulta se ha creado con éxito.")
                        break
                    except ValueError:
                        print("Por favor, ingrese un valor numérico para la cantidad de pacientes.")

    def emitir_ticket_consulta(self):

        especialidad = input("Ingrese la especialidad: ")
    
        if especialidad not in self.especialidades:
            #veficica si la especialidad no esta
            print("La especialidad no está dada de alta.")
            opcion = input("¿Desea dar de alta esta especialidad? (s/n): ")
            if opcion.lower() == "s":
                self.alta_especialidad()
            else:
                return
            
        #busca consultas con respecto a la especialidad escrita
        print("Consultas disponibles para la especialidad", especialidad)
        for i, consulta in enumerate(self.consultas, x=1):
            #utilizo enumerate para numerar int junto con array
            if consulta["especialidad"] == especialidad:
                print(f"{i}. Médico: {consulta['medico']}, Fecha: {consulta['fecha']}")

        while True:
            opcion = int(input("Seleccione el número de atención deseado: "))
            #selecciona una de las consultas disponibles
            try:
                if 1 <= opcion <= len(self.consultas):
                    numero_consulta = opcion - 1
                    consulta = self.consultas[numero_consulta]

                    print(f"Ha seleccionado la consulta del médico {consulta['medico']} el {consulta['fecha']}.")
                    #el print f lo hacemos precisamente para evitar comas y que el print se escriba mas lindo
                    break
                else:
                    print(f"La opción ingresada no es válida. Debe ser un número entre 1 y {len(self.consultas)}.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def menu_principal(self):
        while True:
            os.system("cls") #funcion para limpiar pantalla
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
                print("Saliendo del programa...")
                break
            else:
                print("La opción seleccionada no es válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    poli = Policlínica()
    #inicializa los valores con self para que se guarden
    poli.menu_principal()
    #inicializa el menu
