from cc1 import *
from cc2 import *
from act14 import activity14
from act13 import activity13      
import os
import time
#FINAL PROJECT
#make a compiler of all activities and code challenges
#using a function and conditional statements

name = input("Hello, I would like to know what is your name? -->")
print(f"Welcome {name.title()}, to my FINAL PROJECT!")
print("Enjoy Using my Program!")

isContinue = True

while isContinue == True:
    print("\n\t MAIN MENU")
    print("====================================")
    print("\n\tM - OPEN THE MENU\n\tS - CLOSE THE PROGRAM")
    print("\n====================================")
    door = input("What would you like to choose? --> ").lower()
    os.system('cls')
    if door == 'm':
        while True:
            print("====================================")
            print("\n\tMENU")
            print("\n\tA - ACTVITIES\n\tC - CODE CHALLENGES\n\tD - DEFINITION\n\tE - Exit")
            print("\n====================================")
            two = input("What would you like to open? --> ").lower()
            os.system('cls')

            if two == 'a':
                while True:
                    print("====================================")
                    print("CHOOSE THE FOLDER OF ACTIVITY YOU'D LIKE TO OPEN")
                    print("\n\tA - ACT(1-7)\n\tB - ACT(8-14)\n\tC - ACT(15-21)\n\tD - ACT(22-28)\n\tE - EXIT")
                    print("\n====================================")
                    choose = input("\nWhat folder would you like to run --> ").lower()
                    os.system('cls')

                    # activity from 1-7
                    if choose == 'a':
                        while True:
                            print("\nSelect an Activity you'd like to Open")
                            print("Choose a number from the options below")
                            print("====================================")
                            print("\n\t1 - Act1\n\t2 - Act2\n\t3 - Act3\n\t4 - Act4\n\t5 - Act5\n\t6 - Act6\n\t7 - Act7\n\t0 - Close")
                            print("\n====================================")
                            choice = eval(input("What program/code would you like to run? -->"))
                            os.system('cls')
                            from first_file import *

                            if choice == 1:
                                activity1()
                                continue
                            elif choice == 2:
                                activity2()
                                continue
                            elif choice == 3:
                                activity3()
                                continue
                            elif choice == 4:
                                activity4()
                                continue
                            elif choice == 5:
                                activity5()
                                continue
                            elif choice == 6:
                                activity6()
                                continue
                            elif choice == 7:
                                activity7()
                                continue
                            elif choice == 0:
                                print("Close")
                                break
                            else:
                                print("Invalid Choice, Please pick again")
                                continue
                    # activity from 8-14
                    elif choose == 'b':
                        while True:
                            print("\nSelect an Activity you'd like to Open")
                            print("Choose a number from the options")
                            print("====================================")
                            print("\n\t8 - Act8\n\t9 - Act9\n\t10 - Act10\n\t11 - Act11\n\t12 - Act12\n\t13 - Act13\n\t14 - Act14\n\t0 - Close")
                            print("\n====================================")
                            choice = eval(input("What program/code would you like to run? -->"))
                            os.system('cls')
                            from second_file import *

                            if choice == 8:
                                print("\tOUTPUT")
                                print("============================")
                                activity8()
                                continue
                            elif choice == 9:
                                print("\tOUTPUT")
                                print("============================")
                                activity9()
                                continue
                            elif choice == 10:
                                print("\tOUTPUT")
                                print("============================")
                                activity10()
                                continue
                            elif choice == 11:
                                print("\tOUTPUT")
                                print("============================")
                                activity11()
                                continue
                            elif choice == 12:
                                print("\tOUTPUT")
                                print("============================")
                                activity12()
                                continue
                            elif choice == 13:
                                print("\tOUTPUT")
                                print("============================")                   
                                activity13()
                                continue
                            elif choice == 14:
                                print("\tOUTPUT")
                                print("============================")
                                activity14()
                                continue
                            elif choice == 0:
                                print("Close")
                                break
                            else:
                                print("Invalid Choice, Please pick again")
                                continue
                    # activity from 15-21
                    elif choose == 'c':
                        while True:
                            print("\nSelect an Activity you'd like to Open")
                            print("====================================")
                            print("Choose a number from the options")
                            print("\n\t15 - Act15\n\t16 - Act16\n\t17 - Act17\n\t18 - Act18\n\t19 - Act19\n\t20 - Act20\n\t21 - Act21\n\t0 - Close")
                            print("\n====================================")
                            choice = eval(input("What program/code would you like to run? -->"))
                            os.system('cls')
                            from third_file import *

                            if choice == 15:
                                activity15()
                                continue
                            elif choice == 16:
                                activity16()
                                continue
                            elif choice == 17:
                                activity17()
                                continue
                            elif choice == 18:
                                activity18()
                                continue
                            elif choice == 19:
                                activity19()
                                continue
                            elif choice == 20:
                                activity20()
                                continue
                            elif choice == 21:
                                activity21()
                                continue
                            elif choice == 0:
                                print("Close")
                                break
                            else:
                                print("Invalid Choice, Please pick again")
                            continue
                    # activity 22 - 28
                    elif choose == 'd':
                        while True:
                            print("\nSelect an Activity you'd like to Open")
                            print("Choose a number from the options")
                            print("====================================")
                            print("\n\t22 - Act22\n\t23 - Act23\n\t24 - Act24\n\t25 - Act25\n\t26 - Act26\n\t27 - Act27\n\t28 - Act28\n\t0 - Close")
                            print("\n====================================")
                            choice = eval(input("What program/code would you like to run? -->"))
                            os.system('cls')
                            from fourth_file import *

                            if choice == 22:
                                activity22()
                                continue
                            elif choice == 23:
                                print("\tOUTPUT")
                                print("============================")
                                activity23()
                                continue
                            elif choice == 24:
                                print("\tOUTPUT")
                                print("============================")
                                activity24()
                                continue
                            elif choice == 25:
                                print("\tOUTPUT")
                                print("============================")
                                activity25()
                                continue
                            elif choice == 26:
                                print("\tOUTPUT")
                                print("============================")
                                activity26()
                                continue
                            elif choice == 27:
                                print("\tOUTPUT")
                                print("============================")
                                activity27()
                                continue
                            elif choice == 28:
                                activity28()
                                continue
                            elif choice == 0:
                                print("Close")
                                break
                            else:
                                print("Invalid Choice, Please pick again")
                            continue

                    elif choose == 'e':
                        print("Exiting the Folder")
                        break
                    else:
                        print("Invalid Choice, Please pick again")
                        continue
            elif two == 'c':
                while True:
                    print("====================================")
                    print("Choose the folder of Code Challenge you like to Open")
                    print("\n\tZ - Code_Challenge(1-8)\n\tY - Code_Challenge(9-16)\n\tE - Exit")
                    print("\n====================================")
                    choose = input("\nWhat folder would you like to run --> ").lower()
                    os.system('cls')

                    if choose == 'z':
                        while True:
                            print("Select a Code challenge you'd like to Open")
                            print("\n====================================")
                            print("\n\tC1 - Code_Challenge1\n\tC2 - Code_Challenge2\n\tC3 - Code_Challenge3\n\tC4 - Code_Challenge4")
                            print("\tC5 - Code_Challenge5\n\tC6 - Code_Challenge6\n\tC7 - Code_Challenge7\n\tC8 - Code_Challenge8")
                            print("\tE - Close")
                            print("\n====================================")
                            choice = input("What program/code would you like to run? -->").lower()
                            os.system('cls')

                            if choice == 'c1':
                                print("\tOUTPUT")
                                print("============================")
                                code_challenge1()
                                continue
                            elif choice == 'c2':
                                print("\tOUTPUT")
                                print("============================")
                                code_challenge2()
                                continue
                            elif choice == 'c3':
                                print("\tOUTPUT")
                                print("============================")
                                code_challenge3()
                                continue
                            elif choice == 'c4':
                                print("\tOUTPUT")
                                print("============================")
                                code_challenge4()
                                continue
                            elif choice == 'c5':
                                print("\tOUTPUT")
                                print("============================")
                                code_challenge5()
                                continue
                            elif choice == 'c6':
                                print("\tOUTPUT")
                                print("============================")
                                code_challenge6()
                                continue
                            elif choice == 'c7':
                                print("\tOUTPUT")
                                print("============================")
                                code_challenge7()
                                continue
                            elif choice == 'c8':
                                print("\tOUTPUT")
                                print("============================")
                                code_challenge8()
                                continue
                            elif choice == 'e':
                                print("Close")
                                break
                            else:
                                print("Invalid Choice, Please pick again")
                                continue
                    elif choose == 'y':
                        while True:
                            print("Select a Code challenge you'd like to Open")
                            print("\n====================================")
                            print("\n\tC9 - Code_Challenge9\n\tC10 - Code_Challenge10\n\tC11 - Code_Challenge11\n\tC12 - Code_Challenge12")
                            print("\tC13 - Code_Challenge13\n\tC14 - Code_Challenge14\n\tC15 - Code_Challenge15\n\tC16 - Code_Challenge16")
                            print("\tE - Close")
                            print("\n====================================")
                            choice = input("What program/code would you like to run? -->").lower()
                            os.system('cls')

                            if choice == 'c9':
                                print("\tOUTPUT")
                                print("============================")
                                code_challenge9()
                                continue
                            elif choice == 'c10':
                                print("\tOUTPUT")
                                print("============================")
                                code_challenge10()
                                continue
                            elif choice == 'c11':
                                print("\tOUTPUT")
                                print("============================")
                                code_challenge11()
                                continue
                            elif choice == 'c12':
                                print("\tOUTPUT")
                                print("============================")
                                code_challenge12()
                                continue
                            elif choice == 'c13':
                                print("\tOUTPUT")
                                print("============================")
                                code_challenge13()
                                continue
                            elif choice == 'c14':
                                print("\tOUTPUT")
                                print("============================")
                                code_challenge14()
                                continue
                            elif choice == 'c15':
                                print("\tOUTPUT")
                                print("============================")
                                code_challenge15()
                                continue
                            elif choice == 'c16':
                                print("\tOUTPUT")
                                print("============================")
                                code_challenge16()
                                continue
                            elif choice == 'e':
                                print("Close")
                                break
                            else:
                                print("Invalid Choice, Please pick again")
                                continue
                    elif choose == 'e':
                        print("Exiting the folder...")
                        break
                    else:
                        print("Invalid Choice, Please pick again")
                        continue

            elif two == 'd':
                while True:
                    print("\n============================================")
                    print("\n\t   DEFINITION")
                    print("\n============================================")
                    print("\nThis Folder is about the definition you can know in PYTHON")
                    print("\n\t1 - BuiltIn Function\n\t2 - User-Defined Functions\n\t3 - Operators\n\t4 - Statements\n\t5 - Exit")
                    print("\n============================================")
                    print("\nPlease pick a number in the options")
                    func = input("\nWhat would you like to know about? -->")
                    os.system('cls')

                    if func == '1':
                        while True:
                            print("These are some of the BuiltIn Functions")
                            print("\n===================================")
                            print("\n\t1 - print()\n\t2 - input()\n\t3 - eval()\n\t4 - int()\n\t5 - str()\n\t6 - bool()")
                            print("\t7 - dict()\n\t8 - list()\n\t9 - float()\n\t10 - len()\n\t11 - range()\n\t12 - Exit")
                            print("\n===================================")
                            print("What would you like to know about?")
                            cm = input("Pick one from the options above -->")
                            os.system('cls')

                            if cm == '1':
                                print("\tDEFINITION")
                                print("\n============================================")
                                print("The print() function prints the specified message to the screen, or other standard output device.")
                                print("\n============================================")
                                continue
                            elif cm == '2':
                                print("\tDEFINITION")
                                print("\n============================================")
                                print("The input() function allows user input.")
                                print("\n============================================")
                                continue
                            elif cm == '3':
                                print("\tDEFINITION")
                                print("\n============================================")
                                print("The eval() function evaluates the specified expression, \nif the expression is a legal Python statement, it will be executed.")
                                print("\n============================================")
                                continue
                            elif cm == '4':
                                print("\tDEFINITION")
                                print("\n============================================")
                                print("The int() function converts the specified value into an integer number.")
                                print("\n============================================")
                                continue
                            elif cm == '5':
                                print("\tDEFINITION")
                                print("\n============================================")
                                print("The str() function converts the specified value into a string.")
                                print("\n============================================")
                                continue
                            elif cm == '6':
                                print("\tDEFINITION")
                                print("\n============================================")
                                print("Booleans represent one of two values: True or False.")
                                print("\n============================================")
                                continue
                            elif cm == '7':
                                print("\tDEFINITION")
                                print("\n============================================")
                                print("Dictionaries are used to store data values in key:value pairs."
                                    "\nA dictionary is a collection which is ordered*, changeable and do not allow duplicates."
                                    "\nDictionary are created using curly brackets{}")
                                print("\n============================================")
                                continue
                            elif cm == '8':
                                print("\tDEFINITION")
                                print("\n============================================")
                                print("Lists are used to store multiple items in a single variable."
                                    "\nLists are created using square brackets[]")
                                print("\n============================================")
                                continue
                            elif cm == '9':
                                print("\tDEFINITION")
                                print("\n============================================")
                                print("The float() function converts the specified value into a floating point number.")
                                print("\n============================================")
                                continue
                            elif cm == '10':
                                print("\tDEFINITION")
                                print("\n============================================")
                                print("The len() function returns the number of items in an object."
                                    "\nWhen the object is a string, the len() function returns the number of characters in the string.")
                                print("\n============================================")
                                continue
                            elif cm == '11':
                                print("\tDEFINITION")
                                print("\n============================================")
                                print("The range() function returns a sequence of numbers, starting from 0 by default,"
                                      "\nand increments by 1 (by default), and stops before a specified number.")
                                print("\n============================================")
                                continue
                            elif cm == '12':
                                print("You chose exit")
                                print("Exiting....")
                                break
                            else:
                                print("Invalid Choice")
                                continue

                    elif func == '2':
                        print("\tDEFINITION")
                        print("\n============================================")
                        print("\n\tThe User-Defined Function")
                        print("\n============================================")
                        print("A User-Defined Function (UDF) is a function created by the user to perform specific tasks in a program."
                            "\nUnlike built-in functions provided by a programming language, UDFs allow for customization and code reusability, "
                            "\nimproving program structure and efficiency.")
                        continue

                    elif func == '3':
                        while True:
                            print("\n==================================")
                            print("\n\tOPERATORS")
                            print("\n==================================")
                            print("\n\t1 - Arithmetic\n\t2 - Logical\n\t3 - Assignment\n\t4 - Comparison\n\t5 - Exit")
                            print("\n==================================")
                            op = input("What would you like to choose? -->")
                            os.system('cls')

                            if op == '1':
                                print("\n==========================================")
                                print("\n\tArithmetic")
                                print("\n==========================================")
                                print("Arithmetic operators are used with numeric values to perform common mathematical operations:")
                                print("Such as addition '+', subtraction '-', multiplication '*', division '/'"
                                    "\nmodulos '%', exponentiation '**', floor division '//'"
                                    )
                                continue
                            elif op == '2':
                                print("\n==========================================")
                                print("\n\tLogical")
                                print("\n==========================================")
                                print("Logical operators are used to combine conditional statements:")
                                print("'and' Returns True if both statements are true")
                                print("'or'	Returns True if one of the statements is true")
                                print("'not' Reverse the result, returns False if the result is true")
                                continue
                            elif op == '3':
                                print("\n==========================================")
                                print("\n\tAssignment")
                                print("\n==========================================")
                                print("Assignment operators are used to assign values to variables")
                                print("It's examples are: \n\t=\n\t+=\n\t-=\n\t/=\n\t*=\n\t%=\n\t//=")
                                continue
                            elif op == '4':
                                print("\n==========================================")
                                print("\n\tComparison")
                                print("\n==========================================")
                                print("Comparison operators are used to compare two values")
                                print("It's examples are: \n\t== equal\n\t!= not equal\n\t> greater than\n\t< less than\n\t>= greater than or equal to\n\t<= less than or equal to")
                                continue
                            elif op == '5':
                                print("Exit")
                                break
                            else:
                                print("Invalid choice")
                                continue

                    elif func == '4':
                        while True:
                            print("==============================================")
                            print("\n\tSTATEMENTS")
                            print("\n==============================================")
                            print("\n\t1 - Conditional Statements\n\t2 - Loop Statements\n\t3 - Exit")
                            print("\n==============================================")
                            ss = input("Pick a number in the options ")
                            os.system('cls')

                            if ss == '1':
                                print("==============================================")
                                print("\tThe conditional statements are:")
                                print("\nAn 'if statement' is written by using the if keyword. ")
                                print("The elif keyword is Python's way of saying 'if the previous conditions were not true, then try this condition'.")
                                print("The else keyword catches anything which isn't caught by the preceding conditions.")
                                print("You can have if statements inside if statements. This is called nested if statements.")
                                
                                continue
                            elif ss == '2':
                                print("==============================================")
                                print("\tThe Loop statements are:")
                                print("\n\tFOR LOOP and WHILE LOOP")
                                print("A for loop is used for iterating over a sequence \n(that is either a list, a tuple, a dictionary, a set, or a string)."
                                      "\nWith the for loop we can execute a set of statements, \nonce for each item in a list, tuple, set etc."
                                    )
                                print("With the while loop we can execute a set of statements as long as a condition is true.")
                                continue
                            elif ss == '3':
                                print("Exiting...")
                                break
                            else:
                                print("Invalid Choice")
                                continue

                    elif func == '5':
                        print("Exiting the Definition...")
                        break

                    else:
                        print("Invalid Choice")
                        print("Please Pick Again")
                        continue

            elif two == 'e':
                print("Exiting the Folder....")
                break            
            else:
                print("INVALID CHOICE, PLEASE PICK AGAIN")
    elif door == 's':
        print("Program Closed")
        print("\t----------------------------------"
              "\n\t|THANK YOU FOR USING MY PROGRAM!!|"
              "\n\t----------------------------------"
              )
        break
    else:
        print("Invalid Choice!")
        continue