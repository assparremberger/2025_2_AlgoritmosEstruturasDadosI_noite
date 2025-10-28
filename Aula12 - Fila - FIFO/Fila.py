from No import No

class Fila:

    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self, valor):
        nodo = No( valor )
        if self.inicio is None:
            self.inicio = nodo
        else:
            self.fim.prox = nodo
        self.fim = nodo
        self.imprimir()

    def imprimir(self):
        print( "-----------------------------------")
        print( "-- Fila - FIFO --")
        if self.inicio is None:
            print(" -- Fila Vazia -- ")
        else:
            aux = self.inicio
            txt = ""
            while aux != None:
                txt += " - " + aux.dado 
                aux = aux.prox
            print( txt )
        print( "-----------------------------------")

    def remove(self):
        if self.inicio is None:
            print( "Nenhum elemento removido" )
        else:
            self.inicio = self.inicio.prox
            if self.inicio is None:
                self.fim = None
        self.imprimir()    
