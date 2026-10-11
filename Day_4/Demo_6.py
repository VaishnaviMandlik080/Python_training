
'''
Demonstrate inheritance:
- Person stores a name.
- Vendor inherits from Person and adds a vendor ID.
- Display the vendor's name and ID.
'''

class Person:
    def __init__(self, name):
        self.name = name


class Vendor(Person):
    def __init__(self, name, vId):
        super().__init__(name)
        self.vId = vId


obj = Vendor("Vaishnavi", "V1234")
print(obj.name)
print(obj.vId)