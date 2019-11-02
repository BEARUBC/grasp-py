from tkinter import *
import tkinter as tk

FONT = ("Verdana", 10)

class GRASP_gui(tk.Tk):
    def __init__(self, *args, **kwargs):
        parent = tk.Tk.__init__(self, *args, **kwargs)
        self.frames = []

        root = tk.Frame(parent)
        root.pack()

        actv_frame = tk.Frame(root,highlightbackground="black",highlightthickness=1)
        self.frames.append(actv_frame)
        actv_frame.pack(side=RIGHT)

        stat_frame = tk.Frame(root,highlightbackground="black",highlightthickness=1)
        self.frames.append(stat_frame)
        stat_frame.pack(side=TOP)

        ascr_frame = tk.Frame(root,highlightbackground="black",highlightthickness=1)
        self.frames.append(ascr_frame)
        ascr_frame.pack(side=LEFT)

        self.show_buttons()
        root.tkraise()


    def show_buttons(self):
        height = 10
        width = 20
        hand_1 = Button(self.frames[0], text="hand_1", fg="red", height=height, width=width)
        hand_2 = Button(self.frames[0], text="hand_2", fg="red", height=height, width=width)
        hand_3 = Button(self.frames[0], text="hand_3", fg="red", height=height, width=width)
        hand_4 = Button(self.frames[0], text="hand_4", fg="red", height=height, width=width)
        hand_5 = Button(self.frames[0], text="hand_5", fg="red", height=height, width=width)
        hand_6 = Button(self.frames[0], text="hand_6", fg="red", height=height, width=width)
        hand_1.pack(side=LEFT)
        hand_2.pack(side=LEFT)
        hand_3.pack(side=LEFT)
        hand_4.pack(side=LEFT)
        hand_5.pack(side=LEFT)
        hand_6.pack(side=LEFT)


        # self.frames = {}
        #
        # container = tk.Frame(self)
        # frame = StartPage(container, self)
        # self.frames[0] = frame
        #
        #
        # frame.tkraise()



        # container = tk.Frame(self)

        # container.pack(side="top", fill="both", expand=True)
        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)

        # self.frames = {}
        #
        # frame = StartPage(container, self)
        #
        # self.frames[StartPage] = frame
        #
        # frame.grid(row=0, column=0, sticky="nsew")
        #
        # self.show_frame(StartPage)

    # def show_frame(self, cont):
    #
    #     frame = self.frames[cont]
    #     frame.tkraise()

# class StartPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Start Page", font=FONT)
#         label.pack(pady=10,padx=10)

# app = tk.Tk()
# app.mainloop()

app = GRASP_gui()
app.mainloop()
