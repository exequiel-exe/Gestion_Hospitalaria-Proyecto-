import time
import os

class NodoCola:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None  # Puntero al nodo anterior


class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0

    # Método para agregar un nodo a la cola (arribo)
    def arribo(self, dato):
        nodo = NodoCola(dato)
        if self.cola_vacia():
            self.frente = nodo
            self.final = nodo
            nodo.siguiente = nodo
            nodo.anterior = nodo
        else:
            nodo.anterior = self.final
            nodo.siguiente = self.frente
            self.final.siguiente = nodo
            self.frente.anterior = nodo
            self.final = nodo
        self.tamanio += 1

    # Método para retirar el nodo del frente (atencion)
    def atencion(self):
        if not self.cola_vacia():
            dato = self.frente.dato
            if self.frente == self.final:
                self.frente = None
                self.final = None
            else:
                self.frente = self.frente.siguiente
                self.frente.anterior = self.final
                self.final.siguiente = self.frente
            self.tamanio -= 1
            return dato
        else:
            return None

    # Método para verificar si la cola está vacía
    def cola_vacia(self):
        return self.frente is None

    # Método para obtener el tamaño de la cola
    def tamanio_cola(self):
        return self.tamanio

    # Método para barrer la cola hacia adelante
    def barrido_adelante(self):
        if not self.cola_vacia():
            aux = self.frente
            while True:
                print(aux.dato)
                aux = aux.siguiente
                if aux == self.frente:
                    break
        else:
            print("La cola está vacía")

    # Método para barrer la cola hacia atrás
    def barrido_atras(self):
        if not self.cola_vacia():
            aux = self.final
            while True:
                print(aux.dato)
                aux = aux.anterior
                if aux == self.final:
                    break
        else:
            print("La cola está vacía")

    # Método para barrido circular hacia adelante (recorre la cola indefinidamente)
    def barrido_adelante_circular(self, veces):
        if not self.cola_vacia():
            aux = self.frente
            count = 0
            while count < veces:
                print(aux.dato)
                aux = aux.siguiente
                if aux == self.frente:
                    count += 1
        else:
            print("La cola está vacía")

    # Método para barrido circular hacia atrás (recorre la cola indefinidamente)
    def barrido_atras_circular(self, veces):
        if not self.cola_vacia():
            aux = self.final
            count = 0
            while count < veces:
                print(aux.dato)
                aux = aux.anterior
                if aux == self.final:
                    count += 1
        else:
            print("La cola está vacía")

    def barrido_con_tiempo(self, intervalo,nombre):
            if not self.cola_vacia():
              aux = self.frente
            while aux:
                    os.system('cls')
                    print(nombre)
                    print(aux.dato)
                    time.sleep(intervalo)  # Espera 'intervalo' segundos antes de procesar el siguiente nodo
                    aux = aux.siguiente
            else:
              print("La cola está vacía")
              
    def carga_int(cola, nom):
        entrada = input(f"\n\tIngrese 1 para cargarle un dato a la cola {nom}: ")
        entrada = int(entrada)
        while entrada == 1:
            dato = input("\n\t\tIngrese el dato: ")
            dato = int(dato)
            cola.arribo(dato)
            entrada = input("\n\t\tIngrese 1 para cargarle un dato a la cola / 0 para salir: ")
            entrada = int(entrada)
        return cola
    
    def carga_str(cola, nom):
        entrada = input(f"\n\tIngrese 1 para cargarle un dato a la cola {nom}: ")
        entrada = int(entrada)
        while entrada == 1:
            dato = input("\n\t\tIngrese el dato: ")
            cola.arribo(dato)
            entrada = input("\n\t\tIngrese 1 para cargarle un dato a la cola / 0 para salir: ")
            entrada = int(entrada)
        return cola