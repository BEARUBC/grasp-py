from tkinter import *
import tkinter as tk

FONT = ("Verdana", 10)

class GRASP_gui(tk.Tk):
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


    def show_buttons(self):
        height = 25
        width = 25
        padx = 3
        stat_height = 2
        stat_width = 5
        stat_padx = 1
        cup = Button(self.frames[0], text="cup", fg="red", height=height, width=width, padx=padx)
        hammer = Button(self.frames[0], text="hammer", fg="red", height=height, width=width, padx=padx)
        pinch = Button(self.frames[0], text="pinch", fg="red", height=height, width=width, padx=padx)
        flat = Button(self.frames[0], text="flat", fg="red", height=height, width=width, padx=padx)
        ball = Button(self.frames[0], text="ball", fg="red", height=height, width=width, padx=padx)
        fist = Button(self.frames[0], text="fist", fg="red", height=height, width=width, padx=padx)
        rigid = Button(self.frames[0], text="rigid", fg="red", height=height, width=width, padx=padx)
        distance = Button(self.frames[0], text="distance", fg="red", height=height, width=width, padx=padx)

        status = Button(self.frames[1], text="status", fg="red", height=stat_height, width=stat_width, padx=stat_padx)

        cup.grid(column=0, row=0, padx=2, pady=2)
        hammer.grid(column=1, row=0, padx=2, pady=2)
        pinch.grid(column=2, row=0, padx=2, pady=2)
        flat.grid(column=3, row=0, padx=2, pady=2)
        ball.grid(column=0, row=1, padx=2, pady=2)
        fist.grid(column=1, row=1, padx=2, pady=2)
        rigid.grid(column=2, row=1, padx=2, pady=2)
        distance.grid(column=3, row=1, padx=2, pady=2)

        status.grid(column=0,row=0)
        # cup.pack(side=LEFT)
        # hammer.pack(side=LEFT)
        # pinch.pack(side=LEFT)
        # flat.pack(side=LEFT)
        # ball.pack(side=LEFT)
        # fist.pack(side=LEFT)


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
