"""
Ejercicio 3: Gestión de Reservas en un Hotel de Playa
Descripción: Un hotel de playa cuenta con un recepcionista que se encarga de presentar 
a los clientes las opciones de habitaciones disponibles junto con sus precios. 
Tras la elección de la habitación, el recepcionista solicita los datos personales del cliente 
y el número de noches que permanecerá en el hotel. Finalmente, entrega al cliente una factura 
detallada con el total de los gastos. • Adicionalmente, los clientes pueden solicitar servicios extra, 
como el uso de la piscina o la cancha de golf, que tienen un costo adicional. Implementa esta 
funcionalidad en tu programa

desarrollo:
Crearemos una clase Habitación que contenga atributos como tipo, precio y disponibilidad.
Implementa una clase Cliente que contenga datos personales y gestione la factura.
La clase Hotel va a manejar la reserva de habitaciones y la adición de servicios extra 
como piscina o cancha de golf. 
"""

class Habitacion:
    def __init__(self, tipo, precio, disponible=True):
        """
        Constructor de la clase Habitación.
        tipo: Tipo de la habitación (simple, doble, suite).
        precio: Precio por noche de la habitación.
        disponible: Indica si la habitación está disponible para reservar.
        """
        self.tipo = tipo
        self.precio = precio
        self.disponible = disponible

    def actualizar_disponibilidad(self, disponible):
        """
        actualizar la disponibilidad de la habitación.
        disponible: Nueva disponibilidad de la habitación.
        """
        self.disponible = disponible


class Cliente:
    def __init__(self, nombre, dni):
        """
        Constructor de la clase Cliente.
        nombre: Nombre del cliente.
        dni: Documento de identidad del cliente.
        """
        self.nombre = nombre
        self.dni = dni
        self.factura = []

    def agregar_cargo(self, descripcion, monto):
        """
        agregar un cargo a la factura del cliente.
        descripcion: Descripción del cargo.
        monto: Monto del cargo.
        """
        self.factura.append((descripcion, monto))

    def mostrar_factura(self):
        """
        mostrar la factura detallada del cliente.
        """
        total = 0
        print(f"Factura para {self.nombre} (DNI: {self.dni}):")
        for descripcion, monto in self.factura:
            print(f"- {descripcion}: ${monto:.2f}")
            total += monto
        print(f"Total: ${total:.2f}")


class Hotel:
    def __init__(self):
        """
        Constructor de la clase Hotel.
        """
        self.habitaciones = []
        self.clientes = []

    def agregar_habitacion(self, tipo, precio):
        """
        agregar una nueva habitación al inventario del hotel.
        tipo: Tipo de la habitación.
        precio: Precio por noche de la habitación.
        """
        nueva_habitacion = Habitacion(tipo, precio)
        self.habitaciones.append(nueva_habitacion)

    def mostrar_habitaciones_disponibles(self):
        """
        Método para mostrar todas las habitaciones disponibles con sus precios.
        """
        print("Habitaciones disponibles:")
        for habitacion in self.habitaciones:
            if habitacion.disponible:
                print(f"Tipo: {habitacion.tipo}, Precio: ${habitacion.precio:.2f} por noche")

    def reservar_habitacion(self, cliente, tipo_habitacion, noches):
        """
        reservar una habitación para un cliente.
        cliente: Objeto Cliente que hace la reserva.
        tipo_habitacion: Tipo de habitación que el cliente desea reservar.
        noches: Número de noches que el cliente se hospedará.
        """
        for habitacion in self.habitaciones:
            if habitacion.tipo == tipo_habitacion and habitacion.disponible:
                total_costo = habitacion.precio * noches
                cliente.agregar_cargo(f"Reserva de {tipo_habitacion} por {noches} noches", total_costo)
                habitacion.actualizar_disponibilidad(False)
                print(f"Habitación {tipo_habitacion} reservada para {cliente.nombre} por {noches} noches. Total: ${total_costo:.2f}")
                return
        print(f"No hay habitaciones disponibles del tipo {tipo_habitacion}.")

    def agregar_servicio_extra(self, cliente, servicio):
        """
        agregar un servicio extra a la factura del cliente.
        cliente: Objeto Cliente que solicita el servicio extra.
        servicio: Nombre del servicio extra (por ejemplo, "piscina" o "golf").
        """
        servicios_extras = {
            "piscina": 50.00,
            "golf": 100.00
        }
        if servicio in servicios_extras:
            cliente.agregar_cargo(f"Servicio extra: {servicio}", servicios_extras[servicio])
            print(f"Servicio de {servicio} añadido a la factura de {cliente.nombre}.")
        else:
            print(f"Servicio {servicio} no disponible.")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un objeto Hotel
    hotel = Hotel()
    
    # Agregar habitaciones al hotel
    hotel.agregar_habitacion("simple", 80.00)
    hotel.agregar_habitacion("doble", 120.00)
    hotel.agregar_habitacion("suite", 200.00)
    
    # Mostrar habitaciones disponibles
    hotel.mostrar_habitaciones_disponibles()
    
    # Crear un objeto Cliente
    cliente1 = Cliente("Elmer Gonzalez", "12345678")
    
    # Registrar al cliente en el hotel
    hotel.clientes.append(cliente1)
    
    # Reservar una habitación
    hotel.reservar_habitacion(cliente1, "doble", 3)
    
    # Agregar un servicio extra
    hotel.agregar_servicio_extra(cliente1, "piscina")
    
    # Mostrar la factura del cliente
    cliente1.mostrar_factura()
