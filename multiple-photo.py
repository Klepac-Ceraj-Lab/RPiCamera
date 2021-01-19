from picamera import PiCamera
from time import sleep
import os
from datetime import datetime

camera = PiCamera()
camera.rotation = 270

folder = os.mkdir('/home/anika/Desktop/test')

camera.start_preview(alpha=100)
for i in range(5):
    sleep(5)
    camera.capture('/home/anika/Desktop/test/' + datetime.now().strftime("%Y%m%d-%H%M%S") + '.jpg')
camera.stop_preview()