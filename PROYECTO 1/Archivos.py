import xml.dom.minidom 
from Terreno import Terreno
from ListaEnlazada import LinkedList

def cargarArchivo(ruta): # abre la ruta del archivo donde se encuentra el xml
    try:
        archivo = open(ruta, 'r') # modo lectura
        if(archivo.name[-4:] == ".xml"): # lee el archivo solamente si es extensión xml
            analizarArchivo(archivo)
        else:
            print("Solo se adminten archivos con extensión .xml")    
        archivo.close()
    except FileNotFoundError:
        print("Archivo no encontrado :(")
        

def analizarArchivo(archivo):
    listTerrenos = LinkedList() # instancia de la clase lista enlazada
    xmlDoc = xml.dom.minidom.parse(archivo) # para manejar el xml con las etiquetas
    data = xmlDoc.documentElement
    terrenos = data.getElementsByTagName("terreno") # lo separa por terrenos en una lista
    for terreno in terrenos:
        nombre = terreno.getAttribute("nombre") # el nombre del terreno
        
        # dimensión de los terrenos
        posicion = terreno.getElementsByTagName("dimension")[0]
        m = posicion.getElementsByTagName("m")[0]
        n = posicion.getElementsByTagName("n")[0]
        dimension = [int(m.firstChild.data), int(n.firstChild.data)]

        # posición de inicio de los terrenos
        posicion = terreno.getElementsByTagName("posicioninicio")[0]
        x = posicion.getElementsByTagName("x")[0]
        y = posicion.getElementsByTagName("y")[0]
        posInicio = [int(x.firstChild.data), int(y.firstChild.data)] # posicion de inicio (x, y)       
        
        # poisción final de los terrenos
        posicion = terreno.getElementsByTagName("posicionfin")[0]
        x = posicion.getElementsByTagName("x")[0]
        y = posicion.getElementsByTagName("y")[0]
        posFin = [int(x.firstChild.data), int(y.firstChild.data)] # posición de fin (x, y)

        # aquí agregamos cada terreno en la lista enlazada
        listTerrenos.append(Terreno(nombre, posInicio, posFin, dimension)) 
        
    # probando la lista enlazada...
    for terreno in listTerrenos.iterate():
        print(terreno.nombre)
        print(terreno.pi)
        print(terreno.pf)
    print(len(listTerrenos))
    print(listTerrenos.findTerreno("terreno1"))
    print(listTerrenos.findTerreno("terreno8"))
    print(listTerrenos[1].nombre)
    print(listTerrenos[20])
    listTerrenos.remove("terreno1")
    print(len(listTerrenos))

def crearArchivo(ruta):
    archivo = open(ruta, 'w')
    #Lógica para escribir el archivo
    archivo.close()
    print("Se ha escrito el archivo con éxito.")

