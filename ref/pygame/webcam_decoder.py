import pygame.camera
import pygame.image
import sys
from PIL import Image
import zbarlight

pygame.camera.init()

cameras = pygame.camera.list_cameras()

print( "Using camera %s ..." % cameras[0])

webcam = pygame.camera.Camera(cameras[0])

webcam.start()

# grab first frame
img = webcam.get_image()

WIDTH = img.get_width()
HEIGHT = img.get_height()

rawData = pygame.image.tostring(img, "RGBA", False)
img = Image.frombytes('RGBA', (WIDTH, HEIGHT), rawData)

screen = pygame.display.set_mode( ( WIDTH, HEIGHT ) )
pygame.display.set_caption("pyGame Camera View")

while True:
    img = webcam.get_image()
    # draw frame
    screen.blit(img, (0, 0))
    pygame.display.flip()
    rawData = pygame.image.tostring(img, "RGBA", False)
    img = Image.frombytes('RGBA', (WIDTH, HEIGHT), rawData)
    codes = zbarlight.scan_codes('qrcode', img)

    if codes!=None:
        print('QR codes: %s' % codes)