student_credentials = []

student = input("Would you like to add a student (Y or N)? ")

while student != "N":
    student_name = input("What is the student's name? ")
    student_mark = int(input("What is the student's mark? "))
    student_credentials.append(student_name, student_mark)

    print(student_credentials)
