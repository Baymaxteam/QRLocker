import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QTextEdit, QWidget, QDialog, QApplication
import mainwindow_ui, qrcode_widget_ui
from PIL import ImageQt, Image
import qrcode


class MyPopup(QWidget, qrcode_widget_ui.Ui_Widget):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setGeometry(580, 50, 100, 100)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 產生無框視窗
        self.keyMakeButton.clicked.connect(self.generatingKey)

    def generatingKey(self):
        key = self.QRtextEdit.toPlainText()
        print("Recieved key:{}".format(key))
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=2,
        )
        qr.add_data(key)
        qr.make(fit=True)
        img = qr.make_image()
        QtImage1 = ImageQt.ImageQt(img)
        QtImage2 = QtGui.QImage(QtImage1)
        pixmap = QtGui.QPixmap.fromImage(QtImage2)
        self.QRcodeLabel.setPixmap(pixmap)


class MainWindow(QtWidgets.QMainWindow, mainwindow_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setGeometry(40,50,100,100)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # 產生無框視窗
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 設定半透明
        self.keyWidgetButton.clicked.connect(self.popingNewWidegt)
        self.w = None

    def popingNewWidegt(self):
        print("Opening a new popup window...")
        self.w = MyPopup()
        self.w.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())