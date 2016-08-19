# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qrcode_nonnameing.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 400)
        Form.setStyleSheet("background-color: rgba(4, 20, 20, 100)")
        self.QRcodeLabel = QtWidgets.QLabel(Form)
        self.QRcodeLabel.setGeometry(QtCore.QRect(40, 20, 320, 240))
        self.QRcodeLabel.setMinimumSize(QtCore.QSize(320, 240))
        self.QRcodeLabel.setMaximumSize(QtCore.QSize(320, 240))
        self.QRcodeLabel.setAutoFillBackground(False)
        self.QRcodeLabel.setStyleSheet("background-color:rgb(162, 162, 162)")
        self.QRcodeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.QRcodeLabel.setObjectName("QRcodeLabel")
        self.QRtextEdit = QtWidgets.QTextEdit(Form)
        self.QRtextEdit.setGeometry(QtCore.QRect(40, 280, 321, 41))
        self.QRtextEdit.setStyleSheet("background-color:rgb(200, 200, 200)")
        self.QRtextEdit.setObjectName("QRtextEdit")
        self.keyMakeButton = QtWidgets.QPushButton(Form)
        self.keyMakeButton.setGeometry(QtCore.QRect(40, 350, 90, 31))
        self.keyMakeButton.setStyleSheet("background-color: rgb(200, 200, 200)")
        self.keyMakeButton.setObjectName("keyMakeButton")
        self.closeWidgetButton = QtWidgets.QPushButton(Form)
        self.closeWidgetButton.setGeometry(QtCore.QRect(270, 350, 90, 31))
        self.closeWidgetButton.setStyleSheet("background-color: rgb(200, 200, 200)")
        self.closeWidgetButton.setObjectName("closeWidgetButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.QRcodeLabel.setText(_translate("Form", "QRcode Image"))
        self.keyMakeButton.setText(_translate("Form", "產生鑰匙"))
        self.closeWidgetButton.setText(_translate("Form", "結束"))

