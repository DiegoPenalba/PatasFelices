class Inventario:
    def __init__(self):
        self.listaDeProductos = []
    
    def agregarProducto(self, producto):
        self.listaDeProductos.append(producto)
    
    def instanciaInventario(self, producto, cantidad):
        for prod in self.listaDeProductos:
            if prod.nombre == producto.nombre:
                prod.actualizarCantidad(cantidad)
    
    def generarAlerta(self, umbralMinimo):
        alertas = [prod.nombre for prod in self.listaDeProductos if prod.cantidad < umbralMinimo]
        return f"Productos por debajo del umbral: {', '.join(alertas)}" if alertas else "No hay productos por debajo del umbral minimo determinado"
    