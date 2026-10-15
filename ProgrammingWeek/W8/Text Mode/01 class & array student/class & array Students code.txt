#Written in Python IDLE 3.14.6
class Student:
    def __init__(self, student_id, name, course, age):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.age = age

    def show(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Age:", self.age)


# อ่านข้อมูลจาก text file
students = []

with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        data = line.strip().split(",")

        student_id = data[0]
        name = data[1]
        course = data[2]
        age = int(data[3])

        student = Student(student_id, name, course, age)
        students.append(student)


# ฟังก์ชันแสดงนักเรียนที่อายุน้อยที่สุด
def show_youngest(students):
    youngest = students[0]

    for student in students:
        if student.age < youngest.age:
            youngest = student

    youngest.show()


# เรียกใช้
show_youngest(students)
