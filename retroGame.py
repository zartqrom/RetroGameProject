#!/usr/bin/env python3
################################################
# Author: Erick Hazel Rocha García
# License: MIT
# Description: Displays games available to run
################################################

from tkinter import *

listGamesExtension = [".apple2", ".gb", ".gbc", ".gba", ".gg", ".lynx", ".nes", ".snes",
                      ".pce", ".lynx", ".md", ".pcfx", ".ngp", ".psx", ".sms", ".pce_fast",
                      ".ssfplay", ".cue"]

dirGames="/home/pi/Documents/Games"

files = os.listdir(dirGames)

gamesToRun=[]

def getGames():
    for element in files:
        for ext in listGamesExtension:
            if element.endswith(ext):
                gamesToRun.append(element)

    print("Lista de juegos: ")
    print(gamesToRun)

class InterfazJuegos:

    def __init__(self):
        #Inicializa la ventana
        self.ventana = Tk()
        self.ventana.geometry('1200x800')
        self.ventana.title("Retro Games")
        
        self.listbox = Listbox(self.ventana)
        self.listbox.pack()

        #Refresca la ventana
        self.ventana.mainloop()

def main():
    interfaz = InterfazJuegos()
    
if __name__ == "__main__":
    main()