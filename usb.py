from time import sleep
from psutil import disk_partitions

while True:
    sleep(1)
    for elem in disk_partitions():
        if 'removable' in elem.opts:
            print("USB encontrada", elem.device)
            print("Pausar emulacion")
            print("Copiar ROMS")
            print("ROMs copiadas")
            print("Remover USB")
        else:
            print("Sin USB conectada")

