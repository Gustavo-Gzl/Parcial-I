#4.	Una empresa cuenta con dos tipos de empleados: aquellos con plaza fija y aquellos que trabajan por horas.
#Se han registrado los datos de ambos tipos y, al generar la planilla de pago, se realizan dos cálculos diferentes. 
#A los empleados de plaza fija se les paga el salario base más comisiones, mientras que
#a los empleados por horas se les paga en función de la cantidad de horas trabajadas. 
#Adicionalmente, si un empleado ha laborado más de 5 años, sin importar su tipo de contrato, 
#se le otorga un bono adicional. Implemente esto en su código. 


#Desarrollo:
#Creamos una clase Empleado con atributos comunes como nombre, identificación, años de servicio.
#tambien implemetamos subclases (es decir clases en las clases) EmpleadoFijo y EmpleadoPorHoras, con sus respectivos métodos para calcular el salario.
#La clase Empresa  gestiona la lista de empleados y generar la planilla de pago.
#lo hicimos mas que todo partiendo de las subclases 


# Clase Empleado.
class Empleado:
    def __init__(self, nombre, identificacion, anios_servicio):
        self.nombre = nombre
        self.identificacion = identificacion
        self.anios_servicio = anios_servicio

    def calcular_bono_antiguedad(self):
        """
        Calcula un bono adicional si el empleado tiene más de 5 años de servicio.
        """
        if self.anios_servicio > 5:
            return 100  # Bono fijo de 100
        return 0

    # Subclase dentro de la clase  EmpleadoFijo para empleados con plaza fija
    class EmpleadoFijo:
        def __init__(self, nombre, identificacion, anios_servicio, salario_base, comisiones):
            self.nombre = nombre
            self.identificacion = identificacion
            self.anios_servicio = anios_servicio
            self.salario_base = salario_base
            self.comisiones = comisiones

        def calcular_salario(self):
            """
            Calcula el salario total para un empleado fijo.
            """
            bono = Empleado(self.nombre, self.identificacion, self.anios_servicio).calcular_bono_antiguedad()
            salario = self.salario_base + self.comisiones + bono
            return salario

    # Subclase EmpleadoPorHoras para empleados que trabajan por horas
    class EmpleadoPorHoras:
        def __init__(self, nombre, identificacion, anios_servicio, tarifa_hora, horas_trabajadas):
            self.nombre = nombre
            self.identificacion = identificacion
            self.anios_servicio = anios_servicio
            self.tarifa_hora = tarifa_hora
            self.horas_trabajadas = horas_trabajadas

        def calcular_salario(self):
            """
            Calcula el salario total para un empleado por horas.
            """
            bono = Empleado(self.nombre, self.identificacion, self.anios_servicio).calcular_bono_antiguedad()
            salario = (self.tarifa_hora * self.horas_trabajadas) + bono
            return salario

# Clase Empresa para gestionar la lista de empleados y la generación de la planilla de pago
class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        """
        Agrega un empleado a la lista de la empresa.
        """
        self.empleados.append(empleado)

    def generar_planilla(self):
        """
        Genera la planilla de pago para todos los empleados.
        """
        planilla = {}
        for empleado in self.empleados:
            planilla[empleado.nombre] = empleado.calcular_salario()
        return planilla


if __name__ == "__main__":
    # Crear una empresa
    empresa = Empresa("Tech Solutions")

    # Crear empleados
    emp1 = Empleado.EmpleadoFijo("Melvin Pérez", "001", 6, 2000, 300)
    emp2 = Empleado.EmpleadoPorHoras("Gustavo Gómez", "002", 3, 20, 120)
    emp3 = Empleado.EmpleadoFijo("Alexander Hernández", "003", 4, 1800, 200)
    emp4 = Empleado.EmpleadoPorHoras("Elmer  Ruiz", "004", 8, 25, 100)

    # Agregar empleados a la empresa
    empresa.agregar_empleado(emp1)
    empresa.agregar_empleado(emp2)
    empresa.agregar_empleado(emp3)
    empresa.agregar_empleado(emp4)

    # Se Generar la planilla de pago
    planilla = empresa.generar_planilla()

    # Aca se muestra la planilla
    for nombre, salario in planilla.items():
        print(f"{nombre}: ${salario:.2f}")
