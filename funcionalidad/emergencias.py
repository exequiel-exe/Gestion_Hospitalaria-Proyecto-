from funcionalidad.auxiliar import *
from funcionalidad.tda.tda_cola import *


def cargar_emergencia(datos, emergencias):
    print(datos, "los datos")
    emergencias.barrido_adelante()
    nombre_paciente = datos['nombre_paciente']
    print(nombre_paciente)
    return nombre_paciente


    