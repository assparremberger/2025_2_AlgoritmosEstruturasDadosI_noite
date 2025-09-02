class Cidade:

    def __init__(self, nome = "Tangamandápio"):
        self.nome = nome
        self.populacao = 0

    def __str__(self):
        return "Cidade: " + self.nome