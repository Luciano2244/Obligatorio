
class Consulta_medica:
    def __init__(self, especialidad, nombre_medico, fecha_consulta, cantidad_pacientes_atenderan, precio):
        self.__especialidad = especialidad
        self.__nombre_medico = nombre_medico
        self.__fecha_consulta = fecha_consulta
        self.__cantidad_pacientes_atenderan = cantidad_pacientes_atenderan
        self.__precio = precio
        self.__numeros_disponibles = list(range(1, cantidad_pacientes_atenderan + 1))
        
    @property
    def especialidad(self):
        return self.__especialidad

    @property
    def nombre_medico(self):
        return self.__nombre_medico
     
    @property
    def fecha_consulta(self):
        return self.__fecha_consulta
    
    @property
    def cantidad_pacientes_atenderan(self):
        return self.__cantidad_pacientes_atenderan
    
    @property
    def precio(self):
        return self.__precio
    
    @property
    def numeros_disponibles(self):
        return self.__numeros_disponibles
    
    def elegir_numero_atencion_disponible(self):
        while True:
            try:
                if self.__numeros_disponibles == []:
                    return "1"
                print(f"Números de atención disponibles: {self.__numeros_disponibles}")
                numero_atencion = int(input("Seleccionar el número de atención deseado: "))
                if numero_atencion in self.__numeros_disponibles:
                    print(f"Ha seleccionado el {numero_atencion}")
                    self.__numeros_disponibles.remove(numero_atencion)
                    break
                else:
                    print(f"No es un número de consulta válido, los números válidos son {self.__numeros_disponibles}")
            except ValueError:
                print(f"No es un número de consulta válido, los números válidos son {self.__numeros_disponibles}")

