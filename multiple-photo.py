from picamera import PiCamera
from time import sleep
import os

camera = PiCamera()
camera.rotation = 270

folder = os.mkdir('/home/pi/Desktop/test')

camera.start_preview(alpha=100)
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Desktop/test/image%s.jpg' % (i+1))
camera.stop_preview()