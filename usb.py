#!/usr/bin/env python3
###########################################################
# Author: Erick Hazel Rocha García
# License: MIT
# Description: Displays games available to run in Mednafen
###########################################################
import os
from time import sleep
import shutil
from pyudev import Context, Monitor

mountDir = "/media"
destPathGames = "/home/pi/Documents/Games"

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
                    shutil.copy(completePathGame, destPathGames)
        #print("Completed")
        os.system("sudo umount "+mountDir)
        try:
            os.system("pkill -CONT mednafen")
        except:
            print("Mednafen is not running")
    elif device.action == "remove":
        print("USB removed")
        break
