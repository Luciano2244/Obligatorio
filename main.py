from entities.medico import Medico
from entities.especialidad import Especialidad
from datetime import datetime

# Función para obtener nombres de medicos de una especialidad en específico
def obtener_medico_asociado_especialidad(nombre_especialidad):
    if nombre_especialidad == medico1.especialidad:
        return medico1.nombre
    elif nombre_especialidad == medico2.especialidad:
        return medico2.nombre
    else:
        return None  
    
# Función para obtener el precio de una consulta de una especialidad en específico
def obtener_precio_especialidad(nombre_especialidad):
    if nombre_especialidad == especialidad_1.nombre:
        return especialidad_1.precio_fijo
    elif nombre_especialidad == especialidad_2.nombre:
        return especialidad_2.precio_fijo
    else:
        return None  


especialidad_1 = Especialidad("Dermatología", 50)
especialidad_2 = Especialidad("Cardiología", 80)
nombre_especialidad = "Dermatología"
precio_consulta = obtener_precio_especialidad(nombre_especialidad)
print(precio_consulta)
    
medico1 = Medico("Juan", "Belgeri", 123456, "2002-02-12", "2004-04-12", 222222, "Cardiología")
medico2 = Medico("Pedro", "Martinez", 654321, "2000-01-01", "2005-05-05", 111111, "Dermatología")

medico = obtener_medico_asociado_especialidad("Cardiología")
print(medico)