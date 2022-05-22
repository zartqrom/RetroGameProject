#!/usr/bin/env python3
################################################
# Author: Erick Hazel Rocha García
# License: MIT
# Description: Displays games available to run in Madfen
################################################

import os
import enquiries
import subprocess

listGamesExtension = [".apple2", ".gb", ".gbc", ".gba", ".gg", ".lynx", ".nes", ".snes",
                      ".pce", ".lynx", ".md", ".pcfx", ".ngp", ".psx", ".sms", ".pce_fast",
                      ".ssfplay", ".cue", ".sfc", ".smc"]

dirGames="/home/pi/Documents/Games"

files = os.listdir(dirGames)

gamesToRun=[]

def getGames():
    print(files,"\n")
    for element in files:
        for ext in listGamesExtension:
            if element.endswith(ext):
                gamesToRun.append(element)

def initGame():
    #Clears the list of games
    gamesToRun.clear()
    getGames()
    choice = enquiries.choose('Choose one: ', gamesToRun)
    command = "mednafen "+dirGames+"/"+choice+" &"
    os.system(command)    

subprocess.call("python3 usb.py &", shell=True)
initGame()
while True:
    getData = os.system("pgrep -l mednafen")
    if getData!=0:
        initGame()