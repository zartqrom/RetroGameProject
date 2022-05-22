#!/usr/bin/env python3
##########################################################
# Author: Erick Hazel Rocha García
# License: MIT
# Description: Displays games available to run in Mednafen
##########################################################

from dataclasses import replace
import os
from time import sleep
import enquiries
import subprocess

listGamesExtension = [".apple2", ".gb", ".gbc", ".gba", ".gg", ".lynx", ".nes", ".snes",
                      ".pce", ".lynx", ".md", ".pcfx", ".ngp", ".psx", ".sms", ".pce_fast",
                      ".ssfplay", ".cue", ".sfc", ".smc"]

dirGames="/home/pi/Documents/Games"

gamesToRun=[]
 
def getGames():
    files = os.listdir(dirGames)
    print(files,"\n")
    for element in files:
        for ext in listGamesExtension:
            if element.endswith(ext):
                gamesToRun.append(element)

def initGame():
    #Clears the list of games
    gamesToRun.clear()
    getGames()
    os.system("clear")
    choice = enquiries.choose('Choose one: ', gamesToRun)
    game = "\""+choice+"\""
    print(game)
    command = "mednafen "+dirGames+"/"+game+" &"
    print(command)
    sleep(15)
    os.system(command)
    sleep(15)

subprocess.call("python3 usb.py &", shell=True)
initGame()
while True:
    getData = os.system("pgrep -l mednafen")
    if getData!=0:
        initGame()