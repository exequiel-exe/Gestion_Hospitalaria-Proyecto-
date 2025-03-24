class NodoLista:
    """Clase nodo de una lista doblemente enlazada."""
    def __init__(self, info=None, sig=None, ant=None):
        self.info = info
        self.sig = sig  # Puntero al siguiente nodo
        self.ant = ant  # Puntero al nodo anterior

class Lista:
    """Clase para una lista doblemente enlazada."""
    def __init__(self):
        """Crea una lista vacía."""
        self.inicio = None
        self.fin = None
        self.tamanio = 0
    def insertar_ordenado(self, dato):
            """Inserta el dato pasado en la lista de manera ordenada."""
            nodo = NodoLista(dato)
            if self.inicio is None or self.inicio.info > dato:
                nodo.sig = self.inicio
                self.inicio = nodo
            else:
                ant = self.inicio
                act = self.inicio.sig
                while act is not None and act.info < dato:
                    ant = act
                    act = act.sig
                nodo.sig = act
                ant.sig = nodo
            self.tamanio += 1

    def insertar(self, dato):
        """Inserta el dato pasado al final de la lista."""
        nodo = NodoLista(dato)
        if self.inicio is None:
            # Si la lista está vacía, el nuevo nodo es el primer y único nodo
            self.inicio = nodo
            self.fin = nodo
        else:
            # Añadir el nuevo nodo al final de la lista
            nodo.ant = self.fin
            self.fin.sig = nodo
            self.fin = nodo
        self.tamanio += 1

    def lista_vacia(self):
        """Devuelve True si la lista está vacía."""
        return self.inicio is None

    def eliminar(self, clave):
        """Elimina un elemento de la lista y lo devuelve si lo encuentra."""
        actual = self.inicio
        while actual is not None and actual.info != clave:
            actual = actual.sig

        if actual is None:
            # No se encontró el elemento
            return None

        # Si el nodo a eliminar es el único nodo en la lista
        if actual == self.inicio and actual == self.fin:
            self.inicio = None
            self.fin = None
        elif actual == self.inicio:
            # Si el nodo a eliminar es el primer nodo
            self.inicio = self.inicio.sig
            self.inicio.ant = None
        elif actual == self.fin:
            # Si el nodo a eliminar es el último nodo
            self.fin = self.fin.ant
            self.fin.sig = None
        else:
            # Si el nodo a eliminar está en medio
            actual.ant.sig = actual.sig
            actual.sig.ant = actual.ant

        self.tamanio -= 1
        return actual.info
    
    def mostrar(self, posicion):
        """Devuelve el valor del nodo en una posición específica sin eliminarlo."""
        if posicion < 0 or posicion >= self.tamanio:
            # Si la posición es inválida (fuera del rango), retorna None
            return None

        actual = self.inicio
        indice = 0

        # Recorre la lista hasta llegar a la posición deseada
        while indice < posicion:
            actual = actual.sig
            indice += 1

        # Devuelve el valor del nodo en la posición especificada
        return actual.info

    def obtener_tamanio(self):
        """Devuelve el número de elementos en la lista."""
        return self.tamanio

    def buscar(self, buscado):
        """Devuelve la dirección del nodo que contiene el elemento buscado."""
        aux = self.inicio
        while aux is not None and aux.info != buscado:
            aux = aux.sig
        return aux

    def barrido_adelante(self):
        """Recorre la lista desde el inicio hacia el final mostrando sus valores."""
        aux = self.inicio
        while aux is not None:
            print(aux.info)
            aux = aux.sig

    def barrido_atras(self):
        """Recorre la lista desde el final hacia el inicio mostrando sus valores."""
        aux = self.fin
        while aux is not None:
            print(aux.info)
            aux = aux.ant
    def modificar_nodo(self, posicion, nuevo_valor):
        """Modifica el valor del nodo en la posición dada con el nuevo valor."""
        if posicion < 0 or posicion >= self.tamanio:
            # Si la posición es inválida (fuera del rango)
            print("Posición inválida")
            return False

        actual = self.inicio
        indice = 0

        # Recorre la lista hasta llegar al nodo en la posición especificada
        while indice < posicion:
            actual = actual.sig
            indice += 1

        # Modificar el valor del nodo en la posición indicada
        actual.info = nuevo_valor
        print(f"Nodo en posición {posicion} modificado a {nuevo_valor}")
        return True
    def eliminar_por_posicion(self, posicion):
        """Elimina un nodo en una posición específica."""
        if posicion < 0 or posicion >= self.tamanio:
            print("Posición inválida")
            return None  # Si la posición es inválida, no se puede eliminar

        actual = self.inicio
        indice = 0

        # Recorre la lista hasta llegar al nodo en la posición especificada
        while indice < posicion:
            actual = actual.sig
            indice += 1

        # Ahora 'actual' es el nodo en la posición deseada, lo eliminamos
        if actual == self.inicio and actual == self.fin:
            # Si el nodo a eliminar es el único nodo en la lista
            self.inicio = None
            self.fin = None
        elif actual == self.inicio:
            # Si el nodo a eliminar es el primer nodo
            self.inicio = self.inicio.sig
            self.inicio.ant = None
        elif actual == self.fin:
            # Si el nodo a eliminar es el último nodo
            self.fin = self.fin.ant
            self.fin.sig = None
        else:
            # Si el nodo a eliminar está en medio
            actual.ant.sig = actual.sig
            actual.sig.ant = actual.ant

        self.tamanio -= 1
        return actual.info  # Devuelve el valor del nodo eliminado

    def obtener_ultimo(self):
        """Devuelve el valor del último nodo de la lista."""
        if self.fin is not None:
            return self.fin.info
        return None  # Si la lista está vacía, se devuelve None

    @staticmethod
    def criterio(dato, campo=None):
        """Determina el campo por el cual se debe comparar el dato."""
        dic = getattr(dato, '__dict__', {})
        if campo is None or campo not in dic:
            return dato
        return dic[campo]
