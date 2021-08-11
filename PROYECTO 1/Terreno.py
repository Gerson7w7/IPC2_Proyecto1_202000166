class Terreno(object):
    def __init__(self, nombre, pi, pf, dim, posiciones):
        self.nombre = nombre
        self.pi = pi # posicion inicial (x, y)
        self.pf = pf # posicion final (x, y)
        self.dim = dim # dimension de la matriz (m, n)
        self.posiciones = posiciones # posiciones ((x1, y2, gas)...(xn, yn, gas))