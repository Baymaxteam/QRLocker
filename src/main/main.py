import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QTextEdit, QWidget, QDialog, QApplication, QLabel
import mainwindow_ui, qrcode_widget_ui
from PIL import ImageQt, Image
import qrcode
import pygame.camera
import pygame.image
from PIL import Image
import zbarlight
import RPi.GPIO as GPIO


class aboutMe(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.label = QLabel(self) 
        pixmap = QtGui.QPixmap('aboutMe.jpg')
        pixmap = pixmap.scaledToWidth(500)
        self.label.setPixmap(pixmap)
        self.setGeometry(0, 0, pixmap.width(), pixmap.height())


class MyPopup(QWidget, qrcode_widget_ui.Ui_Widget):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setGeometry(580, 50, 100, 100)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 產生無框視窗
        self.keyMakeButton.clicked.connect(self.generatingKey)
        self.closeWidgetButton.clicked.connect(self.close)

    def generatingKey(self):
        key = self.QRtextEdit.toPlainText()
        print("[Encoder] Recieved key:{}".format(key))
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
        self.KEY = key


class MainWindow(QtWidgets.QMainWindow, mainwindow_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setGeometry(40,50,100,100)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # 產生無框視窗
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 設定半透明
        self.keyWidgetButton.clicked.connect(self.popingNewWidegt)
        self.w = None
        self.w = MyPopup()
        self.enableCamButton.clicked.connect(self.startCam)
        self.w.KEY = '000000'
        self.doorState = False
        self.doorControlButton.clicked.connect(self.doorTrigger)
        self.aboutInfoButton.clicked.connect(self.aboutMeEvent)        
        self.aboutW = None
        self.aboutW = aboutMe()
         

    def aboutMeEvent(self):
        self.aboutW.show()

    def popingNewWidegt(self):
        print("Opening a new popup window...")
        self.w.show()

    def loadingCamimage(self):
        img = webcam.get_image()
        WIDTH = img.get_width()
        HEIGHT = img.get_height()
        rawData = pygame.image.tostring(img, "RGBA", False)
        img = Image.frombytes('RGBA', (WIDTH, HEIGHT), rawData)
        codes = zbarlight.scan_codes('qrcode', img)
        QtImage1 = ImageQt.ImageQt(img)
        QtImage2 = QtGui.QImage(QtImage1)
        pixmap = QtGui.QPixmap.fromImage(QtImage2)
        self.WebCamLabel.setPixmap(pixmap)
        if codes != None:
            print('[Decoder] QR codes: {}'.format(codes[0]))
            if(codes[0].decode() == self.w.KEY and self.doorState==False):
                self.InfotextBrowser.append("Key accept! Door open")
                self.doorState = True
                GPIO.output(21, 1)


    def startCam(self):
        self.InfotextBrowser.append("enable camera for 2 min")
        self.cam_plot_timer = QtCore.QTimer()
        self.cam_plot_timer.timeout.connect(self.loadingCamimage)
        self.cam_plot_timer.start(50)
        self.cam_timer = QtCore.QTimer()
        self.cam_timer.singleShot(12000, self.stopCam)

    def stopCam(self):
        self.InfotextBrowser.append("time out. close camera...")
        self.cam_plot_timer.stop()

    def doorTrigger(self):
        if(self.doorState == False):
            self.InfotextBrowser.append("door opening...")
            self.doorState = True
            GPIO.output(21, 1)
        elif (self.doorState == True):
            self.InfotextBrowser.append("door closing...")
            self.doorState = False
            GPIO.output(21, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    pygame.camera.init()
    cameras = pygame.camera.list_cameras()
    print("Using camera %s ..." % cameras[0])
    webcam = pygame.camera.Camera(cameras[0])

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)

    webcam.start()
    window.show()
    sys.exit(app.exec_())
