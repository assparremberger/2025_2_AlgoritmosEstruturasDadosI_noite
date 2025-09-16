import sys
from PyQt5.QtWidgets import *
from Pessoa import Pessoa
from Cidade import Cidade
from abc import ABC, abstractmethod
from TelaCidade import TelaCidade

class TelaPessoa( QMainWindow, ABC ):

    def __init__(self, telaCid, cidades, titulo = "Cadastro de Pessoa" ):
        super().__init__()
        self.telaCidade = telaCid
        self.cidades = cidades
        self.setWindowTitle( titulo )
        self.setGeometry(100, 100, 300, 150)
        self.layout = QVBoxLayout()

        self.definirLayout()
        self.btnSalvar = QPushButton( "Salvar" , self )
        self.btnSalvar.clicked.connect( self.salvar )
        self.layout.addWidget( self.btnSalvar )

        container = QWidget()
        container.setLayout( self.layout )
        self.setCentralWidget( container )

    @abstractmethod
    def salvar(self):
        pass



    def definirLayout(self):
        self.lblNome = QLabel("Nome: ")
        self.txtNome = QLineEdit(self)
        #self.lblCidade = QLabel("Cidade: ")
        self.cmbCidade = QComboBox(self)
        self.carregarCidades()
        self.btnAddCidade = QPushButton("Adicionar cidade...", self)
        self.btnAddCidade.clicked.connect( self.abrirTelaCidade )

        self.layout.addWidget(self.lblNome)
        self.layout.addWidget(self.txtNome)
        self.layout.addWidget( QLabel("Cidade: ") )
        self.layout.addWidget(self.cmbCidade)
        self.layout.addWidget( self.btnAddCidade )

    def carregarCidades(self):
        self.cmbCidade.clear()
        self.cmbCidade.addItem( "Selecione..." , None )
        for cid in self.cidades:
            self.cmbCidade.addItem( cid.nome , cid )

    def abrirTelaCidade(self):
        self.telaCidade.show()



    


