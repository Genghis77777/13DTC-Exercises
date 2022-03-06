from tkinter import *
root = Tk()

root.title("Welcome")
welcome1 = Label(root, bg="lime", fg="white", text="Computer", font=("Times", 50, "italic"))

root.title("Welcome")
welcome2 = Label(root, bg="blue", fg="yellow", text="Science Is", font=("Comic Sans MS", 50, "bold"))

root.title("Welcome")
welcome3 = Label(root, bg="orange", fg="red", text="Awesome!", font=("Normal", 50, "bold"))

welcome1.pack()
welcome2.pack()
welcome3.pack()

root.mainloop()
