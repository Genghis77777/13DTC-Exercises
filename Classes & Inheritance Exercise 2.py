class Student:
    def __init__(self, name, age, phone_number, form_class, subjects, is_male):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.form_class = form_class
        self.subjects = subjects
        self.is_male = is_male
        self.enrolled = True
        student_list.append(self)

    def display_info(self):
        print(f"\nName: {self.name}")
        print(f"Age: {self.age}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Form Class: {self.form_class}")
        print(f"Subjects: {self.subjects}")
        if self.is_male:
            print("Gender: Male") # Fix this
        print(f"Enrolled: {self.enrolled}\n")


def print_student_details():
    for student in student_list:
        student.display_info()


def select_student_age():
    select_age = int(input("Enter the age of the student: "))
    student_count = 0
    for student in student_list:
        if student.age > select_age:
            student.display_info()
            student_count += 1
    print(f"There are {student_count} students aged over {select_age}")


def generate_students():
    import csv
    with open('random_students.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter='|')
        for line in filereader:
            if line[5] == "True":
                is_male = True
            else:
                is_male = False
            Student(line[0], int(line[1]), line[2], line[3], line[4], is_male)


def count_students():
    what_class = input("Enter the class you are looking for: ")
    student_count = 0
    for student in student_list:
        if what_class in student.subjects:
            student_count += 1
    if student_count == 0:
        print(f"There are no students in {what_class}")
    return student_count


def find_student():
    student_to_find = input("Enter the name of the student: ").title()
    found = False
    for student in student_list:
        if student.name == student_to_find:
            student.display_info()
            found = True
    if not found:
        print("Sorry, there's no student by that name.")


def add_student():
    name = input("Enter the name of the new student: ").title()
    age = int(input("Enter then age of the new student: "))
    phone_number = input("Enter the phone number of the new student: ")
    form_class = input("Enter the form class of the new student: ")
    subjects = input("Enter the subjects of the new student: ")
    is_male = input("Enter the gender of the new student ('M' or 'F'): ")
    if is_male == "M":
        is_male = True
    else:
        is_male = False
    Student(name, age, phone_number, form_class, subjects, is_male)
    print(f"{name} has been added to the student list!")


# Main Routine
student_list = []
generate_students()

main_menu = True

while main_menu:
    print("------------------WELCOME-------------------")
    print("Welcome to the Main Menu for the Student System!\n\n"
          "Please select one of the options below by typing in the number\n"
          "corresponding to the function you would like to select.")

    print("\n1. Select Student Age")
    print("2. Find Student")
    print("3. See Student Details")
    print("4. Count Students")
    print("5. Add Student")
    print("6. Exit\n")

    menu_choice = int(input("Where would you like to go (type a number 1-5, below)? \n"))

    if menu_choice == 1:
        print("-----------Select Student Age------------")
        select_student_age()
    elif menu_choice == 2:
        print("--------------Find Student---------------")
        find_student()
    elif menu_choice == 3:
        print("------------Student Details--------------")
        print_student_details()
    elif menu_choice == 4:
        print("-------------Count Students--------------")
        count_students()
    elif menu_choice == 5:
        print("--------------Add Students---------------")
        add_student()
    elif menu_choice == 6:
        confirm_exit = input("Are you sure you want to exit (Type 'Y' or 'N')? ").upper()
        if confirm_exit == "Y":
            print("Goodbye")
            main_menu = False
    else:
        print("That is not a valid choice.")

