# Initial Test

The HQ Camera was set up in front of a succulent and the RPi took photos in natural lighting from 1/29/21 00:00 to 1/31/21 00:00.

A [cron job](https://en.wikipedia.org/wiki/Cron) was written to capture photos every 30min, at 00 and 30 of every hour:

`0,30 * * * * python ~/Desktop/RPiCamera/scripts/photo.py ~/Pictures/TimeLapseTest/every-thirty/`

A time lapse video was made using [QuickTime Player](https://en.wikipedia.org/wiki/QuickTime).

<img width="758" alt="Initial-Test" src="https://user-images.githubusercontent.com/66045478/125981401-34af4993-21b3-4744-93b7-e32eae66863a.png">

Figure 1: A composite figure of 12 photos taken on the hour on 1/29/21. Numbers in the top right corner indicate which hours the photos were taken.

**https://youtu.be/h0pAcIlQed8**

Figure 2: A time lapse video of all photos taken, at 24 frames per second, made using QuickTime Player Version 10.5 (1086.4.2).
