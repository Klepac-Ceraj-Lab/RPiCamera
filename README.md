# RPiCamera

**buttonphoto.py**
- takes one photo on button press => saves to given directory
- to maintain consistency give directory in Pictures
- protocol: run file --> push button

**photo.py**
- takes one photo => saves to given directory
    - command: 
- to maintain consistency give directory in Pictures

**preview.py**
- shows camera preview for 60sec to allow for adjustments
- only works if pi is connected to monitor

**remotepreview.py**
takes photo with name "remotepreview.jpg" => saves to Pictures

**video5sec.py**
takes one video that is 5sec long => saves to Pictures

**5photos5sec.py**
takes 5 photos with 5 sec intervals between each photo => saves to directory in Pictures

**filenames** = YYYYMMDD-HHMMSS + {extension}

**directory names** = {numberofphotos}x{timeinterval} + YYYYMMDD-HHMMSS