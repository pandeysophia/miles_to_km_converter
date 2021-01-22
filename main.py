from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=100, pady=100)

entry = Entry(width=20)
entry.grid(column=1, row=0)

label = Label(text="Miles")
label.grid(column=2, row=0)

label = Label(text="is equal to")
label.grid(column=0, row=2)

label = Label(text="Km")
label.grid(column=2, row=2)

label = Label(text="0")
label.grid(column=1, row=2)

def action():
    new_text = int(entry.get())
    label.config(text=new_text * 1.6)


button = Button(text="Calculate", command=action)
button.grid(column=1, row=3)

window.mainloop()
