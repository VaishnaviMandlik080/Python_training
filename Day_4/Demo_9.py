
'''
Demonstrate aggregation:
- Create a Teacher object independently.
- Pass it to a Dept object.
- The department stores a reference to the teacher.
- The teacher can exist independently of the department.
'''

class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self):
        print(self.name, "is teaching.")


class Dept:
    def __init__(self, teacher):
        self.teacher = teacher


teacher1 = Teacher("Vaishnavi")
dept = Dept(teacher1)
dept.teacher.teach()