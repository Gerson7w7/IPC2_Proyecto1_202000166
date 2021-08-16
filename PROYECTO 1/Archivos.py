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
        for posicion in posiciones:
            x = posicion.getAttribute("x")
            y = posicion.getAttribute("y")
            gas = posicion.firstChild.data
            listPosiciones.append(Posicion(int(x), int(y), int(gas)))

        # aquí agregamos cada terreno en la lista enlazada
        listTerrenos.append(Terreno(nombre, posInicio, posFin, dimension, listPosiciones)) 
    return listTerrenos


def crearArchivo(ruta):
    archivo = open(ruta, 'w')
    #Lógica para escribir el archivo
    archivo.close()
    print("Se ha escrito el archivo con éxito.")

