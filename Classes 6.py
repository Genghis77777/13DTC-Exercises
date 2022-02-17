class Bus:
    def __init__(self, number, route_key, driver):
        self.number = number
        self.route_key = route_key
        self.driver = driver
        bus_list.append(self)

bus_list = []

bus1 = Bus(2010, "Y", "Robert")
bus2 = Bus(2002, "JB98", "Matt")
bus3 = Bus(1279, "MUL3", "Albert")

for bus in bus_list:
    print(f"\nThis bus was created in {bus.number},"
          f"\nIts route key is {bus.route_key}"
          f"\nIts driver's name is {bus.driver}")
