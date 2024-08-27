#"""Un colegio privado desea registrar la asistencia de sus estudiantes a las
#clases cada docente tiene su listado de los estudiantes en los cuáles se
#les ha solicitado colocar a la par de cada estudiante si ha asistido, si
#cuenta con permiso o tiene inasistencia con la fecha respectiva.
#Actualmente esto se maneja por unas hojas de papel impreso y se
#entregan al director al final del día; la escuela necesita agilizar este
#proceso.
#Si el estudiante tiene un permiso el director necesita la razón de
#dicha falta, ¿Cómo solventarías esta situación? Agrega tu
#propuesta al código."""


#desarrollo:
#Creamos una clase Estudiante con atributos como nombre, identificación y un registro de asistencias y ademas 
#Implementamos una clase Docente que maneje la lista de estudiantes que permiste registrar la asistencia 
#con detalles como fecha y razón de la falta.



from datetime import datetime

class Estudiante:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
        self.registro_asistencias = []

    def registrar_asistencia(self, estado, razon=None):
        """
        Registra la asistencia del estudiante con la fecha actual.
        
        :param estado: "Presente", "Ausente" o "Permiso".
        :param razon: Razón de la falta o permiso, si aplica.
        """
        asistencia = {
            'fecha': datetime.now().strftime('%Y-%m-%d'),
            'estado': estado,
            'razon': razon
        }
        self.registro_asistencias.append(asistencia)
        print(f"Registrada asistencia para {self.nombre}: {estado} el {asistencia['fecha']}")

    def obtener_asistencias(self):
        """
        Devuelve el registro de asistencias del estudiante.
        """
        return self.registro_asistencias

class Docente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        """
        Agrega un estudiante a la lista de estudiantes del docente.
        
        :param estudiante: Instancia de la clase Estudiante.
        """
        self.estudiantes.append(estudiante)

    def registrar_asistencia_estudiante(self, identificacion_estudiante, estado, razon=None):
        """
        Registra la asistencia de un estudiante según su identificación.
        
        :param identificacion_estudiante: Identificación del estudiante.
        :param estado: "Presente", "Ausente" o "Permiso".
        :param razon: Razón de la falta o permiso, si aplica.
        """
        for estudiante in self.estudiantes:
            if estudiante.identificacion == identificacion_estudiante:
                estudiante.registrar_asistencia(estado, razon)
                break
        else:
            print(f"Estudiante con ID {identificacion_estudiante} no encontrado.")

    def generar_informe_diario(self):
        """
        Genera un informe diario de asistencias para todos los estudiantes.
        """
        informe = {}
        for estudiante in self.estudiantes:
            informe[estudiante.nombre] = estudiante.obtener_asistencias()
        return informe


if __name__ == "__main__":
    # Crear un docente
    docente = Docente("Profe Juan")

    # Aca sse crean los estudiantes
    est1 = Estudiante("Carlos García", "001")
    est2 = Estudiante("María López", "002")
    est3 = Estudiante("Lucía Hernández", "003")

    # Agreagar los estudiantes al docente
    docente.agregar_estudiante(est1)
    docente.agregar_estudiante(est2)
    docente.agregar_estudiante(est3)

    # Registrar asistencias
    docente.registrar_asistencia_estudiante("001", "Presente")
    docente.registrar_asistencia_estudiante("002", "Permiso", "Cita médica")
    docente.registrar_asistencia_estudiante("003", "Ausente")

    # Aqui se Generar informe de cada dia 
    informe = docente.generar_informe_diario()
    for estudiante, asistencias in informe.items():
        print(f"\nAsistencias de {estudiante}:")
        for asistencia in asistencias:
            print(f"Fecha: {asistencia['fecha']}, Estado: {asistencia['estado']}, Razón: {asistencia['razon']}")
