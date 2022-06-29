# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 11:07:29 2022

@author: Shoheb
"""

#This section is just for importing twclip which will output dl link through some piggyback url, wget downloads and outputs test1.mp4 in CD. 


#clipData = twyclip.twyclip.clipData('https://clips.twitch.tv/AmazonianApatheticDonutPoooound-v8tFPnok87a53xym')
#response = wget.download(clipData["download_link"], "test1.mp4")

import os
import twyclip
import twitchAPI
from pprint import pprint
from twitchAPI import Twitch
import datetime
import urllib.request
from moviepy.editor import *

# Variables
streamer = 'swagg' # Streamer
game = "509658" # Game
clip = "" # Clip ID
noClips = 3 # Number of Clips
timeClip = 0 # 0 = daily, 1 = weekly

if timeClip == 0:
    timeNow = datetime.datetime.now() # Current Date
    timePrev = timeNow - datetime.timedelta(days=1) # Daily clips for 1 day before
elif timeClip == 1:
    timeNow = datetime.datetime.now() # Current Date
    timePrev = timeNow - datetime.timedelta(days=7) # Daily clips for 1 week before


 # Only has app auth not user auth, can setup userauth with tokens but not sure if needed. Confusing to get the token auth each time. 

twitch = Twitch('ehq9egr235j0mg3wk64gp8domnheiv', 'ca3jppn2uoxctd3cgajmctrv9xtt39')
streamer_info = twitch.get_users(logins=[streamer])
bID = streamer_info['data'][0]['id']
print("Twitch user has been AUTH")

clipDict = twitch.get_clips(broadcaster_id = bID, ended_at = timeNow, started_at = timePrev, first = noClips) # token is pokimane for example with top 5 clips ever made
#clipDict = twitch.get_clips(game_id = game, ended_at = timeNow, started_at = timePrev, first = noClips) # token is pokimane for example with top 5 clips ever made
print("Clip dictionary created")

clipList = []
streamerList = []

currentD = os.getcwd()
os.chdir('Downloads')
for a in range (0, len(clipDict['data'])):
        clipData = twyclip.twyclip.clipData(clipDict['data'][a]['url'])
        urllib.request.urlretrieve(clipData["download_link"], str(a) + ".mp4")
        temp1 = VideoFileClip(str(a) + ".mp4")
        clipList.append(temp1)
        streamerList.append(clipData['author'])
print("Clips downloaded")
#final = concatenate_videoclips(clipList)
#final.write_videofile("compiled.mp4")
os.chdir(currentD)

streamerList = list(dict.fromkeys(streamerList))
streamerOut = open(r"Streamers.txt","w") 
streamerOut.truncate(0)
for a in streamerList:
    streamerOut.write('http://twitch.tv/' + a)
streamerOut.close()

"""
urlOut = open(r"Output.txt","w") 
urlOut.truncate(0)
for a in clipDict['data']: #>>> Just prints out the url for proof of concept, can directly address url for clip download through url
    print(a['url'])
    urlOut.write(a['url'][24:] + '\n')
urlOut.close()
"""


