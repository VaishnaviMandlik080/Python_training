'''
Demonstrate method overriding:
- Animal defines the speak() method.
- Dog overrides speak() with its own implementation.
- super().speak() also calls the parent class method.
'''

class Animal:
    def speak(self):
        print("Animal makes Sound")


class Dog(Animal):
    def speak(self):
        print("Dog barks")
        super().speak()  # Call the parent class method


obj1 = Dog()
obj1.speak()