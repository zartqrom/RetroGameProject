#!/usr/bin/env python3
##########################################################
# Author: Erick Hazel Rocha García
# License: MIT
# Description: Displays games available to run in Mednafen
##########################################################

import os
import threading
import enquiries
from time import sleep
import shutil
from pyudev import Context, Monitor

optionsMenu = ["1.Search game", "2.Show list", "3.Shutdown"]

listGamesExtension = [".apple2", ".gb", ".gbc", ".gba", ".gg", ".lynx", ".nes", ".snes",
                      ".pce", ".lynx", ".md", ".pcfx", ".ngp", ".psx", ".sms", ".pce_fast",
                      ".ssfplay", ".cue", ".sfc", ".smc"]

dirGames="/home/pi/Documents/Games"

gamesToRun=[]

posibleGames=[]

def usbConfig():
    mountDir = "/media"

    context = Context()
    monitor = Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb', device_type='usb_device')
    while True:
        device = None
        while device is None:
            #print("Checando")
            device = monitor.poll(timeout=1)
        if device.action == "add":
            #print("USB added")
            try:
                os.system("pkill -STOP mednafen")
            except:
                print("Mednafen is not running")
            #Waits until the device is mounted
            sleep(3)
            os.system("sudo mount /dev/sda1 "+mountDir)
            with os.scandir(mountDir) as contentUSB:
                for file in contentUSB:
                    if file.is_file():
                        print("Copying \n")
                        completePathGame = mountDir+"/"+file.name
                        print("Game: ", completePathGame)
                        shutil.copy(completePathGame, dirGames)
            os.system("sudo umount "+mountDir)
            try:
                os.system("pkill -CONT mednafen")
            except:
                print("Mednafen is not running")
        elif device.action == "remove":
            print("USB removed")
            break
 
def getGames():
    files = os.listdir(dirGames)
    for element in files:
        for ext in listGamesExtension:
            if element.endswith(ext):
                gamesToRun.append(element)

def initGame(list):
    os.system("clear")
    choice = enquiries.choose('Choose one: ', list)
    game = "\""+choice+"\""
    command = "/usr/games/mednafen "+dirGames+"/"+game+" &"
    os.system(command)

def filterGame(list):
    list.clear()
    #Abra el teclado
    gameName = input("Input the game name: ")
    for elem in gamesToRun:
        elem = str(elem)
        if elem.lower().find(gameName.lower()) >= 0:
            list.append(elem)
    initGame(list)

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
        filterGame(posibleGames)
    elif choice == optionsMenu[1]:
        initGame(gamesToRun)
    else:
        os.system("sudo shutdown now")


thread = threading.Thread(target=usbConfig)

thread.start()
startupWindow()
while True:
    getData = os.system("pgrep -l mednafen")
    if getData!=0:
        startupWindow()