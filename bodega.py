# bodega.py
#.
class Bodega:
    def __init__(self, nombre, ubicacion, capacidad_maxima):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad_maxima = capacidad_maxima
        self.productos_almacenados = {}

    def agregar_producto(self, producto, cantidad):
        if sum(self.productos_almacenados.values()) + cantidad <= self.capacidad_maxima:
            if producto in self.productos_almacenados:
                self.productos_almacenados[producto] += cantidad
            else:
                self.productos_almacenados[producto] = cantidad
        else:
            print("No hay suficiente espacio en la bodega.")

    def retirar_producto(self, producto, cantidad):
        if producto in self.productos_almacenados and self.productos_almacenados[producto] >= cantidad:
            self.productos_almacenados[producto] -= cantidad
            if self.productos_almacenados[producto] == 0:
                del self.productos_almacenados[producto]
        else:
            print("No hay suficiente stock para retirar.")

    def consultar_disponibilidad(self, producto):
        return self.productos_almacenados.get(producto, 0)

    def __str__(self):
        return f"Bodega: {self.nombre}, Ubicación: {self.ubicacion}, Capacidad: {self.capacidad_maxima}, Productos: {[producto.nombre for producto en self.productos_almacenados.keys()]}"
