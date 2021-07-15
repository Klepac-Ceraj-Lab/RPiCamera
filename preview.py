from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview(alpha=100) # alpha value makes preview slightly see-through so screen is still visible
sleep(60) # previews for 60sec
camera.stop_preview()