

'''
Create an Enrollment class.
Initialize and display the name, date of birth and place
for two enrollment objects.
'''

class Enrollment:
    name = ''
    dob = ''
    place = ''

    def initialize(self, name, dob, place):
        self.name = name
        self.dob = dob
        self.place = place
        print(f"Enrollment initialized for: {self.name}")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.dob}")
        print(f"Place: {self.place}")


obj1 = Enrollment()
obj1.initialize("Vaishnavi", "1990-01-01", "Bengaluru")

obj2 = Enrollment()
obj2.initialize("Vaishnavi", "1992-05-12", "Chennai")

obj1.display()
obj2.display()