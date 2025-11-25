# enter 10 numbers, determine if odd or even, and find the summation of odd numbers
# must use for loop

result = 0

for me in range(1, 11):
    odd_num = eval(input("Enter a number --> "))

    if odd_num % 2 == 0:
        print(odd_num, "even")
    else:
        print(odd_num, "is odd")
        result += odd_num
        
print("The summation of all odd numbers is:", result)      


