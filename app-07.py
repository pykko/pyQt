#!/usr/bin/python3
# coding: utf-8

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow , QMenu , QAction


app = QApplication( sys.argv )

w = QMainWindow()
w.resize( 250 , 150 )
w.move( 300, 300 )
w.setWindowTitle( 'pyQt' )
w.statusBar().showMessage( 'Ok' )





barreMenus = w.menuBar()
menuFichier = barreMenus.addMenu( 'Fichier' )

actionOuvrir = QAction( None , 'Ouvrir' , w )
menuFichier.addAction( actionOuvrir )

actionFermer = QAction( None , 'Fermer fichier' , w )
menuFichier.addMenu( actionFermer )


w.show()

sys.exit( app.exec_() )


