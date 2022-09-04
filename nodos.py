

from tkinter import N


class Nodo:
    def __init__(self):
        self.dato = None
        #Coordenadas
        self.posVertical = None
        self.posHorizontal = None
        #apuntadores
        self.derecha = None
        self.izquierda = None
        self.arriba = None
        self.abajo = None

class matriz_ortogonal:
    def __init__(self):
        #creacion el nodo inicial en la posicion 0,0
        self.raiz = Nodo()
        self.raiz.posHorizontal = 0
        self.raiz.posVertical = 0

    def crear_indice_vert(self, posVert):
        #se recorren los nodos de manera vertical
        #se creara un nodo temporal para llevar el control 
        temp = self.raiz
        while temp != None:
            #no existe el indice; solo hay indices menores
            if temp.abajo == None and temp.posVertical < posVert:
                #ya no hay mas nodos en vertical
                #se inserta al final
                nuevo = Nodo()
                nuevo.posHorizontal = 0
                nuevo.posVertical = posVert
                nuevo.arriba = temp
                temp.abajo = nuevo
                return temp.abajo

            #el indice actual es igual a el nuevo indice
            if temp.posVertical == posVert:
                #no hacer nada
                return temp
            
            #si no valida ningun if pasa al siguiente temporal
            temp=temp.abajo

    def crear_indice_hori(self, posHori):
        # recorrer todos los nodos de manera horizontal
        tmp = self.raiz
        while tmp != None:
            # no existe el indice; solo hay índices menores
            if tmp.derecha == None and tmp.posHorizontal < posHori:
                # ya no hay más nodos en horizontal
                # se inserta al final
                nuevo = Nodo()
                nuevo.posHorizontal = posHori
                nuevo.posVertical = 0
                nuevo.izquierda = tmp
                tmp.derecha = nuevo
                return tmp.derecha

            #indice actual es igual a el nuevo indice
            if tmp.posHorizontal == posHori:
                #no hacer nada
                return tmp

    def insert_vert(self, nodo, indice_Hori):
        #recorre todo los nodos de manera horizontal para que al encontrar el nodo, inserte en vertical
        tmp = indice_Hori
        while tmp != None:
            #no existe el indice; solo hay indices menores
            if tmp.abajo == None and tmp.posVertical < nodo.posVertical:
                #ya no hay mas nodos en vertical
                #se inserta al final
                nodo.arriba = tmp
                tmp.abajo = nodo
                return tmp.abajo

            #indice actual es igual a el nuevo indice
            if tmp.posVertical == nodo.posVertical:
                #no hacer nada, el dato solo se sobre escribe
                tmp.dato = nodo.dato
                return tmp

            #indice actual es menor, pero el siguiente es mayor
            if tmp.posVertical < nodo.posVertical and tmp.abajo.posVertical > nodo.posVertical:
                #insertar un nodo en medio del nodo actual y del nodo siguiente 

                #asignar abajo y arriba para el nuevo nodo
                nodo.abajo = tmp.abajo
                nodo.arriba = tmp

                tmp.abajo.arriba = nodo
                tmp.abajo = nodo
                return tmp.abajo

            #pasar al siguiente nodo abajo si no hubo return
            tmp = tmp.abajo
            
    def insert_hori(self, nodo, indice_vert):
        # recorrer todos los nodos en horizontal
        tmp = indice_vert
        while tmp != None:
            # no existe el indice; solo hay índices menores
            if tmp.derecha == None and tmp.posHorizontal < nodo.posHorizontal:
                # ya no hay más nodos en horizontal
                # se inserta al final
                nodo.izquierda  = tmp
                tmp.derecha = nodo
                return tmp.derecha
            
            # indice actual es igual a el nuevo índice
            if tmp.posHorizontal == nodo.posHorizontal :
                # no hacer nada se sobre escribe
                tmp.dato = nodo.dato
                return tmp

            # indice actual es menor, pero el siguiente es mayor
            if tmp.posHorizontal < nodo.posHorizontal and tmp.derecha.posHorizontal > nodo.posHorizontal:
                # insertar un nodo en medio del nodo actual y del nodo siguiente
                # asignar derecha y arriba para el nodo nuevo
                nodo.derecho = tmp.derecha
                nodo.izquierda = tmp
                
                tmp.derecha.izquierda = nodo # reasignar arriba para el nodo de derecha
                tmp.derecha = nodo # reasignar derecha para el nodo actual
                return tmp.derecha
                
            # pasar al siguiente nodo derecha si esque no hubo return
            tmp = tmp.derecha

    def insertarDato(self,dato,  posVertical, posHorizontal):
        # validar que los índices existan en horizontal y vertical
        indiceVertical = self.crear_indice_vert(posVertical)
        indiceHorizontal = self.crear_indice_hori(posHorizontal)

        # crear el nodo valor
        nuevo = Nodo()
        nuevo.posHorizontal = posHorizontal
        nuevo.posVertical = posVertical
        nuevo.dato = dato

        # indexar/apuntar nodo nuevo en indice vertical
        nuevo = self.insert_vert(nuevo, indiceHorizontal) 
        nuevo = self.insert_hori(nuevo, indiceVertical)
        print("Nodo insertado...")
        pass