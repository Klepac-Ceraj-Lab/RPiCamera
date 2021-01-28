from picamera import PiCamera
from time import sleep
import os
from datetime import datetime

camera = PiCamera()

dir = '/home/anika/Pictures/5x5s-' + datetime.now().strftime("%Y%m%d-%H%M%S") + '/'
os.mkdir(dir)

camera.start_preview(alpha=100)
for i in range(5):
    sleep(5)
    camera.capture(dir + datetime.now().strftime("%Y%m%d-%H%M%S") + '.jpg')
camera.stop_preview()