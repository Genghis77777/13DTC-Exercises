from tkinter import *
root = Tk()


def say_hi():
    Label(root, bg="yellow", fg="red", text="Hi User!", font=("Times", 50, "bold")).pack()

root.title("My First Button")
root.minsize(200, 100)

button1 = Button(root, text="Say hi!", command=say_hi)
button1.pack()

root.mainloop()
