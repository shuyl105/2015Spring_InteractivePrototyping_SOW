Python & MoviePy
--------------
Based on [this turtorial](http://zulko.github.io/blog/2014/01/23/making-animated-gifs-from-video-files-with-python/), which you can make GIFs from video with Python by yourself.

### 1. Install [Youtube-dl](http://rg3.github.io/youtube-dl/)

Or OS X users can install youtube-dl with Homebrew.
$ brew install youtube-dl

Or
$ sudo pip install youtube-dl

Here is the [documentation](https://github.com/rg3/youtube-dl/blob/master/README.md#readme)

### 2.Install [MoviePy](http://zulko.github.io/moviepy/)

$ sudo pip install moviepy
$ sudo pip install ez_setup

### 3. Download the sourceson [Github](https://github.com/Zulko/moviepy), unzip everything in one folder, open a terminal and type
$ sudo python setup.py install

### 4.In the same folder, install openCV and Pillow
$ git clone git://code.opencv.org/opencv.git
$ sudo pip install Pillow

### 5. We are ready to go now. Find a video you want to use on Youtube. For this time, I used [Minions - Official Trailer 2](https://www.youtube.com/watch?v=XgYhvSfXlt4)
[id]: 2015Spring_InteractivePrototyping_assignment/week4/MoviePy/ScreenShot_Youtube.png "screenShot_youtube"

$ youtube-dl 2Jw-XgYhvSfXlt4 -o trailer.mp4

### 6.Create a gif.py file and type

from moviepy.editor import *

funny = (VideoFileClip("trailer.mp4")
             .subclip((2,05.30),(2,05.34))
             .resize(0.5))

funny.write_gif("funny.gif")
