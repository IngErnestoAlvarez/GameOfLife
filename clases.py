class Celda(object):

    def __init__(self):
        self.viva = False
        self.siguiente = False
        self.vecinas = []

    def intentar_revivir(self):
        contador = 0

        if self.viva:
            for i in self.vecinas:
                if i.viva:
                    contador += 1
            if contador == 2 or contador == 3:
                self.siguiente = True
                return True
            else:
                self.siguiente = False
                return False
        else:
            for i in self.vecinas:
                if i.viva:
                    contador += 1
            if contador == 3:
                self.siguiente = True
                return True
            else:
                self.siguiente = False
                return False


class Grilla(object):

    def __init__(self, x, y):
        self.columnas = x
        self.filas = y
        self.matriz = []
        for j in range(y):
            self.matriz.append([])
            for i in range(x):
                celda = Celda()
                self.matriz[j].append(celda)

        for i in range(y):
            for j in range(x):
                if i > 0 and j > 0:
                    self.matriz[i][j].vecinas.append(self.matriz[i-1][j-1])
                if i > 0:
                    self.matriz[i][j].vecinas.append(self.matriz[i-1][j])
                if j > 0:
                    self.matriz[i][j].vecinas.append(self.matriz[i][j - 1])
                if i < y-1:
                    self.matriz[i][j].vecinas.append(self.matriz[i+1][j])
                if j < x-1:
                    self.matriz[i][j].vecinas.append(self.matriz[i][j+1])
                if i > 0 and j < x-1:
                    self.matriz[i][j].vecinas.append(self.matriz[i-1][j+1])
                if i < y-1 and j > 0:
                    self.matriz[i][j].vecinas.append(self.matriz[i+1][j-1])
                if i < y-1 and j < x-1:
                    self.matriz[i][j].vecinas.append(self.matriz[i+1][j+1])

    def convertir(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                self.matriz[i][j].viva = self.matriz[i][j].siguiente
