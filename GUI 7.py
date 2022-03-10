from tkinter import *
root = Tk()

root.geometry("800x400")
root.maxsize(600, 400)

root.title("Coloured Box Interface")
blue = Label(root, bg="blue", fg="white", text="blue")
blue.pack(padx=20, pady=20, fill=BOTH, expand=YES, side=RIGHT)

root.title("Coloured Box Interface")
red = Label(root, bg="red", fg="white", text="red")
red.pack(side=LEFT, fill=Y)

root.title("Coloured Box Interface")
green = Label(root, bg="green", fg="white", text="green")
green.pack(side=BOTTOM, fill=X)

blue.pack()
red.pack()
green.pack()

root.mainloop()
