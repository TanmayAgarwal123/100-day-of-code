from tkinter import *

windows = Tk()
windows.title("Flash Card")
windows.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=800, height=526, bg="white", highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)


windows.mainloop()
