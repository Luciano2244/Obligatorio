from datetime import datetime

class Medico:
    def __init__(self, nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular, especialidad):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        self.fecha_ingreso = datetime.strptime(fecha_ingreso, "%Y-%m-%d")
        self.celular = celular
        self.especialidad = especialidad

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    @property
    def antiguedad(self):
        today = datetime.today()
        return today.year - self.fecha_ingreso.year - ((today.month, today.day) < (self.fecha_ingreso.month, self.fecha_ingreso.day))

    def __str__(self):
        return f"Médico: {self.nombre_completo}, Cédula: {self.cedula}, Especialidad: {self.especialidad}, Antigüedad: {self.antiguedad} años"
