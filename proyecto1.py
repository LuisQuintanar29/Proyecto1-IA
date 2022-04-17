
class Mapa:
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
    def printEstados(self):
        for k in self.estados:
            print(k,":",self.estados[k])
    # Ordena el mapa por orden alfanumerico, tanto los estados como sus vecinos
    def ordenaMapa(self):
        tempEstados = self.estados
        self.estados = {}
        for p in sorted(tempEstados):
            self.estados[p] = tempEstados[p]
            self.estados[p] = {}
            for q in sorted(tempEstados[p]):
                self.estados[p][q] = tempEstados[p][q]
    # Constructor. Cuando se instancia un objeto, ordena el mapa
    def __init__(self): 
        self.ordenaMapa()
        pass

e = Mapa()
e.printEstados()