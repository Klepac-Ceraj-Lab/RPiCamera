from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview(alpha=100) # alpha value makes preview slightly see-through so screen is still visible
sleep(5) # previews for 5sec before taking photo
camera.capture('/home/anika/Pictures/remotepreview.jpg') # takes photo and saves to given path
camera.stop_preview()