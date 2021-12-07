This directory contains scripts to control the HQ Camera with an RPi

## Using the Command Line Interface
All scripts are run using the command line interface.

Command prompts will look something like this: `anika@raspberrypi:~ $`. In the Instructions below, everything after `$` is the command to be typed.

Bracketed sections of paths (eg. `<path to RPiCamera>`, `<path to dir where photo will go>`) indicate places where the path differs. Replace everything within and including the brackets with the actual path (eg. `<path to RPiCamera>/RPiCamera/scripts/photo.py` --> `~/Desktop/RPiCamera/scripts/photo.py`)


## Description and Instructions for Individual Scripts

### buttonphoto.py

Description:

- takes photo(s) upon button press
- names photo(s) with current timestamp
- saves photo(s) to directory given in command line

Instructions:

To run:
1. execute `$ python <path to RPiCamera>/RPiCamera/scripts/buttonphoto.py <path to dir where photo(s) will go>/`
2. press button to take photo
3. repeat for as many photos as desired

To stop:
1. press `Ctrl + C`
2. press button

### photo.py

Description:

- takes one photo
- names photo with current timestamp
- saves to directory given in command line

Instructions

1. execute `$ python <path to RPiCamera>/RPiCamera/scripts/photo.py <path to dir where photo will go>/`

### preview.py

Description:

- shows camera preview on screen for 60sec to allow for camera adjustments

Instructions:

1. execute `$ python <path to RPiCamera>/RPiCamera/scripts/preview.py`

### remotepreview.py

Description:

- takes photo
- names photo with path and filename given in command line
- allows preview to be copied to remote device

Instructions:

To run:
1. execute `$ python <path to RPiCamera>/RPiCamera/scripts/remotepreview.py <path to dir where photo will go>/remotepreview.jpg`

To copy to remote device:
1. execute `rd $ rsync pd:<path to photo on pd> <path to dir on rd where photo will be copied>`
    - remote device = rd
    - device with photo = pd

## Time Lapse Instructions
1. Use a [cron job](https://en.wikipedia.org/wiki/Cron) to take photos at predetermined intervals of time
    - see files in `examples/` for example cron jobs
2. Make a time lapse using [QuickTime Player](https://en.wikipedia.org/wiki/QuickTime).
    - Open QuickTime Player
    - Go to "File" -> "Open Image Sequence" (Command+Shift+O)
    - Select images to include in time lapse --> click "Choose media"
    - Select feautures (24 frames per second is standard) --> click "Open"
