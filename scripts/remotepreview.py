from picamera import PiCamera
from time import sleep
import argparse

camera = PiCamera()

# takes command line argument
parser = argparse.ArgumentParser()
parser.add_argument("path")
args = parser.parse_args()

camera.start_preview(alpha=100) # alpha value makes preview slightly see-through so screen is still visible
sleep(5) # previews for 5sec before taking photo
camera.capture(str(args.path)) # takes photo and saves to directory and filename given in command line
camera.stop_preview()