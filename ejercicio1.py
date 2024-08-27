"""
Una tienda local vende diversos productos, cada vez que un cliente
hace una compra niña mary se encarga de anotarlo en una libreta. A su
vez, con una calculadora le da el total a cada cliente y les da su
respectivo vuelto en caso de necesitarlo.
* Niña mary también se encarga de atender a los proveedores que
le dan cierta cantidad de producto y un precio sugerido de venta,
propón una solución dentro de tu programa para ayudarle.

desarrollo:
Implementaremos una clase Producto que contenga atributos como nombre, precio de compra, 
precio de venta y cantidad en inventario.
Creamos una clase Tienda que administre una lista de productos. Esta clase debe permitir:
Registrar una venta, calcular el total y el vuelto.
Registrar productos de proveedores, actualizar inventario y ajustar precios.

"""
class Producto:
    def __init__(self, nombre, precio_compra, precio_venta, cantidad):
        """
        Constructor de la clase Producto.
         nombre: Nombre del producto.
         precio_compra: Precio de compra del producto.
         precio_venta: Precio de venta del producto.
         cantidad: Cantidad disponible en inventario.
        """
        self.nombre = nombre
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio_venta):
        """
        actualizar el precio de venta del producto.
        nuevo_precio_venta: Nuevo precio de venta del producto.
        """
        self.precio_venta = nuevo_precio_venta

    def agregar_inventario(self, cantidad):
        """
        agregar más cantidad al inventario.
        cantidad: Cantidad a agregar al inventario.
        """
        self.cantidad += cantidad

    def reducir_inventario(self, cantidad):
        """
        reducir la cantidad en el inventario.
        cantidad: Cantidad a reducir del inventario.
        return: True si se pudo reducir la cantidad y False si no hay suficiente inventario.
        """
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            return True
        else:
            return False


class Tienda:
    def __init__(self):
        """
        Constructor de la clase Tienda.
        """
        self.productos = []

    def registrar_producto(self, nombre, precio_compra, precio_venta, cantidad):
        """
        Método para registrar un nuevo producto o actualizar uno existente en el inventario.
         nombre: Nombre del producto.
         precio_compra: Precio de compra del producto.
         precio_venta: Precio de venta del producto.
         cantidad: Cantidad del producto a agregar al inventario.
        """
        # Buscar si el producto ya existe
        for producto in self.productos:
            if producto.nombre == nombre:
                # Actualizar el inventario y el precio de venta
                producto.agregar_inventario(cantidad)
                producto.actualizar_precio(precio_venta)
                print(f"Producto '{nombre}' actualizado con éxito.")
                return
        # Si el producto no existe, agregarlo
        nuevo_producto = Producto(nombre, precio_compra, precio_venta, cantidad)
        self.productos.append(nuevo_producto)
        print(f"Producto '{nombre}' registrado con éxito.")

    def registrar_venta(self, nombre_producto, cantidad, pago_cliente):
        """
         Método para registrar una venta de un producto.
         nombre_producto: Nombre del producto a vender.
         cantidad: Cantidad del producto a vender.
         pago_cliente: Monto pagado por el cliente.
        """
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.reducir_inventario(cantidad):
                    total = cantidad * producto.precio_venta
                    if pago_cliente >= total:
                        vuelto = pago_cliente - total
                        print(f"Venta exitosa. Total: ${total:.2f}, Vuelto: ${vuelto:.2f}")
                    else:
                        print(f"Pago insuficiente. Total: ${total:.2f}, Pago: ${pago_cliente:.2f}")
                else:
                    print(f"No hay suficiente inventario de '{nombre_producto}'.")
                return
        print(f"Producto '{nombre_producto}' no encontrado.")

    def mostrar_inventario(self):
        """
        Método para mostrar el inventario actual de la tienda.
        """
        print("\nInventario actual:")
        for producto in self.productos:
            print(f"{producto.nombre} - Cantidad: {producto.cantidad}, Precio de venta: ${producto.precio_venta:.2f}")


if __name__ == "__main__":
    tienda = Tienda()
    
    # Agregar productos
    tienda.registrar_producto("Manzanas", 0.30, 0.50, 10)
    tienda.registrar_producto("Plátanos", 0.20, 0.40, 15)
    
    # Mostrar inventario
    tienda.mostrar_inventario()
    
    # Realizar venta
    tienda.registrar_venta("Manzanas", 10, 6.00)
    
    # Mostrar inventario después de la venta
    tienda.mostrar_inventario()
    
    # Actualizar producto existente
    tienda.registrar_producto("Manzanas", 0.30, 0.55, 50)
    
    # Mostrar inventario actualizado
    tienda.mostrar_inventario()
