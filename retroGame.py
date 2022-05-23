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

optionsMenu = ["1.Search game", "2.Show list"]

listGamesExtension = [".apple2", ".gb", ".gbc", ".gba", ".gg", ".lynx", ".nes", ".snes",
                      ".pce", ".lynx", ".md", ".pcfx", ".ngp", ".psx", ".sms", ".pce_fast",
                      ".ssfplay", ".cue", ".sfc", ".smc"]

dirGames="/home/pi/Documents/Games"

gamesToRun=[]

posibleGames=[]
 
def getGames():
    files = os.listdir(dirGames)
    print(files,"\n")
    for element in files:
        for ext in listGamesExtension:
            if element.endswith(ext):
                gamesToRun.append(element)

def initGame():
    os.system("clear")
    choice = enquiries.choose('Choose one: ', gamesToRun)
    game = "\""+choice+"\""
    command = "mednafen "+dirGames+"/"+game+" &"
    os.system(command)

def startupWindow():
    os.system("clear")
    print("****************************")
    print("*     Arcade Emulator      *")
    print("*   Powered by Mednafen    *")
    print("****************************")
    #Clears the list of games
    gamesToRun.clear()
    getGames()
    choice = enquiries.choose('Choose one: ', optionsMenu)
    if choice == optionsMenu[0]:
        posibleGames.clear()
        #Abra el teclado
        gameName = input("Input the game name: ")
        for elem in gamesToRun:
            elem = str(elem)
            if elem.lower() == gameName.lower():
                posibleGames.append()
        command = "mednafen "+dirGames+"/"+game+" &"
        os.system(command)
    else:
        initGame()

subprocess.call("python3 usb.py &", shell=True)

startupWindow()
while True:
    getData = os.system("pgrep -l mednafen")
    if getData!=0:
        startupWindow()