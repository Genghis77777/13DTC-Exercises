time = ""
times = []
fastest = 99999999999999999999

while time != -1:
     time = int(input("Enter time: "))
     if time != -1:
          times.append(time)

total = 0

for item in times:
     print(item)
     total += int(item)
     if fastest > item:
          fastest = item

average = total/len(times)

print(f"The Average Time was {average}")
print(f"The Fastest Time was {fastest}")

