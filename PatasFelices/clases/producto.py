class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
    
    def actualizarCantidad(self, cantidad):
        self.cantidad = cantidad
    
    def mostrarInformacion(self):
        return f"Producto: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}, Cantidad: {self.cantidad}."