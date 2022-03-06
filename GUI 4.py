from tkinter import *
root = Tk()

root.title("Middleton Grange School Image")

coin_image = PhotoImage(file="MGSLogo.png")

image_label = Label(root, image=coin_image)
image_label.pack()

text_label = Label(root, text="Middleton Grange School",
                   font=("Courier", 25, "bold"), fg="green", bg="white")

text_label.pack()

root.mainloop()
