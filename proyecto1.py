
class Mapa:
    rutas = []
    expandidas = []
    encontradas = []
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
        for k in self.estados:
            print(k,":",self.estados[k])
   
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
        aux = {}
        rep = {}
        for ruta in self.rutas:
            if ruta[-1] not in aux:
                aux[ruta[-1]] = 1
            else:
                aux[ruta[-1]] = aux[ruta[-1]] + 1
        for k,v in aux.items():
            if v > 1:
                rep[k] = v
        aux = {}
        for i in rep:
            aux[i] = []

        for ruta in self.rutas:
            for r in aux:
                if ruta[-1] == r:
                    aux[r].append(ruta[0])
        for i in aux:
            rep[i] = sorted(aux[i])
        return rep

    # Borramos rutas repetidas
    def borrarRepetidos(self):
        rep = self.buscarRepetidos().copy()
        if len(rep) != 0:
            j = 0
            for ruta in self.rutas:
                for k,v in rep.items():
                    for d in v:
                        if(k == ruta[-1] and ruta[0] == d and d !=v[0]):
                            del self.rutas[j]
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
        self.ciudadOrigen = input('Ingrese la ciudad de Origen: ')
        while (self.ciudadOrigen not in self.getMapa()):
            print('Ciudad de Origen no encontrada')
            self.ciudadOrigen = input('Ingrese una ciudad de Origen Válida: ')
        ls=[0]
        ls.append(self.ciudadOrigen)
        self.rutas.append(ls)

        # Leemos la ciudad de destino
        self.ciudadDestino = input('Ingrese la ciudad de Destino: ')
        while (self.ciudadDestino not in self.getMapa() or self.ciudadDestino == self.ciudadOrigen):
            print('Ciudad de Destino no encontrada')
            self.ciudadDestino = input('Ingrese una ciudad de Destino Válida: ')
    
    # Imprime ciudades expandidas y lista de rutas
    def imprimeDatos(self):
        print("CIUDADES EXPANDIDAS")
        print(e.expandidas)
        print("RUTAS")
        print(e.rutas)
    
    # Busqueda de Costo Uniforme
    def BCU(self):
        self.leerCiudades()

        self.expandirCiudad(self.ciudadOrigen)
        self.imprimeDatos()

        while self.buscaRutaMenor() != self.ciudadDestino:
            self.expandirCiudad(self.buscaRutaMenor())
            self.imprimeDatos()
            self.borrarRepetidos()

            if self.buscaRutaMenor() == self.ciudadDestino:
                print("RUTA MÍNIMA ENCONTRADA")
    
    # Constructor. Cuando se instancia un objeto, ordena el mapa
    def __init__(self): 
        self.ordenaMapa()

e = Mapa()
e.BCU()