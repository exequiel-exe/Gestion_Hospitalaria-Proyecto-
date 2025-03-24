from funcionalidad.tda.tda_cola import *

class NodoArbol(object):
    """Clase nodo árbol."""
    
    def __init__(self, dato):
        """Crea un nodo con la información cargada."""
        self.izq = None
        self.der = None
        self.dato = dato

def eliminar_nodo(raiz, clave):
    """Elimina un elemento del árbol y lo devuelve si lo encuentra."""
    x = None
    if raiz is not None:
        if clave < raiz.dato:
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif clave > raiz.dato:
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.dato
            if raiz.izq is None:
                raiz = raiz.der
            elif raiz.der is None:
                raiz = raiz.izq
            else:
                raiz.izq, aux = reemplazar(raiz.izq)
                raiz.dato = aux.dato
    return raiz, x

def insertar_nodo(raiz, dato):
    """Inserta un dato al árbol."""
    if raiz is None:
        raiz = NodoArbol(dato)
    elif dato < raiz.dato:
        raiz.izq = insertar_nodo(raiz.izq, dato)
    else:
        raiz.der = insertar_nodo(raiz.der, dato)
    return raiz

def arbol_vacio(raiz):
    """Devuelve True si el árbol está vacío."""
    return raiz is None

def reemplazar(raiz):
    """Determina el nodo que reemplazará al que se elimina."""
    aux = None
    if raiz.der is None:
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = reemplazar(raiz.der)
    return raiz, aux

def por_nivel(raiz):
    """Realiza el barrido por nivel del árbol."""
    pendientes = Cola()
    pendientes.arribo(raiz)
    while not pendientes.cola_vacia():
        nodo = pendientes.atencion()
        print(nodo.dato)
        if nodo.izq is not None:
            pendientes.arribo(nodo.izq)
        if nodo.der is not None:
            pendientes.arribo(nodo.der)

def buscar(raiz, clave):
    """Devuelve la dirección del elemento buscado."""
    pos = None
    if raiz is not None:
        if raiz.dato == clave:
            pos = raiz
        elif clave < raiz.dato:
            pos = buscar(raiz.izq, clave)
        else:
            pos = buscar(raiz.der, clave)
    return pos

def inorden(raiz):
    """Realiza el barrido inorden del árbol."""
    if raiz is not None:
        inorden(raiz.izq)
        print(raiz.dato)
        inorden(raiz.der)

def preorden(raiz):
    """Realiza el barrido preorden del árbol."""
    if raiz is not None:
        print(raiz.dato)
        preorden(raiz.izq)
        preorden(raiz.der)

def postorden(raiz):
    """Realiza el barrido postorden del árbol."""
    if raiz is not None:
        postorden(raiz.izq)
        print(raiz.dato)
        postorden(raiz.der)
