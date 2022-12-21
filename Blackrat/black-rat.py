import sys
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi

def chama_setup():
    setup.show()

app=QtWidgets.QApplication([])
login=uic.loadUi("login.ui")
setup=uic.loadUi("setup.ui")
login.QPushButton_login.clicked.connect(chama_setup)

login.show()
app.exec()