class Person:
    def __init__(self, first, last, age):
        self.teachers=[]
        self.students=[]
        self.first_name = first
        self.last_name = last
        self.age = age
        self.academy = "National Technical University of Ukraine"

class Teacher(Person):
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

class Student(Person):
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

class Academy:
    def __init__(self,name):
        self.name=name
        self.teachers=[]
        self.students=[]
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    def add_teacher(self,teacher):
        self.teachers.append(teacher.fullname())
    def add_student(self,student):
        self.students.append(student.fullname())

teacher_list=[]
teacher1 = Teacher("Kiril", "Lutsenko", "49")

teacher2 = Teacher("Pert", "Vashull", "34")

student1 = Student("Petr2", "Poplavsky", "21")

student2 = Student("Petr3", "Poplavsky2", "22")

student3 = Student("Petr4", "Poplavsky3", "23")

student4 = Student("Petr5", "Poplavsky4", "24")
academy=Academy("National Technical University of Ukraine")

academy.add_teacher(teacher1)
academy.add_teacher(teacher2)
academy.add_student(student1)
academy.add_student(student2)
academy.add_student(student3)
academy.add_student(student4)

print(academy.teachers)

print(academy.students)
