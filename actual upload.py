# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 11:43:14 2022

@author: Shoheb
"""
from inside.upload import upload_video

video_data = {
            "file": "compiled.mp4",
            "title": f"Test1",
            "description": "Testing this out",
            "keywords": "meme,reddit,Dankestmemes",
            "privacyStatus":"private"
   }
upload_video(video_data)