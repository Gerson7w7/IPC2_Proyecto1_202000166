from Clases import Posicion
from ListaEnlazada import LinkedList

# sinceramente ni yo sé como logré hacer este algoritmo xd 
# no es tan preciso pero encuentra la mejor ruta!

def camino(terreno):
    gas = []
    print("Analizando terreno...")
    for pos in terreno.posiciones.iterate():
        # encuentra la posicion inicial dentro de todas las posiciones
        if terreno.pi.x == pos.x and terreno.pi.y == pos.y:
            pos.flag = True
            gas.append(pos)
            posicion(pos, terreno, gas)
            break


# pos: posición actual
# acumulado: gasolina acumulado
# gas: gasolina por posición
def posicion(pos, terreno, gas):   
    if(terreno.pf.x == pos.x and terreno.pf.y == pos.y):
        print("Buscando la mejor ruta...")
        recorrido(pos, terreno) 
        # si llega a la posición final, se termina la recursividad.
    else:
        gas.pop(0)
        # norte
        # le resta una posición si es diferente de 1
        if pos.y != 1:
            n = Posicion(pos.x, pos.y - 1)
            gasN = consumo(n, terreno, pos)
            if not(gasN == None):
                gasN.posAnt.append(pos)
                gas.append(gasN)

        # oeste
        # le resta una posición si es diferente de 1
        if pos.x != 1:
            o = Posicion(pos.x - 1, pos.y)
            gasO = consumo(o, terreno, pos)
            if not(gasO == None):
                gasO.posAnt.append(pos)
                gas.append(gasO)

        # sur
        # le suma una posición si es diferente del límite
        if pos.y != terreno.dim.y:
            s = Posicion(pos.x, pos.y + 1)
            gasS = consumo(s, terreno, pos)
            if not(gasS == None):
                gasS.posAnt.append(pos)
                gas.append(gasS)

        # este
        # le suma una posición si es diferente del límite
        if pos.x != terreno.dim.x:
            e = Posicion(pos.x + 1, pos.y)
            gasE = consumo(e, terreno, pos)
            if not(gasE == None):
                gasE.posAnt.append(pos)
                gas.append(gasE)

        # ordeno la lista de gas en forma ascendente
        bubbleSortASC(gas)
        # la siguiente posición será la primera de la lista
        nextPosicion = gas[0]
        nextPosicion.flag = True
        posicion(nextPosicion, terreno, gas)


def consumo(nextPosicion, terreno, pos):
    # buscando en la matriz de posiciones del terrreno
    for posicion in terreno.posiciones.iterate():  
        if posicion.x == nextPosicion.x and posicion.y == nextPosicion.y:
            # si no es el pivote será la nueva posición 
            if posicion.flag != True:
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

# lo que hace esta función es agregar a una lista solo las posiciones donde pasará el robot
def recorrido(pos, terreno):
    print("Calculando gasolina...")
    listRecorrido = LinkedList()
    listRecorrido.append(pos)
    gasolina = pos.acumulado
    
    while(not(pos.x == terreno.pi.x and pos.y == terreno.pi.y)):   
            bubbleSortASC(pos.posAnt)
            pos = pos.posAnt[0]
            listRecorrido.append(pos)
    terreno.lRecorrido = listRecorrido

    print("Camino calculado")
    # graficando el terreno
    print("Combustible necesario: " + str(gasolina))
    graficaConsola(terreno, 1, 1, "")


def graficaConsola(terreno, i, j, cadena):
    # i y j empezaran en 1, 1; y la cadena en ""
    if (terreno.dim.y + 1) == i:
        # si la dimensión en y (m) es m + 1 es porque ya se ha llenado 
        # entonces termina la recursivida y pasa a imprimir la matriz
        print(cadena)       
    else:
        for pos in terreno.posiciones.iterate():
            if pos.y == i and pos.x == j:
                flag = False
                for ruta in terreno.lRecorrido.iterate():
                    if pos.x == ruta.x and pos.y == ruta.y:
                        # si la posición es parte de la ruta se pondrá un 1
                        cadena += "|1|"
                        flag = True
                        break
                if flag == False:
                    # si no, se pondrá un 0
                    cadena += "|0|"
                if terreno.dim.x == j:
                    cadena += "\n"
                    i += 1 # pasa a la siguiente fila    
                    j = 0 # reinicia las columnas
                j += 1 # pasa la siguiente columna
        graficaConsola(terreno, i, j, cadena)   
                    
                    
            