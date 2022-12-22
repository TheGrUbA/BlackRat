import os
import Potion
from PyQt5 import QtCore, QtGui, QtWidgets

class Setup_MainWindow(object):    

    def __init__(self):
        self.pocoes = Potion.Pocoes()

    def pararPrograma(self):
        os._exit(0)          

    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(375, 500)
        MainWindow.setMinimumSize(QtCore.QSize(375, 500))
        MainWindow.setMaximumSize(QtCore.QSize(375, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logorat/images/favicon-blackrat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(17, 17, 17);\n"
                                "color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_seteup = QtWidgets.QFrame(self.centralwidget)
        self.frame_seteup.setGeometry(QtCore.QRect(0, 0, 381, 471))
        self.frame_seteup.setStyleSheet("background-color: rgb(17, 17, 17);")
        self.frame_seteup.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_seteup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_seteup.setObjectName("frame_seteup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_seteup)
        self.verticalLayout.setContentsMargins(12, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame_seteup)
        self.frame_2.setMaximumSize(QtCore.QSize(351, 76))
        self.frame_2.setStyleSheet("background-color: rgb(17, 17, 17);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_setup1 = self.criarBotaoMenu(self.frame_2, QtCore.QRect(10, 10, 40, 51), ":/logorat/images/play.png")
        self.pushButton_setup1.setObjectName("pushButton_setup1")
        self.pushButton_setup2 = self.criarBotaoMenu(self.frame_2, QtCore.QRect(70, 10, 40, 51), ":/logorat/images/pause.png")
        self.pushButton_setup2.setObjectName("pushButton_setup2")
        self.pushButton_setup3 = self.criarBotaoMenu(self.frame_2, QtCore.QRect(130, 10, 40, 51), ":/logorat/images/stop.png")
        self.pushButton_setup3.setObjectName("pushButton_setup3")
        self.pushButton_setup3.clicked.connect(self.pararPrograma)
        self.label_start_setup = QtWidgets.QLabel(self.frame_2)
        self.label_start_setup.setGeometry(QtCore.QRect(200, 10, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_start_setup.setFont(font)
        self.label_start_setup.setStyleSheet("text-align:center;")
        self.label_start_setup.setObjectName("label_start_setup")
        self.label_showhud_setup = QtWidgets.QLabel(self.frame_2)
        self.label_showhud_setup.setGeometry(QtCore.QRect(270, 10, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_showhud_setup.setFont(font)
        self.label_showhud_setup.setStyleSheet("text-align:center;")
        self.label_showhud_setup.setObjectName("label_showhud_setup")
        self.lineEdit_setup = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_setup.setGeometry(QtCore.QRect(200, 30, 51, 21))
        self.lineEdit_setup.setStyleSheet("QLineEdit {\n"
                                        "    text-align:center;\n"
                                        "    border-radius: 5px;\n"
                                        "    background-color: rgb(35, 35, 35);\n"
                                        "    padding-left: 3px;\n"
                                        "}")
        self.lineEdit_setup.setObjectName("lineEdit_setup")
        self.lineEdit_setup2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_setup2.setGeometry(QtCore.QRect(270, 30, 51, 20))
        self.lineEdit_setup2.setStyleSheet("QLineEdit {\n"
                                        "    text-align:center;\n"
                                        "    border-radius: 5px;\n"
                                        "    background-color: rgb(35, 35, 35);\n"
                                        "    padding-left: 3px;\n"
                                        "}")
        self.lineEdit_setup2.setObjectName("lineEdit_setup2")
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame_seteup)
        self.frame_3.setMaximumSize(QtCore.QSize(350, 50))
        self.frame_3.setStyleSheet("background-color: rgb(17, 17, 17);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_flaskbuild = QtWidgets.QLabel(self.frame_3)
        self.label_flaskbuild.setGeometry(QtCore.QRect(10, 15, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_flaskbuild.setFont(font)
        self.label_flaskbuild.setObjectName("label_flaskbuild")
        self.pushButton_removeall = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_removeall.setGeometry(QtCore.QRect(260, 12, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_removeall.setFont(font)
        self.pushButton_removeall.setStyleSheet("QPushButton {\n"
                                                "    border: no;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:pressed {\n"
                                                "    color: rgb(170, 255, 0);\n"
                                                "}")
        self.pushButton_removeall.setObjectName("pushButton_removeall")
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_seteup)
        self.frame_4.setMaximumSize(QtCore.QSize(350, 324))
        self.frame_4.setToolTipDuration(1)
        self.frame_4.setStyleSheet("background-color: rgb(17, 17, 17);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_flask1 = self.createFlaskButton(self.frame_4, QtCore.QRect(5, 80, 62, 164), self.pocoes.getPotion(1))
        self.pushButton_flask1.setObjectName("pushButton_flask1")
        self.pushButton_flask2 = self.createFlaskButton(self.frame_4, QtCore.QRect(75, 80, 62, 164), self.pocoes.getPotion(2))
        self.pushButton_flask2.setObjectName("pushButton_flask2")
        self.pushButton_flask3 = self.createFlaskButton(self.frame_4, QtCore.QRect(145, 80, 62, 164), self.pocoes.getPotion(3))
        self.pushButton_flask3.setObjectName("pushButton_flask3")
        self.pushButton_flask4 = self.createFlaskButton(self.frame_4, QtCore.QRect(214, 80, 62, 164), self.pocoes.getPotion(4))
        self.pushButton_flask4.setObjectName("pushButton_flask4")
        self.pushButton_flask5 = self.createFlaskButton(self.frame_4, QtCore.QRect(283, 80, 62, 164), self.pocoes.getPotion(5))
        self.pushButton_flask5.setObjectName("pushButton_flask5")
        self.pushButton_flask_cancel1 = self.createCancelButton(self.frame_4, QtCore.QRect(23, 250, 22, 22), ":/logorat/images/plus.png",":/logorat/images/cancel-pressed.png")
        self.pushButton_flask_cancel1.setObjectName("pushButton_flask_cancel1")
        self.pushButton_flask_cancel2 = self.createCancelButton(self.frame_4, QtCore.QRect(96, 250, 22, 22), ":/logorat/images/plus.png",":/logorat/images/cancel-pressed.png")
        self.pushButton_flask_cancel2.setObjectName("pushButton_flask_cancel2")
        self.pushButton_flask_cancel3 = self.createCancelButton(self.frame_4, QtCore.QRect(165, 250, 22, 22), ":/logorat/images/plus.png",":/logorat/images/cancel-pressed.png")
        self.pushButton_flask_cancel3.setObjectName("pushButton_flask_cancel3")
        self.pushButton_flask_cancel4 = self.createCancelButton(self.frame_4, QtCore.QRect(233, 250, 22, 22), ":/logorat/images/plus.png",":/logorat/images/cancel-pressed.png")
        self.pushButton_flask_cancel4.setObjectName("pushButton_flask_cancel4")
        self.pushButton_flask_cancel5 = self.createCancelButton(self.frame_4, QtCore.QRect(304, 250, 22, 22), ":/logorat/images/plus.png",":/logorat/images/cancel-pressed.png")
        self.pushButton_flask_cancel5.setObjectName("pushButton_flask_cancel5")
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_4_setup_back = QtWidgets.QFrame(self.centralwidget)
        self.frame_4_setup_back.setGeometry(QtCore.QRect(0, 470, 375, 30))
        self.frame_4_setup_back.setStyleSheet("background-color: rgb(17, 17, 17);")
        self.frame_4_setup_back.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4_setup_back.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4_setup_back.setObjectName("frame_4_setup_back")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Black Rat Setup"))
        self.label_start_setup.setText(_translate("MainWindow", "Start:"))
        self.label_showhud_setup.setText(_translate("MainWindow", "Show HUD:"))
        self.lineEdit_setup.setPlaceholderText(_translate("MainWindow", "F2"))
        self.lineEdit_setup2.setPlaceholderText(_translate("MainWindow", "F3"))
        self.label_flaskbuild.setText(_translate("MainWindow", "FLASK BUILD"))
        self.pushButton_removeall.setText(_translate("MainWindow", "Remove All"))

    def criarBotaoMenu(self, frame, button_geometry, button_image_path):
        pushButton = QtWidgets.QPushButton(frame)
        pushButton.setGeometry(button_geometry)
        pushButton.setStyleSheet("QPushButton {\n"
                                "    background-image: url("+button_image_path+");\n"
                                "    background-repeat: no-repeat;\n"
                                "    background-position: center;\n"
                                "    border: no;\n"
                                "}\n"
                                "\n"
                                "QPushButton:hover {\n"
                                "    border: 2px solid rgb(255, 255, 255)\n"
                                "}\n"
                                "\n"
                                "QPushButton:pressed {\n"
                                "    border: 2px solid rgb(170, 255, 0)\n"
                                "}")
        pushButton.setText("")
        return pushButton

    def createFlaskButton(self, frame, button_geometry, button_image_path):
        pushButton = QtWidgets.QPushButton(frame)
        pushButton.setGeometry(button_geometry)
        pushButton.setStyleSheet("QPushButton {\n"
                                "    background-image: url("+button_image_path+");\n"
                                "    background-position:center;\n"
                                "    background-repeat: no-repeat;\n"
                                "    background-color: rgb(35, 35, 35);\n"
                                "    border-radius: 10px;\n"
                                "}\n"
                                "\n"
                                "QPushButton:hover {\n"
                                "    border: 2px solid rgb(255, 255, 255)\n"
                                "}\n"
                                "\n"
                                "QPushButton:pressed {\n"
                                "    border: 2px solid rgb(170, 255, 0);\n"
                                "}")
        pushButton.setText("")
        return pushButton

    def createCancelButton(self, frame, button_geometry, button_image_path, button_image_pressed_path):
        pushButton = QtWidgets.QPushButton(frame)
        pushButton.setGeometry(button_geometry)
        pushButton.setStyleSheet("QPushButton {    \n"
                                "    background-image: url("+button_image_path+");\n"
                                "    background-position:center;\n"
                                "    background-repeat: no-repeat;\n"
                                "    border: no;\n"
                                "}\n"
                                "\n"
                                "QPushButton:pressed {    \n"
                                "    background-image: url("+button_image_pressed_path+");\n"
                                "}\n"
                                "")
        pushButton.setText("")
        return pushButton

import file_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Setup_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())