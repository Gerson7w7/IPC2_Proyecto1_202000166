import os

def graficaG(terreno):
    cadena = ""
    i = 1
    j = 1
    archivo = open("grafo.dot", "w")
    archivo.write("graph grafo{\n")
    archivo.write(f"label={terreno.nombre}\n")

    # se pone un label a cada posición con la gasolina de la misma
    for pos in terreno.posiciones.iterate():
        archivo.write(str(pos.x) + str(pos.y) + "[label=" + str(pos.gas) + "]\n")

    # para enlazar los vértices de izquierda a derecha
    while((terreno.dim.y + 1) != i):
        for pos in terreno.posiciones.iterate():
            if pos.y == i and pos.x == j:
                if j == 1:
                    cadena += "rank=same{" + (str(j) + str(i))
                else: 
                    cadena += f" -- {str(j) + str(i)}" 
                                                      
                if terreno.dim.x == j:
                    cadena += "}\n"
                    i += 1 # pasa a la siguiente fila    
                    j = 0 # reinicia las columnas
                j += 1 # pasa la siguiente columna
    archivo.write(cadena)

    print("Generando gráfica...")

    # para enalazar los vértices de arriba a abajo
    cadena2 = ""
    i = 1
    j = 1
    while((terreno.dim.x + 1) != j):
        for pos in terreno.posiciones.iterate():
            if pos.y == i and pos.x == j:
                if i == 1:
                    cadena2 += (str(j) + str(i))
                else: 
                    cadena2 += f" -- {str(j) + str(i)}" 
                                                      
                if terreno.dim.y == i:
                    cadena2 += "\n"
                    j += 1 # pasa a la siguiente fila    
                    i = 0 # reinicia las columnas
                i += 1 # pasa la siguiente columna
    archivo.write(cadena2)
    
    archivo.write("}")
    archivo.close()

    print("Se ha creado correctamente la gráfica del terreno: " + terreno.nombre)
    os.system(f'cmd /c "dot.exe -Tpng grafo.dot -o {terreno.nombre}.png"')