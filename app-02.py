#!/usr/bin/python3
# coding: utf-8

import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication 

app = QApplication( sys.argv )

w = QWidget()
w.resize( 250 , 150 )
w.move( 300, 300 )
w.setWindowTitle( 'pyQt' )

btn = QPushButton( 'Clic' , w )
btn.setToolTip( 'Un bouton pour <b>cliquer</b>' )

btn.resize( btn.sizeHint() )
btn.move( 50 , 50 )

w.show()



sys.exit( app.exec_() )

