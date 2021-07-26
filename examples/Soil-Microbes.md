# Soil Microbes (Incomplete)

The HQ Camera was set up above a culture plate with micrboes from soil associated with [*Rhoeo spathacea*](https://en.wikipedia.org/wiki/Tradescantia_spathacea) and the RPi took photos from 07/20/21 13:45 to 07/26/21 16:00.

A newly constructed RPi Camera Box was used to take this set of photos.

A [cron job](https://en.wikipedia.org/wiki/Cron) was written to capture photos every 15min, at 00, 15, 30, and 45 of every hour: `0,15,30,45 * * * * python ~/Desktop/RPiCamera/scripts/photo.py ~/Pictures/2021Summer-FirstTimeLapseWithBox/`

A time lapse video was made using [QuickTime Player](https://en.wikipedia.org/wiki/QuickTime).

Figure 1: A time lapse video of all photos taken, at 24 frames per second, made using QuickTime Player Version 10.5 (1086.4.2).

Figure 2: A composite figure of 6 photos taken at 19:00 every day. Numbers in the top right corner indicate which number of days after plating that the photos were taken.