# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(351, 463)
        MainWindow.setStyleSheet("background-color: rgb(118, 125, 129);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 141, 31))
        self.label.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(20, 230, 241, 28))
        self.pushButton.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 0, 0);\n"
"border-color: rgb(255, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.checkBox_USD = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_USD.setGeometry(QtCore.QRect(30, 120, 141, 20))
        self.checkBox_USD.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.checkBox_USD.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.checkBox_USD.setObjectName("checkBox_USD")
        self.checkBox_EURO = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_EURO.setGeometry(QtCore.QRect(30, 150, 131, 20))
        self.checkBox_EURO.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.checkBox_EURO.setObjectName("checkBox_EURO")
        self.checkBox_RUB = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_RUB.setGeometry(QtCore.QRect(30, 180, 171, 20))
        self.checkBox_RUB.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.checkBox_RUB.setObjectName("checkBox_RUB")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 40, 401, 691))
        self.textBrowser.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 255, 127);")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_Exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Exit.setGeometry(QtCore.QRect(160, 740, 141, 31))
        self.pushButton_Exit.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"background-color: rgb(204, 204, 204);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.pushButton_Help = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Help.setGeometry(QtCore.QRect(10, 0, 75, 31))
        self.pushButton_Help.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.pushButton_Help.setObjectName("pushButton_Help")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 351, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Выбор валюты"))
        self.pushButton.setText(_translate("MainWindow", "Отобразить информацию "))
        self.checkBox_USD.setText(_translate("MainWindow", "доллар "))
        self.checkBox_EURO.setText(_translate("MainWindow", "Евро"))
        self.checkBox_RUB.setText(_translate("MainWindow", "Российский рубль"))
        self.pushButton_Exit.setText(_translate("MainWindow", "Вернуться назад"))
        self.pushButton_Help.setText(_translate("MainWindow", "Справка"))

