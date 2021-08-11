class Nodo(object): # clase nodo
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
    
    def __str__(self): # regresa el dato en forma de string
        return str(self.dato)
    
class LinkedList(object):
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0

    def append(self, dato): # función para agregar un dato
        nodo = Nodo(dato) 
        if self.cabeza: 
            self.cabeza.siguiente = nodo
            self.cabeza = nodo
        else: # si es el primer dato
            self.cabeza = nodo
            self.cola = nodo
        self.size += 1

    def iterate(self): # función para iterar la lista
        actual = self.cola
        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato
        
    # forma de llamar a la iteración:
    # for l in lista.iterar():
    #   print(l)    

    # función para encontrar un terreno por medio del nombre
    # devuelve solamente el nombre
    def findTerreno(self, nombreTerreno): 
        for terreno in self.iterate():
            if nombreTerreno == terreno.nombre:
                return terreno.nombre
        return "El terreno no existe."

    # función buscar por índice
    def __getitem__(self, indice): 
        # si está entre 0 y el tamaño de la lista
        # devuelve el objeto
        if indice >= 0 and indice < self.size:
            actual = self.cola
            for i in range(indice):
                actual = actual.siguiente
            return actual.dato
        else:
            return "Índice fuera de rango"

    # función que elimina un dato por medio del nombre del terreno
    def remove(self, dato):
        actual = self.cola
        anterior = self.cola
        while actual:
            if actual.dato.nombre == dato:
                if actual == self.cola:
                    self.cola = actual.siguiente
                else:
                    # esta línea es importante, ya que aquí se enlaza
                    # el anterior nodo con el siguiente nodo, así 
                    # remueve la conexción del nodo actual
                    anterior.siguiente = actual.siguiente
                self.size -= 1
                return
            anterior = actual
            actual = actual.siguiente

    # sobre escritura de la función len, para que devuelva el tamaño de la lista
    def __len__(self):
        return self.size

    # sobre escritura de la función str, para que imprima la lista
    def __str__(self):
        string = "["
        current = self.first
        for i in range(len(self)):
            string += str(current)
            if i != len(self) - 1:
                string += str(", ")
            current = current.next
        string += "]"
        return string