from clases.cliente import Cliente
from clases.inventario import Inventario
from clases.mascota import Mascota, Perro, Gato
from clases.producto import Producto
from clases.venta import Venta

# Funciones para interfaz de consola
def registrarMascota():
    tipo = input("Ingrese el tipo de mascota (Perro/Gato): ").strip().lower()
    nombre = input("Nombre de la mascota: ")
    edad = int(input("Edad de la mascota: "))
    salud = input("Estado de salud de la mascota: ")
    precio = float(input("Precio atencion de la mascota:"))

    if tipo == "perro":
        raza = input("Ingrese la raza del perro: ")
        nivelDeEnergia = input("Nivel de energia del pero: ")
        mascota = Perro(nombre, edad, salud, precio, nivelDeEnergia)
    elif tipo == "gato":
        raza = input("Ingrese la raza del gato: ")
        independencia = input("Ingrese el nivel de independencia del gato: ")
        mascota = Gato(nombre, edad, salud, precio, raza, independencia)
    else:
        print("Tipo de mascota no reconocido")
        return
    
    return mascota

def registrarCliente():
    nombre = input("Ingrese nombre del cliente: ")
    direccion = input("Ingrese direccion del cliente: ")
    telefono = input("ingrese telefono del cliente: ")
    cliente = Cliente(nombre, direccion, telefono)
    return cliente

def registrarVenta(clientes, inventario):
    nombreCliente = input("Nombre del cliente: ")
    cliente = next((c for c in clientes if c.nombre == nombreCliente), None)
    if not cliente:
        print("Cliente no encontrado.")
        return
    
    productos = []
    
    while True:
        nombreDelProducto = input("Nombre del producto (deje vacio para finalizar): ")
        if not nombreDelProducto:
            break

        producto = next((p for p in inventario.listaDeProductos if p.nombre == nombreDelProducto), None)
        if producto:
            productos.append(producto)
        else:
            print("Producto no encontrado")
    
    if productos:
        venta = Venta(cliente, productos)
        venta.registrarVenta()
        print("La venta ha sido realizada con exito")
    else:
        print("No se han registrado productos para la venta.")

def mostrarMenu():
    print("\n --- Menu de gestion de Patas Felices ---")
    print("1. Registrar Mascota")
    print("2. Registrar Cliente")
    print("3. Registrar Producto")
    print("4. Registrar Venta")
    print("5. Mostrar informacion de Mascotas")
    print("6. Mostrar informacion de Clientes")
    print("7. Mostrar informacion de Productos")
    print("8. Generar alerta de Inventario")
    print("9. Salir.")


    