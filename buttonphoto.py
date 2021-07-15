from picamera import PiCamera
from time import sleep
from datetime import datetime
import argparse
from gpiozero import Button

button = Button(17)
camera = PiCamera()

# takes command line argument
parser = argparse.ArgumentParser()
parser.add_argument("dir")
args = parser.parse_args()

camera.start_preview(alpha=100) # alpha value makes preview slightly see-through so screen is still visible
frame = 1
while True:
    try:
        button.wait_for_press()
        camera.capture(str(args.dir) + datetime.now().strftime("%Y%m%d-%H%M%S") + '.jpg') # after button press, takes photo and saves to (directory given in command line)/timestamp.jpg
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break