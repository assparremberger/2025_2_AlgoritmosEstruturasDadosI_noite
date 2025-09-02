import sys
from PyQt5.QtWidgets import *
from Cidade import Cidade

class TelaCidade( QMainWindow ):

    def __init__(self, titulo = "Cadastro de Cidade" , cidades = []):
        super().__init__()
        self.cidades = cidades
        self.setWindowTitle( titulo )
        self.setGeometry(100, 100, 200, 100)
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
        if nome != "" :
            cid = Cidade( nome )
            self.cidades.append( cid )
            self.txtNome.setText( "" )
            QMessageBox.information( self , "Cidade Cadastrada" , str(cid) + 
                                "\n cadastrado(a) com sucesso!" )
            self.hide()

    def definirLayout(self):
        self.lblNome = QLabel("Nome: ")
        self.txtNome = QLineEdit(self)
        self.layout.addWidget(self.lblNome)
        self.layout.addWidget(self.txtNome)
        
    


