from funcionalidad.tda.tda_lista import *
from funcionalidad.auxiliar import *
from funcionalidad.tda.tda_pila import *

def cargar_cita(datos, citas):
    cita = Lista()
    tamanio = citas.obtener_tamanio()
    id_cita = cargar_datos("id_cita")
    if id_cita.pila_vacia():
        id = 1
        id_cita.apilar(id)
        guardar_datos("id_cita", id_cita)
    else:
        ultimo = id_cita.en_cima()
        id = ultimo + 1
        id_cita.apilar(id)
        guardar_datos("id_cita", id_cita)
    nombre_paciente = datos['nombre_paciente']
    nombre_medico = datos['nombre_medico']
    fecha_cita = datos['fecha_cita']
    estado = datos['estado']
    cita.insertar(id)
    cita.insertar(nombre_paciente)
    cita.insertar(nombre_medico)
    cita.insertar(fecha_cita)
    cita.insertar(estado)
    cita.barrido_adelante()
    return cita

def buscar_cita(id, citas):
    posicion = obtener_posicion(id)
    citas.mostrar(posicion)

def obtener_posicion(id):
    citas = cargar_datos('citas')
    tamanio = citas.obtener_tamanio()
    print(tamanio, "tamanino")
    for i in range (tamanio):
        cita = citas.mostrar(i)
        cita.barrido_adelante()
        compara = cita.mostrar(0)
        print(compara)
        if id == compara:
            cita.barrido_adelante()
            print(i)
            return int(i)
         
    return None

