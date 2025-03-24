from funcionalidad.auxiliar import *
from funcionalidad.tda.tda_arbol import *


# Definición de la clase Cama
class Cama:
    def __init__(self, prioridad, numero, disponibilidad):
        self.data = (prioridad, numero, disponibilidad)

    def __lt__(self, other):
        if self.data[0] == other.data[0]:
            return self.data[1] < other.data[1]
        return self.data[0] < other.data[0]

    def __gt__(self, other):
        if self.data[0] == other.data[0]:
            return self.data[1] > other.data[1]
        return self.data[0] > other.data[0]

    def __eq__(self, other):
        return self.data == other.data

    def __str__(self):
        return f"Cama: Prioridad={self.data[0]}, Número={self.data[1]}, Disponible={self.data[2]}"

def iniciar_arbol():
    # Crear la lista de camas 
    camas = []
    for i in range(1, 26):
        prioridad = (i - 1) // 5 + 1  # Calcular prioridad basada en el número de cama
        camas.append(Cama(prioridad, i, True))
    # Crear e insertar las camas en el árbol
    raiz = None
    for cama in camas:
        raiz = insertar_nodo(raiz, cama)
    # Verificar el árbol con un recorrido inorden
    print("Camas ordenadas por prioridad y número:")
    inorden(raiz)
    return raiz
def asignar_cama_por_prioridad(raiz, prioridad):
    """Asigna una cama de acuerdo a la prioridad, buscando primero en la misma prioridad,
       y en niveles inferiores si el paciente tiene alta prioridad (prioridad menor)."""
    
    # Si el paciente tiene alta prioridad, primero busca en su nivel y luego en niveles inferiores
    if prioridad < 5:  # Prioridades altas, se permite ocupar camas de menor prioridad si no hay disponibles
        cama_asignada = None
        raiz, cama_asignada = buscar_cama(raiz, prioridad)
        if cama_asignada:
            return raiz, cama_asignada  # Cama encontrada y ocupada en el nivel solicitado
        
        # Si no hay cama disponible en esa prioridad, buscamos en niveles inferiores
        for p in range(prioridad + 1, 6):
            raiz, cama_asignada = buscar_cama(raiz, p)
            if cama_asignada:
                return raiz, cama_asignada  # Cama encontrada y ocupada en un nivel inferior
    
    # Si el paciente tiene baja prioridad, solo puede ocupar camas en su mismo nivel de prioridad
    elif prioridad == 5:
        raiz, cama_asignada = buscar_cama(raiz, prioridad)
        if cama_asignada:
            return raiz, cama_asignada  # Cama encontrada y ocupada en su nivel de prioridad
        # Si no hay cama disponible en esa prioridad, no se asigna ninguna cama
        else:
            return raiz, None
    
    # Si no se encontró cama en la prioridad correspondiente, no se asigna ninguna cama
    return raiz, None

def buscar_cama(raiz, prioridad):
    """Busca la primera cama libre con la prioridad especificada y la asigna, devolviendo la raíz modificada."""
    if raiz is None:
        return raiz, None  # No hay camas disponibles en este subárbol

    # Si encontramos una cama con la prioridad correcta y disponible
    if raiz.dato.data[0] == prioridad and raiz.dato.data[2]:
        # Marca la cama como ocupada
        raiz.dato.data = (raiz.dato.data[0], raiz.dato.data[1], False)
        return raiz, raiz.dato.data[1]  # Devuelve la raíz modificada y el número de la cama asignada

    # Recursivamente buscamos en el subárbol izquierdo o derecho
    if prioridad < raiz.dato.data[0]:
        raiz.izq, cama_asignada = buscar_cama(raiz.izq, prioridad)
        return raiz, cama_asignada
    
    raiz.der, cama_asignada = buscar_cama(raiz.der, prioridad)
    return raiz, cama_asignada

def cambiar_disponibilidad(raiz, numero_cama):
    if raiz is None:
        return None  # Si el árbol está vacío o no se encuentra la cama, no hacemos nada

    # Compara el número de cama con el número de la raíz
    if raiz.dato.data[1] == numero_cama:
        # Si la cama está ocupada (disponibilidad=False), la cambiamos a True
        if raiz.dato.data[2] == False:
            raiz.dato.data = (raiz.dato.data[0], raiz.dato.data[1], True)  # Cambiar a disponible
            return raiz  # Retornar el árbol con el nodo modificado
        else:
            # Si la cama ya está disponible, no hacemos ningún cambio
            return None

    # Si el número de cama es menor, buscamos en el subárbol izquierdo
    elif numero_cama < raiz.dato.data[1]:
        raiz.izq = cambiar_disponibilidad(raiz.izq, numero_cama)
        return raiz if raiz.izq is not None else None

    # Si el número de cama es mayor, buscamos en el subárbol derecho
    else:
        raiz.der = cambiar_disponibilidad(raiz.der, numero_cama)
        return raiz if raiz.der is not None else None
