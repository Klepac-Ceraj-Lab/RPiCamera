from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(60) # previews for 60sec
camera.stop_preview()