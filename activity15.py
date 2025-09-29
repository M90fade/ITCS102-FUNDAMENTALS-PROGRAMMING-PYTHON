#String Formatting

n1 = 'Moses'
n2 = 'Doctor'
n3 = 'Faderagao'

print(f"Hello {n1} {n2} {n3}, to the World")

mi = 0

for mae in range(1, 11, 1):
    ma = eval(input(f"{mae} - Enter a number --> "))

    if mae % 2 == 1:
        mi += mae


print(f"The total of odd number is: {mi}")
