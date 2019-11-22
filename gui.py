from tkinter import *
from tkinter import filedialog

window = Tk()

width_value = window.winfo_screenwidth()
height_value = window.winfo_screenheight()
window.geometry("{}x{}-0+0".format(width_value, height_value))


def open_file():
    window.filename = filedialog.askopenfile(
        title="Select a file",
        filetypes=(("csv files", "*.csv"), ("other files", "*.*")),
    )


file_openbutton = Button(window, text="Open File", command=open_file)
file_openbutton.pack()
two = Label(
    window, text="Select the csv file containing the data", bg="white", fg="black"
)
two.pack()
topFrame = Frame(window)
topFrame.pack()


button1 = Button(topFrame, text="Principle Component Analysis", fg="red")
button2 = Button(topFrame, text="General Linear Model Analysis", fg="green")

button1.pack(side=LEFT)
button2.pack(side=BOTTOM)

one = Label(
    window, text="Select the type of analysis to conduct", bg="white", fg="black"
)
one.pack()


window.mainloop()
