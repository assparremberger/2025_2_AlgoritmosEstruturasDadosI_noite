import sys
from PyQt5.QtWidgets import *
from Fisica import Fisica
from Cidade import Cidade
from TelaPessoa import TelaPessoa

class TelaFisica( TelaPessoa ):

    def __init__(self, titulo="Cadastro de Pessoa Física"):
        super().__init__(titulo)

        self.setGeometry(500, 100, 300, 200)

    def definirLayout(self):
        super().definirLayout()
        self.layout.addWidget( QLabel("CPF: " ) )
        self.txtCPF= QLineEdit(self)
        self.layout.addWidget( self.txtCPF)

    def salvar(self):
        nome = self.txtNome.text()
        cidade = Cidade( self.txtCidade.text() )
        cpf = self.txtCPF.text()
        pf = Fisica( nome, cidade, cpf)
        self.txtNome.setText( "" )
        self.txtCidade.setText( "" )
        self.txtCPF.setText( "" )
        QMessageBox.information( self , "Pessoa Física Cadastrada" , str( pf ) +
                "\n cadastrado(a) com sucesso!" )