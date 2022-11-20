class Person:

    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Name:{self.fullname} Age: {self.age} married:{self.is_married}')

class Student(Person):
    def __init__(self, fullname, age, is_married, marks: dict):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def introduce_myself(self):
        print(f'Name:{self.fullname} Age: {self.age} married:{self.is_married} marks: {self.marks}')

    def average_mark(self):
        print(sum(self.marks.values()) / len(self.marks.values()))

class Teacher(Person):
    salary = 20000
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def average_salary(self):
        if self.experience > 3:
            a = self.salary + ((self.salary / 100 * 5) * (self.experience - 3))
            return a

def create_students():
    student1 = Student('Aziz' , 19 , 'Yes', marks={
        'math ': 2,
        'biology' : 3,
        'algebra' : 3
    })
    student2 = Student('Aziz', 19, 'Yes', marks={
        'math ': 2,
        'biology': 3,
        'algebra': 3
    })
    student3 = Student('Aziz' , 19 , 'Yes', marks={
        'math ': 2,
        'biology' : 3,
        'algebra' : 3
    })
    some = [student1,student2,student3]
    return some

any = create_students()
for i in any:
    t = []
    for marks in i.marks.values():
            t.append(marks)
    print(f"Name:{i.fullname}\n"
          f"Age:{i.age}\n"
          f"Marriage:{i.is_married}\n"
          f"Average:{sum(t) / len(t)}\n")


teach = Teacher('ata' , 16 , " no", 10)
teach.average_salary()
stud = Student('Aziz' , 19 , 'Yes', {'math': 2 , 'geography': 3 , 'biology': 2})

stud.average_mark()

stud.introduce_myself()
student = Person('Atay', 18, 'No')
# print(student)
student.introduce_myself()