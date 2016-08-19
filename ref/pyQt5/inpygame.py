
from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import pygame
import sys
import pygame.camera
import pygame.image
from PIL import ImageQt, Image
import time

pygame.camera.init()

cameras = pygame.camera.list_cameras()

print( "Using camera %s ..." % cameras[0])

webcam = pygame.camera.Camera(cameras[0])

webcam.start()

# grab first frame
img = webcam.get_image()

WIDTH = img.get_width()
HEIGHT = img.get_height()

class ImageWidget(QWidget):
    def __init__(self,surface,parent=None):
        super(ImageWidget,self).__init__(parent)
        WIDTH=surface.get_width()
        HEIGHT=surface.get_height()
        rawData = pygame.image.tostring(surface, "RGBA", False)
        PilImage = Image.frombytes('RGBA', (WIDTH, HEIGHT), rawData)
        QtImage1 = ImageQt.ImageQt(PilImage)
        QtImage2 = QtGui.QImage(QtImage1)
        pixmap = QtGui.QPixmap.fromImage(QtImage2)
        self.label = QtWidgets.QLabel('', self)
        self.label.setPixmap(pixmap)


    def drawImage(self):
        surface = webcam.get_image()
        WIDTH = surface.get_width()
        HEIGHT = surface.get_height()
        rawData = pygame.image.tostring(surface, "RGBA", False)
        PilImage = Image.frombytes('RGBA', (WIDTH, HEIGHT), rawData)
        QtImage1 = ImageQt.ImageQt(PilImage)
        QtImage2 = QtGui.QImage(QtImage1)
        pixmap = QtGui.QPixmap.fromImage(QtImage2)
        self.label.setPixmap(pixmap)
        self.label.update()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,surface,parent=None):
        super(MainWindow,self).__init__(parent)
        self.resize(640, 480)
        self.setCentralWidget(ImageWidget(surface))
        self.timer = QTimer()
        self.timer.timeout.connect(self.centralWidget().drawImage)
        self.timer.start(1)



app=QApplication(sys.argv)
w=MainWindow(img)
w.show()


app.exec_()
