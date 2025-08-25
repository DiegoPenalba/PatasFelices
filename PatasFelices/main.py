from clases.cliente import Cliente
from clases.inventario import Inventario
from clases.mascota import Mascota, Perro, Gato
from clases.producto import Producto
from clases.venta import Venta

# funciones para interfaz de consola
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