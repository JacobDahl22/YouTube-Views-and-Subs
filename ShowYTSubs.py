#!/usr/bin/env python3
#---------------------------------------------------
#AUTHOR: jacobdahl09@gmail.com
#DATE CREATED: May 18, 2021 11:03pm
#DESCRIPTION: A simple code that uses the YouTube API in order to show the current subscriber count of whatever YouTube channel is put into the script
#---------------------------------------------------

#Necessary imports
import json
import urllib.request
from win10toast import ToastNotifier

channelID = "YOUR CHANNEL ID GOES HERE" #The channel ID of whatever channel you want to see the subscriber count of

APIkey = "YOUR API KEY GOES HERE" #Your API keyfrom Google's API service

openSite = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+channelID+"&key="+APIkey).read()

channelSubs = json.loads(openSite)["items"][0]["statistics"]["subscriberCount"] #Finds the subscriber count of the channel
channelViews = json.loads(openSite)["items"][0]["statistics"]["viewCount"] #Finds the view count of the channel

toasterNotif = ToastNotifier() #Creates a popup on your computer

message = ("You have %d" %int(channelSubs) +" subscribers and %d" %int(channelViews) + " views.") #What the ToastNotifier is displaying

toasterNotif.show_toast("NAME OF POPUP", message) #The popup name followed by the message containing the number of subscribers
