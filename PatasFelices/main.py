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
        mascota = Perro(nombre, edad, salud, precio, raza, nivelDeEnergia)
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

def registrarProducto():
    nombre = input("Nombre del producto: ")
    categoria = input("Categoria del producto")
    precio = input("Precio del producto: ")
    cantidad = int(input("Cantidad del producto: "))
    producto = Producto(nombre, categoria, precio, cantidad)

    return producto

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

def main():
    mascotas = []
    clientes = []
    inventario = Inventario()

    while True:
        mostrarMenu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            mascota = registrarMascota()
            if mascota:
                mascotas.append(mascota)
                print ("Mascota registrada con exito")

        elif opcion == "2":
            cliente = registrarCliente()
            if cliente:
                clientes.append(cliente)
                print ("Cliente agregado con exito")
        
        elif opcion == "3":
            producto = registrarProducto()
            if producto:
                inventario.agregarProducto(producto)
                print("Producto registrado con exito")
        
        elif opcion == "4":
            registrarVenta(clientes, inventario)
        
        elif opcion == "5":
            for mascota in mascotas:
                print(mascota.mostrarInformacion())
                if isinstance(mascota, Perro) or isinstance(mascota, Gato):
                    print(mascota.mostrarCaracteristicas())
        
        elif opcion == "6":
            for cliente in clientes:
                print(cliente.mostrarInformacion())
        
        elif opcion == "7":
            for producto in inventario.listaDeProductos:
                print(producto.mostrarInformacion())
        
        elif opcion == "8":
            umbralMinimo = int(input("Ingrese el umbral minimo del inventario: "))
            print(inventario.generarAlerta(umbralMinimo))
        
        elif opcion == "9":
            print ("Gracias por utilizar nuestro sistema")
            break

        else:
            print("Opciion no valida, intente nuevamente: ")

if __name__ == "__main__":
    main()
