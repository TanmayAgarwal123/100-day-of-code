from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

def calculate():
    miles = float(input.get())
    km = miles * 1.609
    label3.config(text=f"{km}")

label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = Label(text="0")
label3.grid(row=1, column=1)

label4 = Label(text="Km")
label4.grid(row=1, column=2)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

input = Entry(width=10)
input.grid(row=0, column=1)

window.mainloop()

