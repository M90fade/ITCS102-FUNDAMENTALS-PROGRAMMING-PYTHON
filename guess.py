#guessing game
import random
print("Guess the number")

hula = random.randint(1, 20)
ans = True
tries = 0

while ans == True:
    num = int(input("Enter a number: "))
    tries += 1
    if num == hula:
        print("Your guess is correct")
        print("Congratulations!!")
        print(f"only took {tries} tries")
        break
    else:
        print("Wrong guess")
        print("Try Again")
        continue