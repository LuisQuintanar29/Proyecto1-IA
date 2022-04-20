

from cgi import print_arguments


class Mapa:
    # Lista de rutas posibles
    rutas = []
    # Lista de ciudades expandidas
    expandidas = []
    # Mapa de estados con sus vecinos
    estados ={
        'Oradea':{'Zerind':71,'Sibiu':151},
        'Zerind':{'Arad':75,'Oradea':71},
        'Arad':{'Zerind':75,'Sibiu':140,'Timisoara':118},
        'Sibiu':{'Oradea':151,'Arad':140,'Fagaras':99,'Rimnicu Vilcea':80},
        'Fagaras':{'Sibiu':99,'Bucharest':211},
        'Timisoara':{'Arad':118,'Lugoj':111},
        'Lugoj':{'Timisoara':111,'Mehadia':70},
        'Mehadia':{'Lugoj':70,'Dobreta':75},
        'Dobreta':{'Mehadia':75,'Craiova':120},
        'Craiova':{'Dobreta':120,'Pitesti':138,'Rimnicu Vilcea':146},
        'Pitesti':{'Rimnicu Vilcea':97,'Craiova':138,'Bucharest':101},
        'Rimnicu Vilcea':{'Sibiu':80,'Craiova':146,'Pitesti':97},
        'Bucharest':{'Fagaras':211,'Pitesti':101,'Giurgiu':90,'Urziceni':85},
        'Giurgiu':{'Bucharest':90},
        'Urziceni':{'Bucharest':85,'Hirsova':98,'Vaslui':142},
        'Hirsova':{'Urziceni':98,'Eforie':86},
        'Eforie':{'Hirsova':86},
        'Vaslui':{'Urziceni':142,'Iasi':92},
        'Iasi':{'Vaslui':92,'Neamt':87},
        'Neamt':{'Iasi':87}
    }
    
    # Devuelve el diccionario de los estados
    def getMapa(self):
        return self.estados
    
    # Imprime cada Estados con sus vecinos y el costo
    def printMapa(self):
        cad = "CIUDAD: \t \t VECINOS Y COSTOS DE VIAJE"
        for k in self.estados:
            cad = cad + "\n| {:<15} |".format(k)
            for ciudad,costo in self.estados[k].items():
                cad = cad+"{:<15}:{:3} | ".format(ciudad,costo)
        print(cad)
        
    # Ordena el mapa por orden alfanumerico, tanto los estados como sus vecinos
    def ordenaMapa(self):
        # Variable auxiliar
        tempEstados = self.estados
        # Reiniciamos los estados
        self.estados = {}
        # Para cada ciudad en los estados ordenados
        for p in sorted(tempEstados):
            # Agregamos los estados
            self.estados[p] = tempEstados[p]
            # Borramos a sus vecinos
            self.estados[p] = {}
            # Para cada vecino ordenado
            for q in sorted(tempEstados[p]):
                # Agregamos a los vecinos
                self.estados[p][q] = tempEstados[p][q]

    # Buscamos las rutas que lleguen a la misma ciudad
    def buscarRepetidos(self):
        # Variable axiliar para hacer los cambios
        aux = {}
        # Variable con las rutas repetidas
        rep = {}
        # Para cada ruta de la lista de rutas
        for ruta in self.rutas:
            # Guardamos la lista de ciudades al final de la ruta
            # que no existen en aux
            if ruta[-1] not in aux:
                # Cuando no existe, sólo se ha guardado una vez
                aux[ruta[-1]] = 1
            else:
                # Si existe, aumentamos el contador en uno
                aux[ruta[-1]] = aux[ruta[-1]] + 1
        # Guaramos las ciudades y la cantidad de veces que se encuentran en las rutas
        for k,v in aux.items():
            # Si es mayor a uno, guardamos la ciudad, debido a que se repite
            if v > 1:
                rep[k] = v
        # Reiniciamos la variable auxiliar
        aux = {}
        # Le asinamos al diccionario, la lista de ciudades repetidas, y le 
        # añadimos una lista que guardará el costo de cada ruta
        for i in rep:
            aux[i] = []
        # Recorremos las rutas en la lista de rutas
        for ruta in self.rutas:
            # Para cada ciudad repetida que existe
            for r in aux:
                # Si la ultima ciudad de la ruta, es una ciudad repetida
                if ruta[-1] == r:
                    # Guardamos el costo de la ruta
                    aux[r].append(ruta[0])
        # Le asignamos las ciudades repetidas y el costo de la
        # ruta ya ordenamos de menor a mayor y regresamos ese diccionario
        for i in aux:
            rep[i] = sorted(aux[i])
        return rep

    # Borramos rutas repetidas
    def borrarRepetidos(self):
        # Buscamos las rutas que se repiten y el costo de cada una de ellas
        rep = self.buscarRepetidos().copy()
        # Si existen rutas repetidas
        if len(rep) != 0:
            # Contador para saber el indice
            j = 0
            # Buscamos en cada ruta de la lista de rutas
            for ruta in self.rutas:
                # Para cada ciudad y costos repetidos
                for k,v in rep.items():
                    # Para cada costo de las distintas rutas
                    # con ciudades repetidas
                    for d in v:
                        # Si la ciudad repetida coincide con el de la ruta
                        # y además la distancia coincide con la distancia repetida
                        # y no es el valor mínimo para llegar a la ciudad
                        if(k == ruta[-1] and ruta[0] == d and d !=v[0]):
                            # Eliminamos la ruta
                            del self.rutas[j]
                # Aumentamos el índice
                j = j+1        

    # Expande la ciudad en las rutas que la contengan
    def expandirCiudad(self, ciudad):
        # Guardará los indices donde se encuentra la ciudad expandida
        indices = []
        # Recorremos todas las ciudades en las rutas
        for cdad in range(len(self.rutas)):
            # Si se encuentra la ciudad a expandir
            if ciudad in self.rutas[cdad] :
                # Guardamos la lista para agregar las expansiones
                lst = self.rutas[cdad]
                # El indice donde se encuentra la ciudad se guarda
                indices.append(cdad)
                # Para cada vecino de la ciudad a expandir
                for vecino in self.getMapa()[ciudad].keys():
                    # Si el vecino no se ha expandido
                    if vecino not in self.expandidas:
                        ls = []
                        ls = ls + lst
                        # Agregamos al vecino en la ruta a expandir
                        ls.append(vecino)
                        # Lo añadimos a la lista de rutas
                        self.rutas.append(ls)
                        # Sumamos el costo de viaje a la ciudad agregada
                        self.rutas[-1][0] = self.rutas[-1][0] + self.getMapa()[ciudad].get(vecino)
        # Borramos las rutas de las ciudades antes de ser expandidas
        for i in indices:
            del self.rutas[i] 
        self.expandidas.append(ciudad)
    
    # Buscamos la ruta con menos costo
    def buscaRutaMenor(self):
        # Costos de cada ruta en las rutas
        costos = []
        # Para cada ruta en las rutas
        for ruta in self.rutas:
            # Guardamos los costos de cada una
            costos.append(ruta[0])
        # El minimo es el primero de la lista ordenada
        min = sorted(costos)[0]
        # Buscamos en cada ruta de la ruta
        for ruta in self.rutas:
            # Si el costo de la ruta es el mínimo
            if ruta[0] == min:
                # Regresamos la siguiente ciudad a expandir
                return ruta[-1]

    # Lee las ciudades de origen y de destino
    def leerCiudades(self):
        # Leemos la ciudad de origen
        self.ciudadOrigen = input('IINGRESE LA CIUDAD DE ORIGEN: ')
        while (self.ciudadOrigen not in self.getMapa()):
            print('CIUDAD DE ORIGEN NO ENCONTRADA')
            self.ciudadOrigen = input('INGRESE UNA CIUDAD DE ORIGEN VÁLIDA: ')
        ls=[0]
        ls.append(self.ciudadOrigen)
        self.rutas.append(ls)

        # Leemos la ciudad de destino
        self.ciudadDestino = input('INGRESE LA CIUDAD DE DESTINO: ')
        while (self.ciudadDestino not in self.getMapa() or self.ciudadDestino == self.ciudadOrigen):
            print('CIUDAD DE DESTINO NO ENCONTRADA')
            self.ciudadDestino = input('INGRESE UNA CIUDAD DE DESTINO VÁLIDA: ')
    
    # Imprime ciudades expandidas y lista de rutas
    def imprimeDatos(self):
        exp = "CIUDADES EXPANDIDAS:\n \t "
        # Para cada ciudad expandida
        for i in self.expandidas:
            # Concatenamos la ciudad para darle formato
            exp = exp + i + ", "

        rutas = "RUTAS: \n \t"
        # Para cada ruta de la lista de rutas
        for i in self.rutas:
            # Agregamos el costo de la ruta
            rutas = rutas + str(i[0])
            # Para cada ciudad de la ruta
            for j in range(len(i)-1):
                # Le damos formato para imprimir
                rutas = rutas + "->" + str(i[j+1])
            rutas = rutas + "\n\t"
        # Imprimimos las ciudades expandidad
        print(exp)
        # Imprimimos las rutas de las ciudades
        print(rutas)
    
    # Busqueda de Costo Uniforme
    def BCU(self):
        # Leemos las ciudades de Origen y Desino
        self.leerCiudades()
        # Imprimimos la ciudad de origen y el costo
        self.imprimeDatos()
        # Expandimos la ciudad de origen
        self.expandirCiudad(self.ciudadOrigen)
        # Imprimimos los datos nuevos
        self.imprimeDatos()
        # Mientras que la ruta de menor costo no nos lleve a la ciudad de Destino
        while self.buscaRutaMenor() != self.ciudadDestino:
            # Expandimos la ciudad de menor costo
            self.expandirCiudad(self.buscaRutaMenor())
            # Imprimimos los nuevos dato
            self.imprimeDatos()
            # Borramos las rutas que lleguen a la misma ciudad y que 
            # impliquen un mayor costo
            self.borrarRepetidos()
            # Si la ruta de menor costo nos lleva al destino imprimimos un mensaje de éxito
            if self.buscaRutaMenor() == self.ciudadDestino:
                print("RUTA MÍNIMA ENCONTRADA\n")
                for rutas in self.rutas:
                    if rutas[1] == self.ciudadOrigen and rutas[-1] == self.ciudadDestino:
                       print("\tCOSTO: "+str(rutas[0]))
                       stri = "\tRUTA "
                       for r in range(len(rutas)-1):
                           stri = stri +"-> " + rutas[r+1]
                print(stri)
    # Constructor. Cuando se instancia un objeto, ordena el mapa
    def __init__(self): 
        self.ordenaMapa()

if __name__ == "__main__":
    # Creamos un mapa
    e = Mapa()
    # Imprimimos el mapa
    e.printMapa()
    # Iniciamos el algoritmo de Búsqueda de Costo Uniforme
    e.BCU()