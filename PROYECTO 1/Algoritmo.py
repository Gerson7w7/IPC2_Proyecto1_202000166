def camino(terreno):
    for pos in terreno.posiciones:
        if terreno.pi[0] == pos[0] and terreno.pi[1] == pos[1]:
            nextPos = posicion(pos)
    

def posicion(pos):
    # norte 
    n = pos[1] - 1
    # oeste
    o = pos[0] - 1
    # sur
    s = pos[1] + 1 
    # este 
    e = pos[0] + 1
