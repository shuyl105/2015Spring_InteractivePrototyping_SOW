from moviepy.editor import *

funny = (VideoFileClip("trailer.mp4")
             .subclip((2,05.30),(2,05.34))
             .resize(0.5))

funny.write_gif("funny.gif")