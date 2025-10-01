#diamond
for z in range(1, 4, 1):
    for m in range(1, 8, 1):
        print(" ", end=" ")
    for y in range(3, z, -1):
        print(" ", end=" ")
    for x in range(1, z, 1):
        print("*", end=" ")
    for v in range(0, z):
        print("*", end=" ")
    print()
for u in range(1, 3, 1):
    for n in range(1, 8, 1):
        print(" ", end=" ")
    for w in range(0, u, 1):
        print(" ", end=" ")
    for t in range(2, u, -1):
        print("*", end=" ")
    for s in range(3, u, -1):
        print("*", end=" ")
    print()
#the body
for a in range(1, 7, 1):
    for j in range(1, 5, 1):
        print(" ", end=" ")
    for b in range(6, a, -1):
        print(" ", end=" ")
    for c in range(1, a, 1):
        print("*", end=" ")
    for d in range(0, a, 1):
        print("*", end=" ")
    print()
for e in range(1, 9, 1):
    for r in range(1, 3, 1):
        print(" ", end=" ")
    for b in range(8, e, -1):
        print(" ", end=" ")
    for c in range(1, e, 1):
        print("*", end=" ")
    for d in range(0, e, 1):
        print("*", end=" ")
    print()
for q in range(1, 11, 1):
    for b in range(10, q, -1):
        print(" ", end=" ")
    for c in range(1, q, 1):
        print("*", end=" ")
    for d in range(0, q, 1):
        print("*", end=" ")
    print()
#stem
for l in range(1, 6, 1):
    for h in range(1, 8, 1):
        print(" ", end=" ")
    for k in range(1, 6, 1):
        print("*", end=" ")
    print()

