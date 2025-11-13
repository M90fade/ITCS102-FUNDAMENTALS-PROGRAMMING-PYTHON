#creating your OWN functions
#keyword, def - define
#the content inside the parenthesis is called - PARAMETER / ARGUMENT
#CODE REUSABILITY

def greeter(name):
    print(f"Hi {name}, how are you? ")

def summation(x):
    sum = 0
    for y in range(x, 0, -1):
        sum += y
    print(f"the sum of {x}, is {sum}")

def my_Factorial(x):
    fact = 1
    for y in range(x, 0, -1):
        fact *= y
    return fact

print(f"The factorial of 10 is {my_Factorial(5) + 30}")

summation(9)
summation(12)

greeter('Moses')
greeter('Faderagao')
greeter('Sebastian')
