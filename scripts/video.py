from picamera import PiCamera
from time import sleep
from datetime import datetime
import argparse

camera = PiCamera()

# takes command line argument
parser = argparse.ArgumentParser()
parser.add_argument("dir") # first argument = destination directory
parser.add_argument("time") # second argument = video time (in seconds)
args = parser.parse_args()

camera.start_preview(alpha=100) # alpha value makes preview slightly see-through so screen is still visible
camera.start_recording(str(args.dir) + datetime.now().strftime("%Y%m%d-%H%M%S") + '.h264') # starts video and saves to <directory given in command line>/timestamp.h264
sleep(float(args.time)) # takes video for <video time>
camera.stop_recording()
camera.stop_preview()