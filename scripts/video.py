from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()

# takes command line argument
parser = argparse.ArgumentParser()
parser.add_argument("dir")
args = parser.parse_args()

camera.start_preview(alpha=100) # alpha value makes preview slightly see-through so screen is still visible
camera.start_recording(str(args.dir) + datetime.now().strftime("%Y%m%d-%H%M%S") + '.h264') # takes video and saves to (directory given in command line)/timestamp.h264
sleep(5) # takes video for 5s
camera.stop_recording()
camera.stop_preview()