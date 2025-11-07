# enter 10 numbers, determine if odd or even, and find the summation of odd numbers
# must use for loop

result = 0

for arf in range(1, 11):
    bers = eval(input("Enter a number --> "))

    if bers % 2 == 0:
        print(bers, "even")
    else:
        print(bers, "is odd")
        result += bers
        
print("The summation of all odd numbers is:", result)      

