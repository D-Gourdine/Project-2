import tkinter as tk
from tkinter import ttk

# MATTPLOTLIB USED FOR GRAPHS
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


LARGE_FONT = ("Stencil", 16)


class math(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Some random title")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)  # sets size and priority(weight)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # streches to size of window

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()  # raise the frame to the front (so that it is visible)


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Menu", font=LARGE_FONT)
        label.grid(pady=10, padx=10)

        button1 = ttk.Button(
            self, text="Home Page", command=lambda: controller.show_frame(PageOne)
        )
        button1.grid(row=0, sticky="S")


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(
            self, text="Home Page", command=lambda: controller.show_frame(StartPage)
        )
        button1.pack()
        button2 = ttk.Button(
            self, text="Page Two", command=lambda: controller.show_frame(PageTwo)
        )
        button2.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(
            self, text="Home Page", command=lambda: controller.show_frame(StartPage)
        )
        button1.pack()
        button2 = ttk.Button(
            self, text="Page One", command=lambda: controller.show_frame(PageOne)
        )
        button2.pack()


app = math()
app.state("zoomed")  # Makes the application windowed fullscreen
app.mainloop()
