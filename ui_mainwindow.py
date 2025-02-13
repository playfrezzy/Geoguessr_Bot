from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 50)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setObjectName("button")
        self.verticalLayout.addWidget(self.button)
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setObjectName("result_label")
        self.result_label.setWordWrap(True)
        self.verticalLayout.addWidget(self.result_label)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtWidgets.QApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GeoGuessr Bot"))
        self.button.setText(_translate("MainWindow", "Take Screenshot and Process"))
        self.result_label.setText(_translate("MainWindow", "Results will appear here"))
