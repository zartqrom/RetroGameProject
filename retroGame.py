#!/usr/bin/env python3
################################################
# Author: Erick Hazel Rocha García
# License: MIT
# Description: Displays games available to run
################################################

from tkinter import *
import os

listGamesExtension = [".apple2", ".gb", ".gbc", ".gba", ".gg", ".lynx", ".nes", ".snes",
                      ".pce", ".lynx", ".md", ".pcfx", ".ngp", ".psx", ".sms", ".pce_fast",
                      ".ssfplay", ".cue", ".sfc", ".smc"]

dirGames="/home/pi/Documents/Games"

files = os.listdir(dirGames)

gamesToRun=[]

def getGames():
    #print(files)
    for element in files:
        for ext in listGamesExtension:
            if element.endswith(ext):
                gamesToRun.append(element)

    #print("Lista de juegos: ")
    #print(gamesToRun)

class InterfazJuegos:

    def __init__(self):
        #Inicializa la ventana
        self.ventana = Tk()
        self.ventana.geometry('1200x800')
        self.ventana.title("Retro Games")
        
        #Creates the widget for the list
        self.listbox = Listbox(self.ventana)
        #Add the games found it
        self.listbox.insert(0, *gamesToRun)
        self.listbox.pack()

        #Refresca la ventana
        self.ventana.mainloop()

def main():
    getGames()
    interfaz = InterfazJuegos()
    
if __name__ == "__main__":
    main()