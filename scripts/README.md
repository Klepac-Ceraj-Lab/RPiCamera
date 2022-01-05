This directory contains scripts to control the HQ Camera with an RPi

## Using the command-line interface
All scripts are run using the [command-line interface](https://en.wikipedia.org/wiki/Command-line_interface).

For a brief guide to using the command-line interface to navigate the filesystem, refer to [BISC 195 Lesson 1 Part 2](http://bisc195.wellesley.edu/lessons/Lesson01/#part_2_-_navigating_the_filesystem_using_the_terminal)

Command prompts will look something like this: `anika@raspberrypi:~ $`. In the Instructions below, everything after `$` is the command to be typed.

Most scripts also use command line arguments (parsed using `argparse`). See [Python Command Line Arguments](https://www.askpython.com/python/python-command-line-arguments) for a brief description.

Bracketed sections of paths (eg. `<path to RPiCamera>`, `<path to destination directory>`) indicate places where the path differs. Replace everything within and including the brackets with the actual path (e.g., `<path to RPiCamera>` --> `~/Desktop` if RPiCamera is in Desktop).

**Note**: In the Examples below, the RPiCamera directory is in Desktop and all photos and videos are sent to Desktop/example.

## Descriptions and instructions for individual scripts

### [buttonphoto.py](buttonphoto.py)

DESCRIPTION:

- takes photo(s) upon button press
- names photo(s) with current timestamp (yyyymmdd-hhmmss)
- saves photo(s) to directory given in command line

INSTRUCTIONS:

To run:
1. execute `$ python <path to RPiCamera>/RPiCamera/scripts/buttonphoto.py <path to destination directory>/`
    - path to destination directory must include '`/`' to insure that file goes inside the given dir
2. press button to take photo
3. wait at least one second to ensure script is ready to take another photo
4. repeat for as many photos as desired

To stop:
1. press `Ctrl + C` to execute a KeyboardInterrupt in terminal
2. press button

EXAMPLE:

Command: `anika@raspberrypi:~ $ python ~/Desktop/RPiCamera/scripts/buttonphoto.py ~/Desktop/example/`

Filename(s): `~/Desktop/example/20220104-173010.jpg`, `~/Desktop/example/20220104-173020.jpg`, etc.

### [photo.py](photo.py)

DESCRIPTION:

- takes one photo
- names photo with current timestamp (yyyymmdd-hhmmss)
- saves to directory given in command line
- *this script can be used in conjuntion with a cron job to create time lapse videos - see [Creating time lapse videos from photos](#time-lapse) below for more details*

INSTRUCTIONS:

1. execute `$ python <path to RPiCamera>/RPiCamera/scripts/photo.py <path to destination directory>/`
    - path to destination directory must include '`/`' to insure that file goes inside the given dir

EXAMPLE:

Command: `anika@raspberrypi:~ $ python ~/Desktop/RPiCamera/scripts/photo.py ~/Desktop/example/`

Filename: `~/Desktop/example/20220104-173128.jpg`

### [preview.py](preview.py)

DESCRIPTION:

- shows camera preview on screen for 60sec to allow for camera adjustments

INSTRUCTIONS:

1. execute `$ python <path to RPiCamera>/RPiCamera/scripts/preview.py`
2. adjust camera settings as needed - refer to the [VKC RPi Manual](https://github.com/Klepac-Ceraj-Lab/klepac-ceraj-lab.github.io/blob/main/drylab/rpi-manual.md) for more detailed instructions

EXAMPLE:

Command: `anika@raspberrypi:~ $ python ~/Desktop/RPiCamera/scripts/preview.py`

### [remotepreview.py](remotepreview.py)

DESCRIPTION:

- takes photo
- names photo with `remotepreview.jpg`
- saves to directory given in command line

INSTRUCTIONS:

To run:
1. execute `$ python <path to RPiCamera>/RPiCamera/scripts/remotepreview.py <path to destination directory>/`
    - path to destination directory must include '`/`' to insure that file goes inside the given dir

To copy to remote device:
1. execute `rd $ rsync pd:<path to photo on pd> <path to destination directory on rd>/`
    - remote device = rd
    - device with photo = pd
2. or execute `pd $ rsync <path to photo on pd> rd:<path to destination directory on rd>/`

EXAMPLE:

Command to take photo: `anika@raspberrypi:~ $ python ~/Desktop/RPiCamera/scripts/remotepreview.py ~/Desktop/example/`

Filename: `~/Desktop/example/remotepreview.jpg`

Command to copy to remote device: `anika:~ $ rsync doudna:~/Desktop/example/remotepreview.jpg ~/Desktop/`
- remote device = `anika`
- device with photo = `doudna`
- destination directory of photo = `~/Desktop`

### [video.py](video.py)

DESCRIPTION:

- takes one video of time length (in seconds) given in command line
- names photo with current timestamp (yyyymmdd-hhmmss)
- saves to directory given in command line

INSTRUCTIONS:

1. execute `$ python <path to RPiCamera>/RPiCamera/scripts/video.py <path to destination directory>/`
    - path to destination directory must include '`/`' to insure that file goes inside the given dir

EXAMPLE:

Command: `anika@raspberrypi:~ $ python ~/Desktop/RPiCamera/scripts/video.py ~/Desktop/example/ 30`

Filename: `~/Desktop/example/20220104-174953.h264`

## Creating time lapse videos from photos {time-lapse}
1. Use a [cron job](https://en.wikipedia.org/wiki/Cron) to take photos at predetermined intervals of time
    - see files in `RPiCamera/examples/` for example cron jobs
2. Make a time lapse using [QuickTime Player](https://en.wikipedia.org/wiki/QuickTime).
    - For MacOS 11.6 running QuickTime Player 10.5
        - Open QuickTime Player
        - Go to "File" -> "Open Image Sequence" (Command+Shift+O)
        - Select images to include in time lapse --> click "Choose media"
        - Select feautures (24 frames per second is standard) --> click "Open"