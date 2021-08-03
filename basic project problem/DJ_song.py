# import-ant  libeary
import os
from random import choice
import vlc
from time import sleep

# Demo
# change path to file location

#os.chdir('/media/alimam/5A3C6EF93C6ED015/Users/family/Music/music')
os.chdir('/media/alimam/5A3C6EF93C6ED015/Users/ASGAR HUSSAIN/Downloads/Music/')

# files in list in list
files=os.listdir()
only_media=[file for file in files if file.endswith(('.mp3','.mp4','.mkv'))]
print(len(only_media),'\n')
# loop
for i in range(len(only_media)):
    file =(choice(only_media))    # choice
    im=vlc.MediaPlayer(file)      # music object create
    im.play()                     # play
    im.set_time(50000)            # set specific time
    
    only_media.remove(file)       # remove played music
    sleep(choice([20,10,30,25,15,19,13]))                     # play music for 10 sec
    im.set_pause(1)               # pause music


