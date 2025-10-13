#multiplication table
# col = eval(input("Enter a number of columns-->"))
# print(f"The number of columns:{col}")

# #rows
# for i in range(1, 11, 1):
#     for z in range(1, col+1, 1):
#         print(f"{z} x {i} = {i*z}", end=" \t")
#     print()

#pyramid
for a in range(1, 7, 1):
    for b in range(6, a, -1):
        print(" ", end=" ")
    for c in range(1, a, 1):
        print(" * ", end=" ")
    print()