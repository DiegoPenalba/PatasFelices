class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.historialCompras = []
    
    def actualizarInformacion(self, direccion=None, telefono=None):
        if direccion:
            self.direccion = direccion
        
        if telefono:
            self.telefono = telefono
    
    def registrarCompra(self, compra):
        self.historialCompras.append(compra)
    
    def mostrarInformacion(self):
        return f"Cliente: {self.nombre}, Direccion: {self.direccion}, Telefono: {self.telefono}."