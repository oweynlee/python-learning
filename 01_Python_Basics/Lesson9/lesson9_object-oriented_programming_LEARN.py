class Blueprint:    # Create a class
    def __init__(self, name, age):  #__init__: [double underscore] special (dunder) methods/variables
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

car = Blueprint()  # car is an instance of the Blueprint class, the () is used to create an instance of the class
car.greet()  # Output: Hello, my name is Alice and I am 30 years old.

car.add() #adding into the class Blueprint

car.pop() # remove by the index of the list
car.remove() # remove by the value of the list
car.add() # add into the list

