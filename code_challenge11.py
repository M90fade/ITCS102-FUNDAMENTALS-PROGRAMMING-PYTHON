

for z in range(1, 12, 1):
    for y in range(11, z, -1):
        print(" ", end=" ")
    for x in range(1, z, 1):
        print("*", end=" ")
    for v in range(0, z, 1):
        print("*", end=" ")
    print()
for u in range(1, 11, 1):
    for w in range(0, u, 1):
        print(" ", end=" ")
    for t in range(10, u, -1):
        print("*", end=" ")
    for s in range(11, u, -1):
        print("*", end=" ")
    print()
