# RPiCamera

**buttonphoto.py**
- takes photo upon button press => saves all photos to given directory
    - command: `~/Desktop/RPiCamera $ python buttonphoto.py <path to dir/>`
- protocol: run file --> button press to take photo --> repeat
- to stop: `Ctrl + C` in terminal --> button press to close

**photo.py**
- takes one photo => saves to given directory
    - command: `~/Desktop/RPiCamera $ python photo.py <path to dir/>`

**preview.py**
- shows camera preview for 60sec to allow for adjustments
- only works if pi is connected to monitor

**remotepreview.py**
takes photo with name "remotepreview.jpg" => saves to Pictures