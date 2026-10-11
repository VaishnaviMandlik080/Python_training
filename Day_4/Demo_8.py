
'''
Demonstrate composition (a Has-A relationship):
- A Car contains an Engine object.
- When driving() is called, the engine starts first.
'''

class Engine:
    def start(self):
        print("Engine has started")


class Car:
    def __init__(self):
        self.engine_obj = Engine()  # Car has an Engine

    def driving(self):
        self.engine_obj.start()
        print("Car is being driven")


obj = Car()
obj.driving()