from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()

camera.start_preview(alpha=100) # alpha value makes preview slightly see-through so screen is still visible
camera.start_recording('/home/anika/Desktop/' + datetime.now().strftime("%Y%m%d-%H%M%S") + '.h264')
sleep(5) # takes video for 5s
camera.stop_recording()
camera.stop_preview()