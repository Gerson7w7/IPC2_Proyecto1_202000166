import xml.dom.minidom 
from Clases import Terreno, Posicion
from ListaEnlazada import LinkedList

def cargarArchivo(ruta, listTerrenos): # abre la ruta del archivo donde se encuentra el xml
    try:
        archivo = open(ruta, 'r') # modo lectura
        if(archivo.name[-4:] == ".xml"): # lee el archivo solamente si es extensión xml
            listTerrenos = analizarArchivo(archivo, listTerrenos)
            print("Archivo cargado con éxito :D")
        else:
            print("Solo se adminten archivos con extensión .xml")    
        archivo.close()
    except FileNotFoundError:
        print("Archivo no encontrado :(")
    return listTerrenos


def analizarArchivo(archivo, listTerrenos):
    xmlDoc = xml.dom.minidom.parse(archivo) # para manejar el xml con las etiquetas
    data = xmlDoc.documentElement
    terrenos = data.getElementsByTagName("terreno") # lo separa por terrenos en una lista
    for terreno in terrenos:
        nombre = terreno.getAttribute("nombre") # el nombre del terreno
        
        # dimensión de los terrenos
        posicion = terreno.getElementsByTagName("dimension")[0]
        m = posicion.getElementsByTagName("m")[0]
        n = posicion.getElementsByTagName("n")[0]
        dimension = Posicion(int(n.firstChild.data), int(m.firstChild.data))

        # posición de inicio de los terrenos
        posicion = terreno.getElementsByTagName("posicioninicio")[0]
        x = posicion.getElementsByTagName("x")[0]
        y = posicion.getElementsByTagName("y")[0]
        posInicio = Posicion(int(x.firstChild.data), int(y.firstChild.data)) # posicion de inicio (x, y)       
        
        # posición final de los terrenos
        posicion = terreno.getElementsByTagName("posicionfin")[0]
        x = posicion.getElementsByTagName("x")[0]
        y = posicion.getElementsByTagName("y")[0]
        posFin = Posicion(int(x.firstChild.data), int(y.firstChild.data)) # posición de fin (x, y)

        # posiciones de las matrices y las unidades de gasolina 
        posiciones = terreno.getElementsByTagName("posicion")
        listPosiciones = LinkedList()
        listPosiciones2 = LinkedList()
        for posicion in posiciones:
            x = posicion.getAttribute("x")
            y = posicion.getAttribute("y")
            gas = posicion.firstChild.data
            listPosiciones.append(Posicion(int(x), int(y), int(gas)))

        # aquí agregamos cada terreno en la lista enlazada
        listTerrenos.append(Terreno(nombre, posInicio, posFin, dimension, listPosiciones)) 
    return listTerrenos


def crearArchivo(ruta, listTerrenos):
    # creando el archivo xml
    DOMimp = xml.dom.minidom.getDOMImplementation()
    xmlDoc = DOMimp.createDocument(None, "terrenos", None)
    # raíz del archivo
    docRoot = xmlDoc.documentElement
    
    # por cada terreno creamos un nodo
    for terreno in listTerrenos.iterate():
        if terreno.analizado == True:
            # nodo terreno
            terr = xmlDoc.createElement("terreno")

            # sub nodo dimensión
            dim = xmlDoc.createElement("dimension")
            m = xmlDoc.createElement("m")
            m.appendChild(xmlDoc.createTextNode(str(terreno.dim.y)))
            n = xmlDoc.createElement("n")
            n.appendChild(xmlDoc.createTextNode(str(terreno.dim.x)))
            # agregando m y n al sub nodo dimensión
            dim.appendChild(m)
            dim.appendChild(n)
            terr.appendChild(dim)

            # sub nodo posicioninicial
            posicion = xmlDoc.createElement("posicioninicial")
            x = xmlDoc.createElement("x")
            x.appendChild(xmlDoc.createTextNode(str(terreno.pi.x)))
            y = xmlDoc.createElement("y")
            y.appendChild(xmlDoc.createTextNode(str(terreno.pi.y)))
            # agregamos x, y al sub nodo posicioninicial
            posicion.appendChild(x)
            posicion.appendChild(y)
            terr.appendChild(posicion)

            # sub nodo posicionfinal
            posicion = xmlDoc.createElement("posicionfinal")
            x = xmlDoc.createElement("x")
            x.appendChild(xmlDoc.createTextNode(str(terreno.pf.x)))
            y = xmlDoc.createElement("y")
            y.appendChild(xmlDoc.createTextNode(str(terreno.pf.y)))
            # agregamos x, y al sub nodo posicioninicial
            posicion.appendChild(x)
            posicion.appendChild(y)
            terr.appendChild(posicion)

            for pos in terreno.lRecorrido.iterate():
                if pos.x == terreno.pf.x and pos.y == terreno.pf.y:
                    # sub nodo combustible
                    gas = xmlDoc.createElement("combustible")
                    gas.appendChild(xmlDoc.createTextNode(str(pos.acumulado)))
                    terr.appendChild(gas)
                # sub nodo posicion 
                posicion = xmlDoc.createElement("posicion")
                posicion.setAttribute("x", str(pos.x))
                posicion.setAttribute("y", str(pos.y))
                posicion.appendChild(xmlDoc.createTextNode(str(pos.gas)))
                # agregamos x, y al sub nodo posicioninicial
                terr.appendChild(posicion)

            # añadimos el nodo terreno a la raíz del archivo
            docRoot.appendChild(terr)

    # guardando el fichero en la ruta especificada
    archivo = open(ruta, 'w')
    archivo.write(xmlDoc.toxml())
    archivo.close()
    print("Se ha escrito el archivo con éxito! :D")

