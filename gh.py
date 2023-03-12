from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(783, 447)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 151, 471))
        self.tableWidget.setStyleSheet("background-color: rgb(35, 136, 192);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 60, 151, 61))
        self.pushButton.setStyleSheet("background-color: rgb(35, 136, 192);\n"
"font: 75 10pt \"GetVoIP Grotesque\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 120, 151, 61))
        self.pushButton_2.setStyleSheet("background-color: rgb(35, 136, 192);\n"
"font: 75 10pt \"GetVoIP Grotesque\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 141, 41))
        font = QtGui.QFont()
        font.setFamily("GetVoIP Grotesque")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 20pt \"GetVoIP Grotesque\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 180, 151, 61))
        self.pushButton_3.setStyleSheet("background-color: rgb(35, 136, 192);\n"
"font: 75 10pt \"GetVoIP Grotesque\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 20, 51, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 75 50pt \"GetVoIP Grotesque\";\n"
"font: 50ptpt \"Arial\";")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Оптимизация"))
        self.pushButton_2.setText(_translate("MainWindow", "Очистить ОЗУ"))
        self.label.setText(_translate("MainWindow", "   OptiPC"))
        self.pushButton_3.setText(_translate("MainWindow", "Очистить мусор"))
        self.label_2.setText(_translate("MainWindow", "6"))

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
