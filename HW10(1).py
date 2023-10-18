class Academy:
    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.academy = "National Technical University of Ukraine"

    def fullname(self):
        return f"{self.first_name} {self.last_name}"


class Teacher:
    def __init__(self, first, last, age, department):
        Academy.__init__(self, first, last, age)
        self.department = department

    def full_name(self):
        return Academy.fullname(self)


class Student:
    def __init__(self, first, last, age, major):
        Academy.__init__(self, first, last, age)
        self.major = major

    def full_name(self):
        return Academy.fullname(self)


class Department:
    global major1
    global major2
    global cs_department
    global ecn_department
    global students
    major1 = ["Audit", "Global Economics", "Finance", "Marketing"]
    major2 = ["Computer Science", "Information Science"]
    cs_department = []
    ecn_department = []

    def __init__(self, students: list):
        self.students = students
        self.cs_department = cs_department
        self.ecn_department = ecn_department

    def ecn_department_ty(self):
        stud = []
        for i in range(len(students)):
            if students[i].major in major1:
                self.ecn_department.append(students[i])
        for i in range(len(self.ecn_department)):
            stud.append(self.ecn_department[i].full_name())
        return print("Students of the Department of Economics: ", stud)

    def cs_department_ty(self):
        stud = []
        for i in range(len(students)):
            if students[i].major in major2:
                self.cs_department.append(students[i])
        for i in range(len(self.cs_department)):
            stud.append(self.cs_department[i].full_name())
        return print("Students of the Department of Computer Science: ", stud)
        # elif students[i] in major2:
        #     self.cs_department.append(students[i])

    # @property
    # def cs_department(self):
    #     return self.__cs_department
    #     # self.exn_department=[]
    #
    # @cs_department.setter
    # def cs_depertment(self, cs_department):
    #     for i in range(len(students)):
    #         if students[i] in major1:
    #             self.cs_department.append(students[i])
    #         # elif students[i] in major2:
    #         #     self.cs_department.append(students[i])
    #
    # @property
    # def ecn_department(self):
    #     return self.__ecn_department
    #     # self.exn_department=[]
    #
    # @ecn_department.setter
    # def ecn_depertment(self, ecn_department):
    #     for i in range(len(students)):
    #         if students[i] in major1:
    #             self.ecn_department.append(students[i])
    #
    # else:
    #     self.cs_department = department
    #     self.ecn_department = department

    # # def add_std_to_department(self,Student):
    #     if major in major1:
    #         self.ecn_department.append(Student)
    #     elif major in major2:
    #         self.cs_department.append(Student)
    # def print_cs_department(self):
    #     stud=[]
    #     for i in range(len(self.cs_department_ty())):
    #         pass
    #
    #
    #
    #
    #     # for i in range(len(self.cs_department)):
    #     #     stud.append(self.cs_department[i])
    #     # return print("Students of the Computer Science Department: ", stud)
    #
    # def print_ecn_department(self):
    #     for students[i] in self.ecn_department:
    #         print("Students of the Department of Ecomonics: ", students.fullname())


teacher1 = Teacher("Kiril", "Lutsenko", "49", "Economics")

teacher2 = Teacher("Pert", "Vashull", "34", "Computer Science")

student1 = Student("Petr2", "Poplavsky", "21", "Audit")

student2 = Student("Petr3", "Poplavsky2", "22", "Finance")

student3 = Student("Petr4", "Poplavsky3", "23", "Computer Science")

student4 = Student("Petr5", "Poplavsky4", "24", "Information Science")

print(student3.first_name)
print(teacher2.department)
print(student3.academy)
print(student4.full_name())
print(teacher1.full_name())
students = [student1, student2, student3, student4]
print(students[1].major)

print(student1)
departments = Department(students)
departments = departments.cs_department_ty()
departments = Department(students)
departments1 = departments.ecn_department_ty()


# departments.print_cs_department()
