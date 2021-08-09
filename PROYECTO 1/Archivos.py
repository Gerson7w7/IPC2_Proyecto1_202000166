import xml.dom.minidom 
from Terreno import Terreno

def cargarArchivo(ruta):
    try:
        archivo = open(ruta, 'r')
        if(archivo.name[-4:] == ".xml"):
            analizarArchivo(archivo)
        else:
            print("Solo se adminten archivos con extensión .xml")    
        archivo.close()
    except FileNotFoundError:
        print("Archivo no encontrado :(")
        

def analizarArchivo(archivo):
    listTerrenos = []
    xmlDoc = xml.dom.minidom.parse(archivo)
    data = xmlDoc.documentElement
    terrenos = data.getElementsByTagName("terreno")
    for terreno in terrenos:
        nombre = terreno.getAttribute("nombre")
        print(nombre)
        posicion = terreno.getElementsByTagName("posicioninicio")[0]
        x = posicion.getElementsByTagName("x")[0]
        y = posicion.getElementsByTagName("y")[0]
        posInicio = [int(x.firstChild.data), int(y.firstChild.data)]       
        posicion = terreno.getElementsByTagName("posicionfin")[0]
        x = posicion.getElementsByTagName("x")[0]
        y = posicion.getElementsByTagName("y")[0]
        posFin = [int(x.firstChild.data), int(y.firstChild.data)]
        print(posInicio)
        print(posFin)
        listTerrenos.append(Terreno(nombre, posInicio, posFin))
    print(listTerrenos[0].nombre, listTerrenos[0].pi, listTerrenos[0].pf)

def crearArchivo(ruta):
    archivo = open(ruta, 'w')
    #Lógica para escribir el archivo
    archivo.close()
    print("Se ha escrito el archivo con éxito.")

