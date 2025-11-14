def activity1():
    print("Hello World")

def activity2():
    name = input("What is your name? ")
    print("Hi", (name), "welcome to the Matrix")
    
def activity3():
    print("\t\tHappy \nMonday")
    print("BSIT 1A \n\t\tfrom DLL")
    print("The Quick Brown Fox \rJumps Over The Lazy \\Dog")
    print("\"Be Happy on your Life\"")

def activity4():
    name = input("Enter a string")
    print("Your name has", len(name), "characters")

def activity5():
    something = eval(input("Input something -->"))
    print("The data type of something is", type(something))
    answer = 7 + something
    print("The answer is", answer)

def activity6():
    n1 = eval(input("Enter the first number : "))
    n2 = eval(input("Enter the second number : "))
    s = n1 + n2
    d = n1 - n2
    p = n1 * n2
    q = n1 / n2

    solution = ((n1 / n2) * 100 - 5 ) // 300
    print("\nThe sum of",n1,"and" ,n2, "is",s)
    print("The difference of",n1, "and",n2, "is",d)
    print("The product of",n1, "and" ,n2, "is",p)
    print("The quotient of" ,n1,"and",n2, "is",q)
    print(n1, "exponent by",n2, "is",n1**n2)
    print("The remainder of",n1, "and",n2, "is",n1 % n2)
    print("The floor division of","and",n2,"is",n1//n2)