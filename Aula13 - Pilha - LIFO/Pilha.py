from No import No

class Pilha:

    def __init__(self):
        self.topo = None

    def add(self, valor):
        nodo = No( valor )
        if self.topo != None:
            nodo.prox = self.topo
        self.topo = nodo
        self.imprimir()

    def imprimir(self):
        print( "---- Pilha - LIFO -----------------------")
        if self.topo is None:
            print(" -- Pilha Vazia -- ")
        else:
            aux = self.topo
            while aux != None:
                print( aux.dado )
                aux = aux.prox
        print( "-----------------------------------")

    def remove(self):
        if self.topo is None:
            print("Nenhum elemento removido")
        else:
            self.topo = self.topo.prox
        self.imprimir()