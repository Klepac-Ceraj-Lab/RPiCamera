from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview(alpha=100)
sleep(5)
camera.capture('/home/anika/Pictures/remotepreview.jpg')
camera.stop_preview()