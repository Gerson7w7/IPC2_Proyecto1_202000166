from Clases import Posicion

def camino(terreno):
    gas = []
    for pos in terreno.posiciones.iterate():
        if terreno.pi.x == pos.x and terreno.pi.y == pos.y:
            pos.flag = True
            pos.acumulado = pos.gas
            posicion(pos, terreno, gas)
            break
    

def posicion(pos, terreno, gas):
    if(terreno.pf.x == pos.x and terreno.pf.y == pos.y):
        print("Camino calculado")
    else:
        if gas != []:
            gas.pop(0)
        # norte 
        if pos.y != 1:
            n = Posicion(pos.x, pos.y - 1)
            if not(n.x == pos.posAnt.x and n.y == pos.posAnt.y):
                gasN = consumo(n, terreno, pos)
                gas.append(gasN)
        # oeste
        if pos.x != 1:
            o = Posicion(pos.x - 1, pos.y)
            if not(o.x == pos.posAnt.x and o.y == pos.posAnt.y):
                gasO = consumo(o, terreno, pos)
                gas.append(gasO)
        # sur
        if pos.y != terreno.dim.y:
            s = Posicion(pos.x, pos.y + 1)
            if not(s.x == pos.posAnt.x and s.y == pos.posAnt.y):
                gasS = consumo(s, terreno, pos) 
                gas.append(gasS)
        # este 
        if pos.x != terreno.dim.x: 
            e = Posicion(pos.x + 1, pos.y)
            if not(e.x == pos.posAnt.x and e.y == pos.posAnt.y):
                gasE = consumo(e, terreno, pos)
                gas.append(gasE)

        bubbleSortASC(gas)
        nextPosicion = gas[0]
        nextPosicion.posAnt = pos
        nextPosicion.flag = True
        print(nextPosicion.x, nextPosicion.y, nextPosicion.acumulado, nextPosicion.gas)
        posicion(nextPosicion, terreno, gas)
        
    

def consumo(nextPosicion, terreno, pos):
    for posicion in terreno.posiciones.iterate():
        if posicion.x == nextPosicion.x and posicion.y == nextPosicion.y:
            posicion.acumulado = pos.acumulado + posicion.gas
            return posicion
    return None


def bubbleSortASC(gas):  # algoritmo de ordenamiento ascendente
    n = len(gas)
    # itera cada elemento de la lista
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            # recorre la lista de 0 a n-i-1.
            # intercambia el elemento actual si
            # es mayor que el siguiente elemento.
            if gas[j].acumulado > gas[j+1].acumulado:
                gas[j], gas[j+1] = gas[j+1], gas[j]
                swapped = True
        # Si los elementos no se intercambian por el loop
        # entonces se para con un break
        if swapped == False:
            break