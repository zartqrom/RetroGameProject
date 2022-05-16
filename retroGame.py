#!/usr/bin/env python3
################################################
# Author: Erick Hazel Rocha García
# License: MIT
# Description: Displays games available to run
################################################

from tkinter import *

class InterfazJuegos:

    def __init__(self,):
        #Inicializa la ventana
        self.ventana = Tk()
        self.ventana.geometry('1200x800')
        self.ventana.title("Retro Games")

        #Refresca la ventana
        self.ventana.mainloop()

def main():
    interfaz = InterfazJuegos()
    
if __name__ == "__main__":
    main()