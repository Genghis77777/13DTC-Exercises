from tkinter import *
root = Tk()


def count_up():
    count = 0
    while count != 100:
        text_variable = count
        count = count + 1


def count_down():
    count = 0
    while count != -100:
        print(count)
        count = count - 1

root.title("My First Button")
root.minsize(200, 100)

button1 = Button(root, text="Count Up", command=count_up)
button1.pack()

button2 = Button(root, text="Count Down", command=count_down)
button2.pack()

root.mainloop()
