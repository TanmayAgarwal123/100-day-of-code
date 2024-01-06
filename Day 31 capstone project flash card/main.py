BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *

windows = Tk()
windows.title("Flashy")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg="white", highlightthickness=0)
front_img = PhotoImage(file="Day 31 capstone project flash card/images/card_front.png")
back_img = PhotoImage(file="Day 31 capstone project flash card/images/card_back.png")
card_img = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)



windows.mainloop()
