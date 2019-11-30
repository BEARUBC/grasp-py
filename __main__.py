#!/usr/bin/python

from GRASP_Manager import GRASP_Manager
import GRASP_Input_TS
import GRASP_Input_Voice
import GRASP_gui as gui
import tkinter as tk



#MAIN:------------------------------------------------------------------------------------------------------------------
def main():
    manager = GRASP_Manager()
    manager.manage()
    app = gui()
    app.mainloop()



if __name__ == "__main__":
    main()
