def say_hello(): # Define a function, thus it can be easier to use as a block
    print("Hello")

say_hello() # Do the function as the definition
say_hello()
say_hello()

# Anatomy of a function
def greet():
    print("Welcome!")
# def -> tells Python youre creating a function
# greet -> function name 
# () -> parameters go here
# : -> start the function body

def greet (name):
    print("Hello", name)

greet("Oweyn")

def add(a,b):
    return a + b    # function should give back something

result = add(10,5)
print (result)

# print() ->  display, return -> sends a value back

# ---------------------------------------- #
## Mini Project
def rectangle_area(length, width):
    area = length * width
    return area

result = rectangle_area (8,5)

print("Area =", result)

# ---------------------------------------- #
# Exercise 1
def say_goodbye():
    print("Goodbye!")

say_goodbye()

# Exercise 2
def square(number):
    return number * number

print(square(6))

# Exercise 3
def average(a,b,c):
    return (a+b+b)/3

print(average(1,2,3))

# Mini challenge
def countdown():
    for i in range (5, 0, -1):
        print(i)
    print("\n🚀 Lift off!")

countdown() 