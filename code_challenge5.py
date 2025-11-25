#create a manga recommendation

print("Welcome to the Manga Reader Recommender!! ")
print("Answer a few questions to find your next read.")

genre = input("What genre do you like? (action, horror, romance, comedy): ")
dura = input("How long should the manga be? (short, medium, long): ")
year = eval(input("Which decade do you want? (1990s, 2000s, 2010s, 2020s): "))

if genre.lower() == 'action':
	if dura == 'short' and year == 1990:
			print("This are some of the manga recommendation we have for you: \n1. Shaman King \n2. Inuyasha \n3. Hajime no Ippo \n4. Samurai X")
	elif dura == 'short' and year == 2000:
			print("This are some of the manga recommendation we have for you: \n1. Black Butler \n2. Terror and Resonance")
	elif dura == 'short' and year == 2010:
			print("This are some of the manga recommendation we have for you: \n1. Tokyo Ghoul \n2. Dororo \n3. Beelzebub")
	elif dura == 'medium' and year == 1990:
			print("This are some of the manga recommendation we have for you: \n1. Slam Dunk \n2. HunterXHunter \n3. YuYu Hakusho")
	elif dura == 'medium' and year == 2000:
			print("This are some of the manga recommendation we have for you: \n1. Berserk \n2. Digimon Adventure \n3. Naruto \n4. Bleach \n5. FullMetal Alchemist")
	elif dura == 'medium' and year == 2010:
			print("This are some of the manga recommendation we have for you: \n1. My Hero Academia \n2. Assasination Classroom \n3. JoJo's Bizarre Adventure \n4. Sword Art Online \n5. FairyTail \n6. OnePunch Man")
	elif dura == 'medium' and year == 2020:
			print("This are some of the manga recommendation we have for you: \n1. Frieren \n2. Spy Family \n3. Chainsaw Man \n4. Demon Slayer \n5. Mashle: Magic and Muscles")
	elif dura == 'long' and year == 1990:
			print("This are some of the manga recommendation we have for you: \n1. DragonBall \n2. Detective Conan \n3. OnePiece \n4. Pokemon")
	else:
		print("Sorry, there is no", dura, genre, "manga from the", str(year) + "s in our list")

elif genre.lower() == 'horror':
	if dura == 'short' and year == 2020:
			print("This are some of the manga recommendation we have for you: \n1. Jujutsu Kaisen \n2. Dandadan")
	else:
		print("Sorry, there is no", dura, genre, "manga from the", str(year) + "s in our list")

elif genre.lower() == 'romance':
	if dura == 'short' and year == 2000:
			print("This are some of the manga recommendation we have for you: \n1. From me to you \n2. NANA \n3. Inuyasha \n4. Daa! Daa! Daa!")
	elif dura == 'short' and year == 2010:
			print("This are some of the manga recommendation we have for you: \n1. Nisekoi \n2. Horimiya \n3. Maid Sama \n4. Darling In The Franxx")
	elif dura == 'short' and year == 2020:
			print("This are some of the manga recommendation we have for you: \n1. Rent a girlfriend \n2. A whisker away \n3. The Fragrant Blooms with Dignity \n4. My Dress Up Darling \n5. My Apothecary Diaries \n6. Kaguya sama Love is War \n7. Komi Can't Communicate")
	else:
		print("Sorry, there is no", dura, genre, "manga from the", str(year) + "s in our list")


elif genre.lower() == 'comedy':
	if dura == 'medium' and year == 1990:
			print("This are some of the manga recommendation we have for you: \n1. Gintama \n2. Doraemon")
	elif dura == 'medium' and year == 2010:
			print("This are some of the manga recommendation we have for you: \n1. Saiki K \n2. Slam Dunk \n3. KONOSUBA \n4. Food Wars \n5. Buddy Daddies \n6. Haikyu")
	elif dura == 'medium' and year == 2020:
			print("This are some of the manga recommendation we have for you: \n1. Spy X Family")
	elif dura == 'long' and year == 1990:
			print("This are some of the manga recommendation we have for you: \n1. OnePiece \n2. DragonBall \n3. Bleach \n4. Pokemon")
	else:
		print("Sorry, there is no", dura, genre, "manga from the", str(year) + "s in our list")
else:
		print("Sorry, you put", dura, genre, "manga from the", str(year) + "s is invalid")