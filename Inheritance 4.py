class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name}, and I am {self.age} years old.")

    def speak(self):
        print("I don't know what to say")


class Cat(Pet):
    def speak(self):
        print("Meow")


class Dog(Pet):
    def speak(self):
        print("Woof")


class Snake(Pet):
    pass


# Main Routine

c = Cat("Tim", 7)
c.show()
c.speak()
print()

d = Dog("Jack", 10)
d.show()
d.speak()
print()

p = Pet("Liz", 5)
p.show()
p.speak()
print()

s = Pet("Hissy", 2)
s.show()
s.speak()
