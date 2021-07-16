# Initial Test

The HQ Camera was set up in front of a succulent and took photos in natural lighting for 3 full days from 1/29/21 to 1/31/21.

A [cron job](https://en.wikipedia.org/wiki/Cron) was written to capture photos every thirty minutes, at 00 and 30 of every hour: `0,30 * * * * python ~/Desktop/RPiCamera/photo.py ~/Pictures/TimeLapseTest/every-thirty/`

<img width="758" alt="Initial-Test" src="https://user-images.githubusercontent.com/66045478/125981401-34af4993-21b3-4744-93b7-e32eae66863a.png">

Figure 1: A composite figure of 12 photos taken on the hour on 1/29/21. Numbers in the top right corner indicate which hours the photos were taken.

Figure 2: A time lapse video of all photos taken during the 3 days at 24 frames per second, made using QuickTime Player Version 10.5 (1086.4.2).

To make a time lapse video using [QuickTime Player](https://en.wikipedia.org/wiki/QuickTime):
- Open QuickTime Player
- Go to File -> Open Image Sequence (Command+Shift+O)
- Select images to include in time lapse
- Select feautures (24 frames per second is standard)
