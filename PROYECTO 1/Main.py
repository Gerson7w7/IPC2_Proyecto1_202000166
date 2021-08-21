from Archivos import cargarArchivo, crearArchivo
from Algoritmo import camino
from ListaEnlazada import LinkedList
from Grafica import graficaG

# menú
def menu(listTerrenos):
    try:
        menu = int(input("Eliga una opción:\n"))
        print("\n\n")
        if(menu == 1):
            listTerrenos = cargarArchivos(listTerrenos)        
        elif(menu == 2):
            procesarTerreno(listTerrenos)
        elif(menu == 3):
            crearArchivos(listTerrenos)
        elif(menu == 4):
            datosEstudiante()
        elif(menu == 5): 
            reportes(listTerrenos)
        elif(menu == 6):
            exit()
        else:
            print("Opción fuera de rango.")
    except ValueError:
        print("Ingrese un número.\n\n")


# Opciones del menú
def cargarArchivos(listTerrenos):
    print("====================CARGAR ARCHIVOS====================")
    print("Ingrese la ruta absoluta del archivo:")
    #ruta = input()
    ruta = "C:\\Users\\gerso\\Desktop\\PROGRAMACIÓN\\Python\\IPC2\\IPC2_Proyecto1\\PROYECTO 1\\terrenos.xml"
    listTerrenos = cargarArchivo(ruta, listTerrenos)
    return listTerrenos


def crearArchivos(listTerrenos):
    print("====================ESCRIBIR ARCHIVOS====================")
    print("Ingrese una ruta absoluta y nombre donde se guardará:")
    print("NOTA: Solo se escribirán los terrenos que hayan sido analizados.")
    # ruta = input()
    ruta = "C:\\Users\\gerso\\Desktop\\PROGRAMACIÓN\\Python\\IPC2\\IPC2_Proyecto1\\PROYECTO 1\\prueba.xml"
    crearArchivo(ruta, listTerrenos)


def datosEstudiante():
    print("==================== DATOS DEL ESTUDIANTE ================")
    print(">Gerson Rubén Quiroa del Cid")
    print(">202000166")
    print(">Introducción a la programación y computación 2 sección A")
    print(">Ingeniería en Ciencias y Sistemas")
    print(">Cuarto semestre")

def procesarTerreno(listTerrenos):
    print("==================== PROCESAR TERRENO ================")
    flag = False
    if listTerrenos.size != 0:
        nombreTerreno = input("Ingrese el nombre del terreno que quiere analizar: \n")

        # buscando el terreno a procesar
        print("Buscando terreno...")
        for terreno in listTerrenos.iterate():
            if terreno.nombre == nombreTerreno:
                if terreno.analizado == False:
                    terreno.analizado = True
                    caminoTerreno = camino(terreno)
                    flag = True
                    # verificando si se procesó el terreno o no se encontró        
                    if flag:
                        print("Terreno procesado con éxito! :D")
                    else: 
                        print("No se ha encontrado el terreno, intente con otro nombre.")
                else: 
                    print("Este terreno ya ha sido analizado")
                    break
    else:
        print("No se ha cargado ningún archivo")
    return caminoTerreno
    

def reportes(listTerrenos):
    print("==================== REPORTES ================")
    if listTerrenos.size != 0:
        print("Elija el terreno que desea graficar")
        i = 1
        for terreno in listTerrenos.iterate():
            print(str(i) + ") " + terreno.nombre)
            i += 1

        iTerreno = int(input(">"))
        #graficaG(listTerrenos[iTerreno - 1])

    else: 
        print("No se ha cargado ningún terreno.")

# menú principal y main del programa
# variable global        
listTerrenos = LinkedList() # instancia de la clase lista enlazada

while(True):
    print("======================== BIENVENIDO AL PROYECTO R2E2 ========================")
    print("============Menú principal============")
    print("1. Cargar archivo")
    print("2. Procesar terreno")
    print("3. Escribir archivo de salida")
    print("4. Mostrar datos del estudiante")
    print("5. Generar gráfica")
    print("6. Salir")
    menu(listTerrenos)
