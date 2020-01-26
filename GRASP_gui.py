from tkinter import *
import tkinter as tk

FONT = ("Verdana", 10)

class GRASP_gui(tk.Tk):
    def btn1(self):
        print("Hello world!")
    
    def btn2(self):
        print("Hello world!")
    
    def btn3(self):
        print("Hello world!")
    
    def btn4(self):
        print("Hello world!")
    
    def btn5(self):
        print("Hello world!")
    
    def btn6(self):
        print("Hello world!")

    def __init__(self, *args, **kwargs):
        parent = tk.Tk.__init__(self, *args, **kwargs)
        self.frames = []

        root = tk.Frame(parent)
        root.pack()

        actv_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1)
        self.frames.append(actv_frame)
        actv_frame.grid(column=1, row=0, rowspan=20, sticky="nsew")

        stat_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1)
        self.frames.append(stat_frame)
        stat_frame.grid(column=0, row=0, rowspan=1, sticky="nsew")

        ascr_frame = tk.Frame(root, highlightbackground="black", highlightthickness=1)
        self.frames.append(ascr_frame)
        ascr_frame.grid(column=0, row=1, rowspan=19, sticky="nsew")

        self.show_buttons()
        root.tkraise()

    def shutdown(self):
        pass
    
    def show_buttons(self):
        height = 5
        width = 5
        padx = 3
        stat_height = 2
        stat_width = 5
        stat_padx = 1
        hand_1 = Button(self.frames[0], text="hand_1", fg="red", height=height, width=width, padx=padx, command=self.btn1)
        hand_2 = Button(self.frames[0], text="hand_2", fg="red", height=height, width=width, padx=padx, command=self.btn2)
        hand_3 = Button(self.frames[0], text="hand_3", fg="red", height=height, width=width, padx=padx, command=self.btn3)
        hand_4 = Button(self.frames[0], text="hand_4", fg="red", height=height, width=width, padx=padx, command=self.btn4)
        hand_5 = Button(self.frames[0], text="hand_5", fg="red", height=height, width=width, padx=padx, command=self.btn5)
        hand_6 = Button(self.frames[0], text="hand_6", fg="red", height=height, width=width, padx=padx, command=self.btn6)

        status = Button(self.frames[1], text="status", fg="red", height=stat_height, width=stat_width, padx=stat_padx)

        hand_1.grid(column=0, row=0, padx=2, pady=2)
        hand_2.grid(column=1, row=0, padx=2, pady=2)
        hand_3.grid(column=2, row=0, padx=2, pady=2)
        hand_4.grid(column=0, row=1, padx=2, pady=2)
        hand_5.grid(column=1, row=1, padx=2, pady=2)
        hand_6.grid(column=2, row=1, padx=2, pady=2)

        status.grid(column=0,row=0)
        # hand_1.pack(side=LEFT)
        # hand_2.pack(side=LEFT)
        # hand_3.pack(side=LEFT)
        # hand_4.pack(side=LEFT)
        # hand_5.pack(side=LEFT)
        # hand_6.pack(side=LEFT)


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
