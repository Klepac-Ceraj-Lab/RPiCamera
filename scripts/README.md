This directory contains scripts to control the HQ Camera with an RPi

## Description and Instructions for Individual Scripts:

**buttonphoto.py**
- takes photo(s) upon button press
- names photo(s) with current timestamp
- saves photo(s) to directory given in command line
1. to run: `$ python <path to RPiCamera>/RPiCamera/scripts/buttonphoto.py <path to dir where photo(s) will go>/`
2. press button to take photo
3. repeat for as many photos as desired
4. to stop: `Ctrl + C` in terminal, then press button

**photo.py**
- takes one photo
- names photo with current timestamp
- saves to directory given in command line
1. to run: `$ python <path to RPiCamera>/RPiCamera/scripts/photo.py <path to dir where photo will go>/`

**preview.py**
- shows camera preview on screen for 60sec to allow for adjustments
1. to run: `$ python <path to RPiCamera>/RPiCamera/scripts/preview.py`

**remotepreview.py**
- takes photo
- names photo with path and filename given in command line
- allows preview to be copied to remote device
1. to run: `$ python <path to RPiCamera>/RPiCamera/scripts/remotepreview.py`
2. to copy to remote device: `rd $ rsync pd:<path to photo> <path to dir where photo will be copied>`
    - remote device = rd
    - device with photo = pd