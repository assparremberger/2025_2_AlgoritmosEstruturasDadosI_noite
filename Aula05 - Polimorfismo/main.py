import sys
from PyQt5.QtWidgets import *

from TelaPessoa import TelaPessoa
#from TelaFisica import TelaFisica

from TelaCidade import TelaCidade
from Cidade import Cidade

app = QApplication( sys.argv )

cid1 = Cidade()
cid2 = Cidade("Porto Alegre")

cidades = [cid1, cid2]
tc = TelaCidade( cidades = cidades)

tp = TelaPessoa(tc, cidades)
tc.telaPessoa = tp
tp.show()

#tf = TelaFisica()
#tf.show()


sys.exit( app.exec_() )
