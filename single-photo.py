from picamera import PiCamera
from time import sleep
import time

camera = PiCamera()
camera.rotation = 270


camera.start_preview(alpha=100)
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()