#!/usr/bin/python3
# coding: utf-8

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


app = QApplication( sys.argv )

w = QMainWindow()
w.resize( 250 , 150 )
w.move( 300, 300 )
w.setWindowTitle( 'pyQt' )
w.statusBar().showMessage( 'Ok' )
w.show()

sys.exit( app.exec_() )


