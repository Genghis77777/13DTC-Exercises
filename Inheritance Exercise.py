class AllStaff:
    def __init__(self, name, age, birthdate, job):
        self.name = name
        self.age = age
        self.birthdate = birthdate
        self.job = job

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old\n"
              f"and I was born on {self.birthdate},\n"
              f"my job is {self.job}")


class Management(AllStaff):
    def __init__(self, name, age, birthdate, job, car):
        super().__init__(name, age, birthdate, job)
        self.car = car

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old\n"
              f"and I was born on {self.birthdate},\n"
              f"my job is {self.job}, and my car is a {self.car}")


class Clerical(AllStaff):
    def __init__(self, name, age, birthdate, job, typing_speed):
        super().__init__(name, age, birthdate, job)
        self.typing_speed = typing_speed

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old\n"
              f"and I was born on {self.birthdate},\n"
              f"my job is {self.job}, my typing speed is {self.typing_speed}.")


class Factory(AllStaff):
    def __init__(self, name, age, birthdate, job):
        super().__init__(name, age, birthdate, job)


m = Management("Bill", 46, "17/09/1976", "Head of Management", "Blue Car")
m.show()
print()

c = Clerical("Sammy", 23, "04/05/1999", "Head of Keyboards", "Infinite")
c.show()
print()

f = Factory("Cecil", 35, "12/11/1988", "Best Factory Worker")
f.show()
print()
