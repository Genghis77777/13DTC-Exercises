total_volume = 0

build = input("Do you want to build (Y or N)? ")

while build == "Y":
    build_type = input("What type of building are you building (residential or commercial)? ")
    length = int(input("What is the length of the building in meters? "))
    width = int(input("What is the width of the building in meters? "))

    if build_type == "residential":
        depth = 0.5

    else:
        depth = 0.25

    volume = length * width * depth

    print(f"The volume of concrete required for a slab with a length of {length} and a n/"
          f"width of {width} and a depth of {depth} is {volume} cubic meters")

    total_volume = total_volume + volume

    print(f"The total volume of concrete made is {total_volume}")
