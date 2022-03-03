class Student:
    def __init__(self, name, age, phone_number, form_class, subjects, is_male):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.form_class = form_class
        self.subjects = subjects
        self.is_male = True
        self.enrolled = True
        student_list.append(self)

    def display_info(self):
        print(f"\nName: {self.name}")
        print(f"Age: {self.age}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Form Class: {self.form_class}")
        print(f"Subjects: {self.subjects}")
        print(f"Gender: {self.is_male}")
        print(f"Enrolled: {self.enrolled}\n")


def print_student_details():
    for student in student_list:
        Student.display_info(student)


def select_student_age():
    select_age = int(input("Enter the age of the student: "))
    for student in student_list:
        if student.age > select_age:
            Student.display_info(student)


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
    print(student_count)

# Main Routine
student_list = []
generate_students()

print("-----------Select Students-------------")
select_student_age()
print("-----------Student Details-------------")
print_student_details()
print("------------Count Students-------------")
count_students()
