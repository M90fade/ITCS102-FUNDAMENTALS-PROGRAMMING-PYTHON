from activity25_1 import *
# from activity25_1 import activity2
# from activity25_1 import activity3


#Creating a Menu Options with While Loop and Functions

name = input("Hi, What is your name? -->")
print(f"Welcome {name}, to my Compiler Program")

isContinue = True

while isContinue == True:
    print("Select a program")
    print("A - Activity1\nB - Activity2\nC - Activity3\nD - Activity4\nF - Activity5\nG - Activity6\nE - Exit")

    choose = input("What program / code would you like to run --> ").lower()

    if choose == 'a':
        activity1()
        continue
    elif choose == 'b':
        activity2()
        continue
    elif choose == 'c':
        activity3()
        continue
    elif choose == 'd':
        activity4()
        continue
    elif choose == 'f':
        activity5()
        continue
    elif choose == 'g':
        activity6()
        continue
    elif choose == 'e':
        print("Program Stops")
        break
    else:
        print("Invalid")
        continue
        