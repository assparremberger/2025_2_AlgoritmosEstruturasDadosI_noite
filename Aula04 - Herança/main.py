import sys
from PyQt5.QtWidgets import *

from TelaPessoa import TelaPessoa
from TelaFisica import TelaFisica
app = QApplication( sys.argv )


tp = TelaPessoa()
tp.show()

tf = TelaFisica()
tf.show()


sys.exit( app.exec_() )
