class nodoPila:
    """Clase nodo pila"""
    
    def __init__(self):
        self.info, self.sig = None, None

class Pila:
    """Clase Pila"""
    def __init__(self):
        """Crear Pila vacía"""
        self.cima = None
        self.tamanio = 0
    
    def apilar(self, dato):
        """Apila el dato sobre la cima de la Pila"""
        nodo = nodoPila()
        nodo.info = dato
        nodo.sig = self.cima
        self.cima = nodo
        self.tamanio += 1
    
    def desapilar(self):
        """Desapila el elemento en la cima de la pila y lo devuelve"""
        x = self.cima.info
        self.cima = self.cima.sig
        self.tamanio -= 1
        return x
    
    def pila_vacia(self):
        """Devuelve true si la pila esta vacía"""
        return self.cima is None
    
    def en_cima(self):
        """Devuelve el valor almacenado en la cima de la pila"""
        if self.cima is not None:
            return self.cima.info
        else:
            return None
    
    def obtener_tamanio(self):
       """Devuelve elmero de elementos en la pila"""
       return self.tamanio
    
    def barrido(self):
        """Muestra el contenido de una pila sin perder datos"""
        paux = Pila()
        while not self.pila_vacia():
            dato = self.desapilar()
            print(dato)
            paux.apilar(dato)
        while not paux.pila_vacia():
            dato = paux.desapilar()
            self.apilar(dato)


