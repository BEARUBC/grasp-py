#!/usr/bin/python

from GRASP_Manager import GRASP_Manager
from GRASP_Input_TS import GRASP_Input_TS
from GRASP_Input_Voice import GRASP_Input_Voice
import tkinter as tk

def main():
    manager = GRASP_Manager()
    manager.manage()
if __name__ == "__main__":
    main()
