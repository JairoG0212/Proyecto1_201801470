

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

    def crear_indice_vert(self, posVertical):
        #se recorren los nodos de manera vertical