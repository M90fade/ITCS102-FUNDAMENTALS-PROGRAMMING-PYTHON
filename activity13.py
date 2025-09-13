#using for loop, ask the user to input 10 numbers
#after input, get the summation of all the numbers

num = 0
for m in range(1, 11, 1):
    numbers = eval(input("Enter a number"))
    num += numbers
    print("The new value is", num)
    
print("The final value is", num)