#String Formatting

n1 = 'Moses'
n2 = 'Doctor'
n3 = 'Faderagao'

print(f"Hello {n1} {n2} {n3}, to the World")

me = 0

for you in range(1, 11, 1):
    ma = eval(input(f"{you} - Enter a number --> "))

    if ma % 2 == 1:
        me += ma


print(f"The total of odd number is: {me}")


