This directory contains scripts to control the HQ Camera with an RPi

## Description and Instructions for Individual Scripts:

**buttonphoto.py**
- takes photo upon button press => saves all photos to directory given in command line
1. to run: `$ python <path to RPiCamera>/RPiCamera/scripts/buttonphoto.py <path to dir where photos will go>/`
2. press button to take photo
3. repeat for as many photos as desired
4. to stop: `Ctrl + C` in terminal, then press button

**photo.py**
- takes one photo => saves to directory given in command line
1. to run: `$ python <path to RPiCamera>/RPiCamera/scripts/photo.py <path to dir where photo will go>/`

**preview.py**
- shows camera preview on screen for 60sec to allow for adjustments
1. to run: `$ python <path to RPiCamera>/RPiCamera/scripts/preview.py`

**remotepreview.py**
- takes photo with name "remotepreview.jpg" => saves to Pictures
- allows preview to be copied to remote device
1. to run: `$ python <path to RPiCamera>/RPiCamera/scripts/remotepreview.py`