import tkinter as tk
from tkinter import ttk

# MATTPLOTLIB USED FOR GRAPHS
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


LARGE_FONT = ("Stencil", 24)


dataSet = []


class math(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, "Data Analyzer")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)  # sets size and priority(weight)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (
            StartPage,
            PageOne,
            PageTwo,
        ):  # https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # streches to size of window

        self.show_frame(StartPage)  # Sets the initial screen/frame

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()  # raise the frame to the front (so that it is visible)


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Data Analysis Helper", font=LARGE_FONT)
        label.pack()

        options = ttk.Combobox(
            self, values=["January", "February"], width=25, justify="center"
        )
        options.pack(anchor="c")

        # options.bind("something", callbackFunc)
        options.set("Please select a data set")

        f1 = tk.Frame(width=200, height=200, background="grey")
        f1.pack(fill="both", expand=True, padx=20, pady=20)

        button2 = ttk.Button(
            self,
            text="Execute",
            command=lambda: [
                dataSet.append(options.get()),
                controller.show_frame(PageOne),
                print(dataSet[0]),
            ],
        )
        button2.pack(anchor="center")


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=dataSet[0], font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(
            self, text="Back", command=lambda: controller.show_frame(StartPage)
        )
        button1.pack(side="left", anchor="s", pady=10, padx=10)
        button2 = ttk.Button(
            self, text="Next", command=lambda: controller.show_frame(PageTwo)
        )
        button2.pack(side="right", anchor="s", pady=10, padx=10)


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(
            self, text="Home Page", command=lambda: controller.show_frame(StartPage)
        )
        button1.pack(side="right", anchor="s", pady=10, padx=10)
        button2 = ttk.Button(
            self, text="Back", command=lambda: controller.show_frame(PageOne)
        )
        button2.pack(side="left", anchor="s", pady=10, padx=10)


app = math()
app.state("zoomed")  # Makes the application windowed fullscreen
app.mainloop()
