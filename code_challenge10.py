
print("\t\t *", end=" ")

for z in range(1, 11, 1):
    for y in range(10, z, -1):
        print(" ", end=" ")
    for x in range(1, z, 1):
        print("*", end=" ")
    for v in range(1, z, 1):
        print("*", end=" ")
    print()
