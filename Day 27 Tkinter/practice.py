from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="left")
my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
def button_clicked():
    print("I got clicked")
    my_label.config(text="Button Got Clicked")
    
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()
# input.get()
# input.delete(0, END)
# input.insert(END, string="Some text to begin with.")

# Text
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multi-line text entry.")
# Get all text in textbox
# text.get("1.0", END)
text.pack()

# Spinbox
def spinbox_used():
    print(spinbox.get())
    
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton
# def checkbutton_used():
#     print(checked_state.get())
    
# checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?")#, variable=checked_state, command=checkbutton_used)
#checked_state.get()
checkbutton.pack()

# Radiobutton
def radio_used():
    print(radio_state.get())
    
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# Layout Manager
# Place
my_label.place(x=100, y=200)
# Pack
my_label.pack(side="left")
# Grid
#my_label.grid(column=0, row=0)
#button.grid(column=1, row=1)

window.mainloop()