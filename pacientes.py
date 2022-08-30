class persona:
    def __init__(self, nombre, edad, periodos, matriz, celdas_cont):
        self.nombre = nombre
        self.edad = edad
        self.periodos = periodos
        self.matriz = matriz
        self.celdas_cont = celdas_cont

    def mostrarInfo(self):
        print('los datos de la persona son los siguientes')
        print('nombre :' + self.nombre)
        print('Edad: ' + self.edad)
        print('Periodos: ' + self.periodos)
        print('Matriz: ' + self.matriz)
        print('Celdas contagiadas: ' + self.celdas_cont)