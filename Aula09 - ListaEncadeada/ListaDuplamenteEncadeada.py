from No import No
# Lista Duplamente Encadeada em ordem crescente
class ListaDuplamenteEncadeada:
     
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self, valor):
        nodo = No( valor )
        if self.inicio == None:
            self.inicio = nodo
            self.fim = nodo
        else:
            if nodo.dado < self.inicio.dado :
                nodo.proximo = self.inicio
                self.inicio.anterior = nodo
                self.inicio = nodo
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux != None :
                    if nodo.dado < aux.dado:
                        ant.proximo = nodo
                        nodo.proximo = aux
                        nodo.anterior = ant     #nodo.anterior = aux.anterior
                        aux.anterior = nodo
                        break
                    else:
                        ant = aux
                        aux = aux.proximo
                if aux is None:
                    ant.proximo = nodo
                    nodo.anterior = ant 
                    self.fim = nodo
        self.imprimir()

    def imprimir(self):
        print( "-----------------------------------")
        print( "Lista Duplamente Encadeada em ordem crescente")
        if self.inicio is None:
            print(" -- Lista Vazia -- ")
        else:
            aux = self.inicio
            while aux != None:
                print( aux.dado )
                aux = aux.proximo
        print( "-----------------------------------")

    def imprimirReverso(self):
        print( "-----------------------------------")
        print( "Lista DUplamente Encadeada em ordem crescente Reversa")
        if self.inicio is None:
            print(" -- Lista Vazia -- ")
        else:
            aux = self.fim
            while aux != None:
                print( aux.dado )
                aux = aux.anterior
        print( "-----------------------------------")
            

    def remove(self, valor):
        if self.inicio is None:
            print( "Nada removido, pois a lista está vazia")
        else:
            removeu = False
            if valor == self.inicio.dado:
                self.inicio = self.inicio.proximo
                if self.inicio is None:
                    self.fim = None
                removeu = True
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux != None:
                    if valor == aux.dado:
                        ant.proximo = aux.proximo
                        #falta finalizar aqui
                        aux.proximo.anterior =  ant
                        removeu = True
                        break
                    else:
                        ant = aux
                        aux = aux.proximo
            if removeu: 
                print( "Elemento " + valor + " removido!")
            else:
                print( "Elemento " + valor + " não encontrado!")
            
            self.imprimir()


    