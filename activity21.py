#while loop

isClean = True

while isClean == True:
    ask = input("are the clothes clean already (y/n)? --->")

    if ask.lower() == 'y':
        print("Loop continues")
        continue
    else:
        print("Loop stops")
        break