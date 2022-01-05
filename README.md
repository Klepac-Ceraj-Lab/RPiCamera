# RPiCamera

## Installing RPiCamera
This repository allows you to control and take pictures with a [Raspberry Pi (RPi)](https://www.raspberrypi.org/) connected to a [High Quality (HQ) Camera](https://www.raspberrypi.org/products/raspberry-pi-high-quality-camera/) using `Python`. In order to use this repository, follow the instructions below.

### Installing Python
Follow the installation instructions for your system from the [Python website](https://www.python.org/downloads/). The code in this repository has been tested against Python 2.7.16.

The code in this repository was written in Python through [VS Code](https://code.visualstudio.com/). Instructions on how to download VS Code and install the Python extension can be found [here](https://code.visualstudio.com/docs/python/python-tutorial).

### Cloning this repository
If you have `git` installed, the easiest way to obtain this code is to clone the repository.

```sh
$ git clone https://github.com/Klepac-Ceraj-Lab/RPiCamera.git
Cloning into 'RPiCamera'...
remote: Enumerating objects: 60, done.
remote: Counting objects: 100% (60/60), done.
remote: Compressing objects: 100% (38/38), done.
remote: Total 60 (delta 29), reused 50 (delta 19), pack-reused 0
Unpacking objects: 100% (60/60), done.
```

## Using RPiCamera
All Python scripts can be found in [`scripts/`](scripts). Instructions for how to run scripts can be found in [`scripts/README.md`](scripts/README.md). Scripts should run with no additional modifications.

Instructions for how to set up and create time lapse videos with this repository can also be found under [Creating time lapse videos](scripts/README.md#creating-time-lapse-videos) in `scripts/README.md`

Example photos taken and time lapses made with the code in this repository can be found in the files in [`examples/`](examples).