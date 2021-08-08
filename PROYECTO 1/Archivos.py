from xml.dom.minidom import parse

def cargarArchivo(ruta):
    archivo = open(ruta, 'r')
    if(archivo.name[-4:] == ".xml"):
        analizarArchivo(archivo)
    else:
        print("Solo se adminten archivos con extensión .xml")    
    archivo.close()

def analizarArchivo(archivo):
    dom = parse(archivo)

def crearArchivo(ruta):
    archivo = open(ruta, 'w')
    #Lógica para escribir el archivo
    archivo.close()
    print("Se ha escrito el archivo con éxito.")

