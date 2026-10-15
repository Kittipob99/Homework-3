#Written in Python IDLE 3.14.6
class Person:
    def __init__(self, name, address, weight, height):
        self.name = name
        self.address = address
        self.weight = weight
        self.height = height

    def show(self):
        print("Name :", self.name)
        print("Address :", self.address)
        print("Weight :", self.weight, "kg")
        print("Height :", self.height, "m")

    def getBMI(self):
        bmi = round((self.weight / (self.height ** 2)),1)
        return bmi


class Student(Person):
    def __init__(self, name, address, weight, height,
                 student_id, course, gpa):
        super().__init__(name, address, weight, height)
        self.student_id = student_id
        self.course = course
        self.gpa = gpa

    def show(self):
        super().show()
        print("Student ID :", self.student_id)
        print("Course :", self.course)
        print("GPA :", self.gpa)
        print("BMI :", self.getBMI())


class Employee(Person):
    def __init__(self, name, address, weight, height,
                 employee_id, department, salary):
        super().__init__(name, address, weight, height)
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def show(self):
        super().show()
        print("Employee ID :", self.employee_id)
        print("Department :", self.department)
        print("Salary :", self.salary)
        print("BMI :", self.getBMI())


# สร้าง Object Student
student1 = Student(
    "Somchai",
    "Bangkok",
    60,
    1.70,
    "S001",
    "Computer Science",
    3.50
)

# สร้าง Object Employee
employee1 = Employee(
    "Somsak",
    "Chiang Mai",
    75,
    1.75,
    "E001",
    "IT",
    30000
)


# แสดงข้อมูล
print("===== Student =====")
student1.show()

print()

print("===== Employee =====")
employee1.show()
