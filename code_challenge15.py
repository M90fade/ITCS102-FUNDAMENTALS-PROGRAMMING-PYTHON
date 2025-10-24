#create an anime compiler 

anime = True
zoro = []
while anime == True:
    title = input("Enter the title of an anime (or type 'close' to finish): ")
    if title.lower() == 'close':
        print("You have exited the anime entry program.")
        break
    else:
        zoro.append(title)
        print(f"'{title}' has been added to your anime list")
        continue

print("Your anime list includes:")
for title in zoro:
    print(f"- {title}")

