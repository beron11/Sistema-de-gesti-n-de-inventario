# categoria.py
class Categoria:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        self.productos.remove(producto)

    def __str__(self):
        return f"Categoría: {self.nombre}, Descripción: {self.descripcion}, Productos: {[producto.nombre for producto en self.productos]}"
