# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_nonnameing.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(62, 62, 62)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.InfotextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.InfotextBrowser.setGeometry(QtCore.QRect(30, 290, 441, 192))
        self.InfotextBrowser.setStyleSheet("background-color:rgb(200, 200, 200)\n"
"")
        self.InfotextBrowser.setObjectName("InfotextBrowser")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 502, 286))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(20, 0, 20, 0)
        self.gridLayout.setHorizontalSpacing(50)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 30, -1, 20)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.enableCamButton = QtWidgets.QPushButton(self.layoutWidget)
        self.enableCamButton.setStyleSheet("background-color: rgb(200, 200, 200)")
        self.enableCamButton.setObjectName("enableCamButton")
        self.verticalLayout.addWidget(self.enableCamButton)
        self.keyWidgetButton = QtWidgets.QPushButton(self.layoutWidget)
        self.keyWidgetButton.setStyleSheet("background-color: rgb(200, 200, 200)")
        self.keyWidgetButton.setObjectName("keyWidgetButton")
        self.verticalLayout.addWidget(self.keyWidgetButton)
        self.doorControlButton = QtWidgets.QPushButton(self.layoutWidget)
        self.doorControlButton.setStyleSheet("background-color: rgb(200, 200, 200)")
        self.doorControlButton.setObjectName("doorControlButton")
        self.verticalLayout.addWidget(self.doorControlButton)
        self.aboutInfoButton = QtWidgets.QPushButton(self.layoutWidget)
        self.aboutInfoButton.setStyleSheet("background-color: rgb(200, 200, 200)")
        self.aboutInfoButton.setObjectName("aboutInfoButton")
        self.verticalLayout.addWidget(self.aboutInfoButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.WebCamLabel = QtWidgets.QLabel(self.layoutWidget)
        self.WebCamLabel.setMinimumSize(QtCore.QSize(320, 240))
        self.WebCamLabel.setMaximumSize(QtCore.QSize(320, 240))
        self.WebCamLabel.setAutoFillBackground(False)
        self.WebCamLabel.setStyleSheet("background-color:rgb(162, 162, 162)")
        self.WebCamLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.WebCamLabel.setObjectName("WebCamLabel")
        self.gridLayout.addWidget(self.WebCamLabel, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.enableCamButton.setText(_translate("MainWindow", "啟動相機"))
        self.keyWidgetButton.setText(_translate("MainWindow", "產生鑰匙"))
        self.doorControlButton.setText(_translate("MainWindow", "手動控制"))
        self.aboutInfoButton.setText(_translate("MainWindow", "關於我們"))
        self.WebCamLabel.setText(_translate("MainWindow", "Webcam Image"))

