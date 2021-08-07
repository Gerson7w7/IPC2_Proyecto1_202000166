def cargarArchivo(ruta):
    archivo = open(ruta, 'r')
    contenido = archivo.read()
    archivo.close()
    print("Archivo cargado correctamente.")

def crearArchivo(ruta):
    archivo = open(ruta, 'w')
    #Lógica para escribir el archivo
    archivo.close()
    print("Se ha escrito el archivo con éxito.")