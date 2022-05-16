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

class GameInterface:

    def __init__(self):
        #Startup window
        self.window = Tk()
        self.window.geometry('1200x800')
        self.window.title("Retro Games")
        
        #Creates the widget for the list and configures the element selected
        # with green background
        self.listbox = Listbox(self.window, selectbackground="#00aa00")
        #Adds the games found it
        self.listbox.insert(0, *gamesToRun)
        #Selects the first element by default
        self.listbox.selection_set(0)
        self.listbox.pack()

        #Refresh window
        self.window.mainloop()

def main():
    getGames()
    interface = GameInterface()
    
if __name__ == "__main__":
    main()