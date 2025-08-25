from datetime import datetime

class Venta:
    def __init__(self, cliente, listaDeProductos):
        self.cliente = cliente
        self.listaDeProductos = listaDeProductos
        self.fecha = datetime.now() 
        self.total = self.calcularTotal()
    
    def calcularTotal(self):
        return sum(producto.precio for producto in self.listaDeProductos)
    
    def registrarVenta(self):
        self.cliente.registrarCompra(self)
        return f"Venta registrada: {self.mostrarInformacion()}"

    def mostrarInformacion(self):
        productos = ", ".join([producto.nombre for producto in self.listaDeProductos])
        return f"Cliente: {self.cliente.nombre}, Producto: {productos}, Total: {self.total}"
