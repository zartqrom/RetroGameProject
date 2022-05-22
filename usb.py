#!/usr/bin/env python3
################################################
# Author: Erick Hazel Rocha García
# License: MIT
# Description: Displays games available to run in Madfen
################################################
import os
from time import sleep
import shutil
from pyudev import Context, Monitor

mountDir = "/media/pi"
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
        sleep(5)
        #Name of the USB as String
        nameUSB = str(os.listdir(mountDir)[0])
        pathUSB = mountDir+"/"+nameUSB
        with os.scandir(pathUSB) as contentUSB:
            for file in contentUSB:
                if file.is_file():
                    print("Copying \n")
                    completePathGame = pathUSB+"/"+file.name
                    shutil.copy(completePathGame, destPathGames)
        #print("Completed")
        os.system("umount "+pathUSB)
        try:
            os.system("pkill -CONT mednafen")
        except:
            print("Mednafen is not running")
    elif device.action == "remove":
        print("USB removed")

