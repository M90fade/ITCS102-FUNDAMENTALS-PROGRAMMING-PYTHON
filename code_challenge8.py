#create a program that prints the of a number entered by the user, using a simple for loop.
# Format each line clearly (e.g., 5 x 1  = 5).
# looping a fixed ranged(1, 11)

print("MULTIPLICATION TABLE MAKER")

mult = eval(input("Enter a number: "))
print("\nMultiplication table for", str(mult) +":")

for xin in range(1, 11):
    times = mult * xin
    print(mult, "x", xin, "=", times)