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

nameUSB = os.listdir("/media/pi")

context = Context()
monitor = Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb', device_type='usb_device')

while True:
    device = None
    while device is None:
        print("Checando")
        device = monitor.poll(timeout=3)
    if device.action == "add":
        print("USB added")
        print("\nUSB conected ->", nameUSB)
    elif device.action == "remove" or device.action == "offline":
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

