from picamera import PiCamera
from time import sleep
from datetime import datetime
import argparse
from gpiozero import Button

button = Button(17)
camera = PiCamera()

parser = argparse.ArgumentParser()
parser.add_argument("dir")
args = parser.parse_args()

camera.start_preview(alpha=100)
button.wait_for_press()
camera.capture(str(args.dir) + datetime.now().strftime("%Y%m%d-%H%M%S") + '.jpg')
camera.stop_preview()