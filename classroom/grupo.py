from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, listadoALumnos=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = listadoALumnos

    def listadoAsignaturas(self, **kwargs):
        if self._asignaturas == None:
            self._asignaturas = []
        for x in kwargs.values(): 
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista == None:
            lista = []
        if self.listadoAlumnos == None:
            self.listadoAlumnos = []
        lista.append(alumno)
        self.listadoAlumnos+=lista

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}"

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
