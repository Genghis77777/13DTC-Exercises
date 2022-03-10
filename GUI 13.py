from tkinter import *
root = Tk()


class Option:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        fillings.append(self)


def generate_options():
    choices = []
    for filling in choices:
        choices.append(f"{filling.name} ${filling.price:.2f}")
    return choices


def exit_program():
    root.destroy()

root.title("Dropdown From Class")
root.geometry("300x90")
fillings = []

Option("Cheese", 2.5)
Option("Beef", 3.5)
Option("Chicken", 3)
Option("Egg", 1.5)
Option("Lettuce", 1)

label_text = StringVar()
option_choices = generate_options()

label_text.set("Choose filling...")

option = OptionMenu(root, label_text, *option_choices)
option.pack()

label = Label(root, textvariable=label_text)
label.pack()

exit_button = Button(root, text="Exit Program", command=exit_program)
exit_button.pack()

root.mainloop()
