#!/usr/bin/env python3
################################################
# Author: Erick Hazel Rocha García
# License: MIT
# Description: Displays games available to run in Madfen
################################################
import os
import pathlib
from time import sleep
from datetime import datetime
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
        print("Checando")
        device = monitor.poll(timeout=1)
    if device.action == "add":
        print("USB added")
        #Waits until the device is mounted
        sleep(5)
        #Name of the USB as String
        nameUSB = str(os.listdir(mountDir)[0])
        pathUSB = mountDir+"/"+nameUSB
    elif device.action == "remove":
        print("USB removed")

# while True:
#     sleep(1)
#     for elem in disk_partitions():
#         print("DISC: \n", elem)
#         if 'removable' in elem.opts:
#             try:
#                 os.system("pkill -STOP mednafen")
#             except:
#                 print("Mednafen is not running")
#             print("USB encontrada", elem.device)
#             deviceDetected = str(elem.device)
#             contentUSB = pathlib.Path(deviceDetected)
#             for file in contentUSB.iterdir():
#                 if file.is_file():
#                     print("Copying ")
#                     completePathGame = deviceDetected+file
#                     shutil.copy(completePathGame, destination)
#         else:
#             print("Sin USB conectada")

