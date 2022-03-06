from tkinter import *
root = Tk()

root.title("My First Window")

root.geometry("600x200")
root.maxsize(800, 400)

greeting = Label(text="Hello Tkinter")

greeting.pack()

root.mainloop()
