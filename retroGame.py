#!/usr/bin/env python3
################################################
# Author: Erick Hazel Rocha García
# License: MIT
# Description: Displays games available to run in Madfen
################################################

import os
import enquiries

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

    print("Lista de juegos: ")
    print(gamesToRun)

getGames()
choice = enquiries.choose('Choose one: ', gamesToRun)
print("Game to run: ", choice)
command = "mednafen "+dirGames+"/"+choice
os.system(command)