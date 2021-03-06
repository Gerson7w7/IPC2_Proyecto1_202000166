from ListaEnlazada import LinkedList

class Terreno(object):
    def __init__(self, nombre, pi, pf, dim, posiciones):
        self.nombre = nombre
        self.pi = pi # posicion inicial (x, y)
        self.pf = pf # posicion final (x, y)
        self.dim = dim # dimension de la matriz (m, n)
        self.posiciones = posiciones # posiciones ((x1, y2, gas)...(xn, yn, gas))
        self.analizado = False
        self.lRecorrido = LinkedList()

class Posicion(object):
    def __init__(self, x, y, gas = None):
        self.x = x
        self.y = y
        self.gas = gas
        self.flag = False # pivote
        self.posAnt = LinkedList() # posiciones anteriores
        self.acumulado = 0 # gasolina acumulado 