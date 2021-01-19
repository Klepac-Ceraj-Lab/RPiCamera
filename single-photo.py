from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()
camera.rotation = 270

camera.start_preview(alpha=100)
sleep(5)
camera.capture('/home/anika/Desktop/' + datetime.now().strftime("%Y%m%d-%H%M%S") + '.jpg')
camera.stop_preview()