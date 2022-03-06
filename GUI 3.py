from tkinter import *
root = Tk()

root.title("Using a label for a picture")

coin_image = PhotoImage(file="giphy.gif")

image_label = Label(root, image=coin_image)
image_label.pack()

text_label = Label(root, text="Money of $? worth", font=("Courier", 25, "bold"), fg="green", bg="gold")

text_label.pack()

root.mainloop()
