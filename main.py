import os
from PyQt5 import Qt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QColor
import test
from tkinter import messagebox
import nbrb
import urllib.request

import json


class Test(QtWidgets.QMainWindow, test.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonOkClick)
        self.textBrowser.setVisible(False)
        self.pushButton_Exit.clicked.connect(self.buttonExit)
        self.pushButton_Help.clicked.connect(self.buttonHelp)

    def buttonOkClick(self):
        self.window().setFixedHeight(826)
        self.window().setFixedWidth(428)
        self.textBrowser.setVisible(True)
        self.textBrowser.clear()
        typeOfCurrency = ""
        if self.checkBox_USD.isChecked():
            typeOfCurrency = '145'
        if self.checkBox_EURO.isChecked():
            typeOfCurrency = '292'
        if self.checkBox_RUB.isChecked():
            typeOfCurrency = '298'
        print(type(typeOfCurrency))
        api_endpoint = "http://www.nbrb.by/API/ExRates"
        print("sosoat")
        url = api_endpoint + "/Rates/Dynamics/" + str(typeOfCurrency) + "?startDate=2018-9-1&endDate=2018-9-30"
        print(url)
        response = urllib.request.urlopen(url)
        parseResponse = json.loads(response.read())
        Ratelist = []
        Dates = []
        getInf = ""
        for rate in parseResponse:
            Ratelist.append(float(rate['Cur_OfficialRate']))
        for item in Ratelist:
            print(item)
        for date in parseResponse:
            Dates.append(str(date['Date'])[:10])
        for item in Dates:
            print(item)
        if Ratelist[-1] >= Ratelist[-2]:
            getInf = "возрастет"
        else:
            getInf = "упадет"
        for i in range(len(Ratelist)):
            self.textBrowser.append("на " + Dates[i] + " число, значение - " + str(Ratelist[i]) + " byn")
        self.textBrowser.append("на основании приведенных результатов доллар - " + getInf)

    def buttonExit(self):
        self.window().setFixedHeight(322)
        self.window().setFixedWidth(260)
        self.textBrowser.setVisible(False)
        self.textBrowser.clear()

    def buttonHelp(self):
        self.textBrowser.setVisible(True)
        self.textBrowser.clear()
        self.window().setFixedHeight(826)
        self.window().setFixedWidth(428)
        self.textBrowser.append(
            "Для отображения динамики валюты, напротив названия необходимой валюты поставьте галочку"
            "Затем нажмите кнопку 'Отобразить информацию' "
            "Для возвращения назад(после нажатия кнопки 'Отобразить информацию' ), нажмите вернуться назад")


# pyuic5 untitled.ui -o test.py
# сделать интерфес отменасправква и допилиь диаграммы

if __name__ == '__main__':
    app = Qt.QApplication([])
    si = Test()
    si.show()
    app.exec()

# вывести значение джейсона в листбокс и сделать на основании этих данных оно возрастет или упадет
