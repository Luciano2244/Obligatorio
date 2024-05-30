from datetime import datetime

class Socio:
    def __init__(self, nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular, tipo):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        self.fecha_ingreso = datetime.strptime(fecha_ingreso, "%Y-%m-%d")
        self.celular = celular
        self.tipo = "Bonificado" if tipo == "1" else "No bonificado"
        self.deuda = 0

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    @property
    def edad(self):
        today = datetime.today()
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))

    def __str__(self):
        return f"Socio: {self.nombre_completo}, Cédula: {self.cedula}, Edad: {self.edad}, Tipo: {self.tipo}"
