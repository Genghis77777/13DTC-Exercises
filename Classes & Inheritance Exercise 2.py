class Student:
    def __init__(self, name, age, phone_number, form_class, subjects, is_male):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.form_class = form_class
        self.subjects = subjects
        self.is_male = is_male  # Fix this
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
    for student in student_list:
        if student.age > select_age:
            student.display_info()


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
    for student in student_list:
        if student.name == student_to_find:
            student.display_info()
        else:
             print("Sorry, there's no student by that name.")

# Main Routine
student_list = []
generate_students()

print("-----------Select Students-------------")
# select_student_age()
print("------------Find Student---------------")
# find_student()
print("-----------Student Details-------------")
# print_student_details()
print("------------Count Students-------------")
count_students()
