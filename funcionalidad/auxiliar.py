import pickle
from funcionalidad.camas import *
from funcionalidad.tda.tda_lista import *
from funcionalidad.tda.tda_cola import *
from funcionalidad.tda.tda_pila import *
from funcionalidad.tda.tda_arbol import *


import pickle

def validating_existence(file_name, tipo):
    try:
        # Intenta abrir el archivo en modo lectura/escritura binaria
        with open(file_name, "rb+"):
            pass  # Si el archivo existe, no se hace nada
    except IOError:
        if tipo == "lista":
            # Si no existe, lo crea e inicializa con una instancia de la TAD Lista
            lista_vacia = Lista()  # Crear una lista vacía usando la TAD
            with open(file_name, "wb") as file:
                pickle.dump(lista_vacia, file)  # Guardar la lista en el archivo
            print(f"Archivo '{file_name}' creado e inicializado con una lista vacía de TAD.")
        elif tipo == "cola":
            # Si no existe, lo crea e inicializa con una instancia de la TAD Cola
            cola_vacia = Cola()  # Crear una cola vacía usando la TAD
            with open(file_name, "wb") as file:
                pickle.dump(cola_vacia, file)  # Guardar la cola en el archivo
            print(f"Archivo '{file_name}' creado e inicializado con una cola vacía de TAD.")
        elif tipo == "pila":
            # Si no existe, lo crea e inicializa con una instancia de la TAD Pila
            pila_vacia = Pila()  # Crear una pila vacía usando la TAD
            with open(file_name, "wb") as file:
                pickle.dump(pila_vacia, file)  # Guardar la pila en el archivo
            print(f"Archivo '{file_name}' creado e inicializado con una pila vacía de TAD.")
        elif tipo == "arbol":
            # Si no existe, lo crea como un archivo vacío (sin ningún formato de datos)
            with open(file_name, "wb") as file:
                pass  # No se guarda nada, solo se crea el archivo vacío
            raiz = iniciar_arbol()
            guardar_datos('asignacion_camas', raiz)  
            print(f"Archivo '{file_name}' creado como para el TAD Árbol.")
        else:
            print(f"Tipo de archivo invalido.")
       

def cargar_datos(file_name):
    try:
        with open(file_name, "rb") as file:
            datos = pickle.load(file)
        print(f"Datos cargados correctamente desde '{file_name}'.")
        return datos
    except FileNotFoundError:
        print(f"El archivo '{file_name}' no existe. Asegúrate de crearlo primero.")
        return None
    except EOFError:
        print(f"El archivo '{file_name}' está vacío.")
        return None
    except Exception as e:
        print(f"Error al cargar el archivo '{file_name}': {e}")
        return None

def guardar_datos(file_name, datos):
    try:
        with open(file_name, "wb") as file:
            pickle.dump(datos, file)
        print(f"Datos guardados correctamente en '{file_name}'.")
    except Exception as e:
        print(f"Error al guardar datos en el archivo '{file_name}': {e}")

def inicio_archivos():
    validating_existence("citas", "lista")
    validating_existence("emergencias", "cola")
    validating_existence("historial", "pila")
    validating_existence("asignacion_camas", "arbol")
    validating_existence("id_cita", "pila")
 
