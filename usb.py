#!/usr/bin/env python3
################################################
# Author: Erick Hazel Rocha García
# License: MIT
# Description: Displays games available to run in Madfen
################################################
import pathlib
from time import sleep
import shutil
from psutil import disk_partitions

destination = ""

while True:
    sleep(1)
    for elem in disk_partitions():
        if 'removable' in elem.opts:
            print("USB encontrada", elem.device)
            deviceDetected = str(elem.device)
            contentUSB = pathlib.Path(deviceDetected)
            for file in contentUSB.iterdir():
                if file.is_file():
                    completePathGame = deviceDetected+file
                    shutil.copy(completePathGame, destination)
            
            print("Pausar emulacion")
            print("Copiar ROMS")
            print("ROMs copiadas")
            print("Remover USB")
        else:
            print("Sin USB conectada")

