from tkinter import *
import os

listGamesExtension = [".apple2", ".gb", ".gbc", ".gba", ".gg", ".lynx", ".nes", ".snes",
                      ".pce", ".lynx", ".md", ".pcfx", ".ngp", ".psx", ".sms", ".pce_fast",
                      ".ssfplay", ".cue", ".sfc", ".smc"]

dirGames="/home/pi/Documents/Games"

files = os.listdir(dirGames)

gamesToRun=[]

def initInterface(window):
    #Configure the window
    window.geometry('800x800')
    window.title("Retro Games")
    
    #Creates the widget for the list and configures the element selected
    # with green background
    listbox = Listbox(window, selectbackground="#00aa00")
    #Adds the games found it
    listbox.insert(0, *gamesToRun)
    #Selects the first element by default
    listbox.selection_set(0)
    listbox.pack()

#Startup window
window = Tk()
initInterface(window)
#Refresh window
window.mainloop()
