event = input("Which event would you like to enter (100m, 200m or 400m)? ")
one_hundred_time = 0
one_hundred_times = []
two_hundred_time = 0
two_hundred_times = []
four_hundred_time = 0
four_hundred_times = []
fastest = 999999999999999999


def one_hundred(one_hundred_time):
    while one_hundred_time != -1:
        one_hundred_time = int(input("Enter time: "))
        if one_hundred_time != -1:
            one_hundred_times.append(one_hundred_time)

        total = 0

        for item in one_hundred_times:
            print(item)
            total += int(item)
            if fastest > item:
                fastest = item

        average = total/len(one_hundred_times)

        print(f"The Average Time was {average}")
        print(f"The Fastest Time was {fastest}")

def two_hundred(two_hundred_time):
    while two_hundred_time != -1:
        two_hundred_time = int(input("Enter time: "))
        if two_hundred_time != -1:
              one_hundred_times.append(two_hundred_time)

        total = 0

        for item in one_hundred_times:
            print(item)
            total += int(item)
            if fastest > item:
                fastest = item

        average = total/len(one_hundred_times)

        print(f"The Average Time was {average}")
        print(f"The Fastest Time was {fastest}")

def four_hundred(four_hundred_time):
    while four_hundred_time != -1:
        four_hundred_time = int(input("Enter time: "))
        if four_hundred_time != -1:
              four_hundred_times.append(four_hundred_time)

        total = 0

        for item in one_hundred_times:
            print(item)
            total += int(item)
            if fastest > item:
                fastest = item

        average = total/len(one_hundred_times)

        print(f"The Average Time was {average}")
        print(f"The Fastest Time was {fastest}")


if event == "400m":
    four_hundred(four_hundred_time)

elif event == "200m":
    two_hundred(two_hundred_time)

elif event == "100m":
    one_hundred(one_hundred_time)
