from funcionalidad.auxiliar import *
from funcionalidad.citas import *
from funcionalidad.tda.tda_pila import *
from funcionalidad.tda.tda_cola import *


def cita_historial(cita):
    historial = cargar_datos('historial')
    lista = []
    lista.append(cita.mostrar(0))
    lista.append(cita.mostrar(1))
    lista.append(cita.mostrar(2))
    lista.append(cita.mostrar(3))
    lista.append(cita.mostrar(4))
    historial.apilar(lista)
    historial.barrido()
    guardar_datos('historial', historial)

def historial_emergencia(siguiente):
    historial = cargar_datos('historial')
    lista = []
    lista.append(siguiente)
    historial.apilar(lista)
    historial.barrido()
    guardar_datos('historial', historial)

def mostrar_historial():
    pilaux = Pila()
    historial = cargar_datos('historial')
    tamanio = historial.obtener_tamanio()
    mostrar = []
    for i in range(tamanio):
        dato = historial.desapilar()
        mostrar.append(dato)
        pilaux.apilar(dato)
    for i in range(tamanio):
        dato = pilaux.desapilar()
        historial.apilar(dato)
    historial.barrido(), print("Historial")
    return mostrar

def deshacer():
    historial = cargar_datos('historial')
    tamanio = historial.obtener_tamanio()
    if tamanio != 0:
        ultima = historial.desapilar()
        if len(ultima) == 1:
            emergencias = cargar_datos('emergencias')
            emergencias.arribo(ultima[0])
            guardar_datos('emergencias', emergencias)
            emergencias.barrido_adelante()
            print("es emergencia")
        elif len(ultima) == 5:
            citas = cargar_datos('citas')
            id = ultima[0]
            posicion = obtener_posicion(id)
            estado = "Pendiente"
            if posicion != None:
                cita = citas.mostrar(posicion)
                cita.barrido_adelante(), print("cita a modificar")
                cita.modificar_nodo(4, estado)
                cita.barrido_adelante(), print("modificado")
                guardar_datos("citas", citas)
                print(posicion)
                print(id)
            else:
                print(ultima[0])
                cita = Lista()
                cita.insertar(ultima[0])
                cita.insertar(ultima[1])
                cita.insertar(ultima[2])
                cita.insertar(ultima[3])
                cita.insertar(estado)
                cita.barrido_adelante()
                citas.insertar(cita)
                guardar_datos("citas", citas)
        guardar_datos('historial', historial)# Suponiendo que el estado está en la posición 4
        return True
    else:
        return False

       