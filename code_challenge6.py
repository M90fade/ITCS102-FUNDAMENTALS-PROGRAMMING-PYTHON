print("Factorial Program")

num = eval(input("Enter a number --> "))

result = 1
for haha in range(num, 0, -1):
        result *= haha
        #print(result)

print("The Factorial of", str(num) +"! is", result)