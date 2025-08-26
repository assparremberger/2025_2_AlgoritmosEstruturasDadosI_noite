import sys
from PyQt5.QtWidgets import *
from Pessoa import Pessoa
from Cidade import Cidade

class TelaPessoa( QMainWindow ):

    def __init__(self, titulo = "Cadastro de Pessoa"):
        super().__init__()
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

    def salvar(self):
        nome = self.txtNome.text()
        cidade = Cidade( self.txtCidade.text() )
        pessoa = Pessoa( nome, cidade)
        self.txtNome.setText( "" )
        self.txtCidade.setText( "" )
        QMessageBox.information( self , "Pessoa Cadastrada" , nome + " cadastrado(a) com sucesso!" )


    def definirLayout(self):
        self.lblNome = QLabel("Nome: ")
        self.txtNome = QLineEdit(self)
        #self.lblCidade = QLabel("Cidade: ")
        self.txtCidade = QLineEdit(self)
        self.layout.addWidget(self.lblNome)
        self.layout.addWidget(self.txtNome)
        self.layout.addWidget( QLabel("Cidade: ") )
        self.layout.addWidget(self.txtCidade)
    


