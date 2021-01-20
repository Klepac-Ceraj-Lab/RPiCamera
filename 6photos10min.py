from picamera import PiCamera
from time import sleep
import os
from datetime import datetime

camera = PiCamera()
camera.rotation = 270

dir = '/home/anika/Desktop/6x10m-' + datetime.now().strftime("%Y%m%d-%H%M%S") + '/'
os.mkdir(dir)

camera.start_preview(alpha=100)
for i in range(6):
    sleep(10*60)
    camera.capture(dir + datetime.now().strftime("%Y%m%d-%H%M%S") + '.jpg')
camera.stop_preview()