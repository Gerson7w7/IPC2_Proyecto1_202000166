from Archivos import cargarArchivo, crearArchivo

# menú
def menu():
    try:
        menu = int(input("Eliga una opción:\n"))
        print("\n\n")
        if(menu == 1):
            cargarArchivos()
        elif(menu == 2):
            print()
        elif(menu == 3):
            crearArchivos()
        elif(menu == 4):
            print("HOLA2")
        elif(menu == 5):
            print("HOLA3")
        elif(menu == 6):
            exit()
        else:
            print("Opción fuera de rango.")
    except ValueError:
        print("Ingrese un número.\n\n")


# Opciones del menú
def cargarArchivos():
    print("====================CARGAR ARCHIVOS====================")
    print("Ingrese la ruta absoluta del archivo:")
    ruta = input()
    cargarArchivo(ruta)


def crearArchivos():
    print("====================ESCRIBIR ARCHIVOS====================")
    print("Ingrese una ruta absoluta y nombre donde se guardará:")
    ruta = input()
    crearArchivo(ruta)


# menú principal y main del programa
while(True):
    print("======================== BIENVENIDO AL PROYECTO R2E2 ========================")
    print("============Menú principal============")
    print("1. Cargar archivo")
    print("2. Procesar terreno")
    print("3. Escribir archivo de salida")
    print("4. Mostrar datos del estudiante")
    print("5. Generar gráfica")
    print("6. Salir")
    menu()
