class Mascota:
    def __init__(self, nombre, edad, salud, precio):
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.precio = precio
    
    #get
    def actualizarInformacion(self, edad=None, salud=None, precio=None):
        if edad:
            self.edad = edad
        
        if salud:
            self.salud = salud
        
        if precio:
            self.precio = precio
    
    def mostrarInformacion(self):
        return f"Mascota: {self.nombre}, Edad: {self.edad}, Precio: {self.precio}"

class Perro(Mascota):
    def __init__(self, nombre, edad, salud, precio, raza, nivelDeEnergia):
        super().__init__(nombre, edad, salud, precio)
        self.raza = raza
        self.nivelDeEnergia = nivelDeEnergia
    
    def mostrarCaracteristicas(self):
        return f"Raza: {self.raza}, Nivel de energia: {self.nivelDeEnergia}"

class Gato(Mascota):
    def __init__(self, nombre, edad, salud, precio, raza, independencia):
        super().__init__(nombre, edad, salud, precio)
        self.raza = raza
        self.independencia = independencia
    
    def mostrarCaracteristicas(self):
        return f"Raza: {self.raza}, Nivel de independencia: {self.independencia}"
