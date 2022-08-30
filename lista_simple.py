class node:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente: node = None

class listaSimple:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    #creacion de metodo que obtendra el tamaño de la lista nodo para poderla iterar
    def size(self):
        if self.primero is None:
            return 0

        aux = self.primero
        the_size = 0
        while aux is not None:
            the_size += 1
            aux = aux.siguiente
        return the_size

    #metodo para anadir nodo al final
    def añadirNodoFinal(self, dato):
        #para anadir nodo primero se debera crear
        nuevoNodo = node(dato)

        #preguntar si la lista esta vacia 
        #si la lista esta vacia
        if self.primero == None:
            print('insertando al inicio')
            self.primero = nuevoNodo
            self.ultimo = nuevoNodo

        #si la lista no esta vacia
        else:
            self.ultimo.siguiente = nuevoNodo
            self.ultimo = nuevoNodo

    
    def impirmirListaSimple(self):
        print('Inicio de lista\n')
        #se debe crear un nodo temporal para poder recorrer esta lista y poder imprimirlo
        print()
        nodoTemporal = self.primero
        #creacion de contador para ver el numero de nodos
        contador = 0

        #se usara un ciclo while para que sea diferente de nulo
        while nodoTemporal != None:
            contador += 1
            print(f'Nodo No#{contador} --> valor:{nodoTemporal.dato}')
            nodoTemporal = nodoTemporal.siguiente

        print('\nFin de la lista\n')