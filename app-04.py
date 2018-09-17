#!/usr/bin/python3
# coding: utf-8

import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication , QMessageBox
from PyQt5.QtCore import pyqtSlot

@pyqtSlot()
def afficherMsg() :
	print( 'Message' )
	
	reponse = QMessageBox.question( w, 'Message', "Quitter ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
	
	if reponse == QMessageBox.Yes :
		print( 'Yes' )
		QApplication.instance().quit()
	
	
if __name__ == '__main__' :

	app = QApplication( sys.argv )

	w = QWidget()
	w.resize( 250 , 150 )
	w.move( 300, 300 )
	w.setWindowTitle( 'pyQt' )

	btn = QPushButton( 'Quitter' , w )
	btn.clicked.connect( afficherMsg )
	btn.setToolTip( 'Un bouton pour <b>afficher un message</b>' )

	btn.resize( btn.sizeHint() )
	btn.move( 50 , 50 )

	w.show()



	sys.exit( app.exec_() )

