from picamera import PiCamera
from time import sleep
import argparse

camera = PiCamera()

# takes command line argument
parser = argparse.ArgumentParser()
parser.add_argument("dir")
args = parser.parse_args()

camera.start_preview(alpha=100) # alpha value makes preview slightly see-through so screen is still visible
sleep(5) # previews for 5sec before taking photo
camera.capture(str(args.dir) + 'remotepreview.jpg') # takes photo and saves to <destination directory>/remotepreview.jpg
camera.stop_preview()