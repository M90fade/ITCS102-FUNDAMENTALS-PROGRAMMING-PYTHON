#create a manga recommendation

print("Welcome to the Manga Reader Recommender!! ")
print("Answer a few questions to find your next read.")

genre = input("What genre do you like? (action, horror, romance, comedy): ")
dura = input("How long should the manga be? (short, medium, long): ")
year = eval(input("Which decade do you want? (1990s, 2000s, 2010s, 2020s): "))

if genre == 'action':
	if dura == 'short':
		if year == 1990:
			print("This are some of the manga recommendation we have for you: \n1. Shaman King \n2. Inuyasha \n3. Hajime no Ippo \n4. Samurai X")
if genre == 'action':
	if dura == 'short':
		if year == 2000:
			print("This are some of the manga recommendation we have for you: \n1. Black Butler \n2. Terror and Resonance")
if genre == 'action':
	if dura == 'short':
		if year == 2010:
			print("This are some of the manga recommendation we have for you: \n1. Tokyo Ghoul \n2. Dororo \n3. Beelzebub")
if genre == 'action':
	if dura == 'medium':
		if year == 1990:
			print("This are some of the manga recommendation we have for you: \n1. Slam Dunk \n2. HunterXHunter \n3. YuYu Hakusho")
if genre == 'action':
	if dura == 'medium':
		if year == 2000:
			print("This are some of the manga recommendation we have for you: \n1. Berserk \n2. Digimon Adventure \n3. Naruto \n4. Bleach \n5. FullMetal Alchemist")
if genre == 'action':
	if dura == 'medium':
		if year == 2010:
			print("This are some of the manga recommendation we have for you: \n1. My Hero Academia \n2. Assasination Classroom \n3. JoJo's Bizarre Adventure \n4. Sword Art Online \n5. FairyTail \n6. OnePunch Man")
if genre == 'action':
	if dura == 'medium':
		if year == 2020:
			print("This are some of the manga recommendation we have for you: \n1. Frieren \n2. Spy Family \n3. Chainsaw Man \n4. Demon Slayer \n5. Mashle: Magic and Muscles")
if genre == 'action':
	if dura == 'long':
		if year == 1990:
			print("This are some of the manga recommendation we have for you: \n1. DragonBall \n2. Detective Conan \n3. OnePiece \n4. Pokemon")

if genre == 'horror':
	if dura == 'short':
		if year == 2020:
			print("This are some of the manga recommendation we have for you: \n1. Jujutsu Kaisen \n2. Dandadan")
if genre == 'romance':
	if dura == 'short':
		if year == 2000:
			print("This are some of the manga recommendation we have for you: \n1. From me to you \n2. NANA \n3. Inuyasha \n4. Daa! Daa! Daa!")

if genre == 'romance':
	if dura == 'short':
		if year == 2010:
			print("This are some of the manga recommendation we have for you: \n1. Nisekoi \n2. Horimiya \n3. Maid Sama \n4. Darling In The Franxx")
if genre == 'romance':
	if dura == 'short':
		if year == 2020:
			print("This are some of the manga recommendation we have for you: \n1. Rent a girlfriend \n2. A whisker away \n3. The Fragrant Blooms with Dignity \n4. My Dress Up Darling \n5. My Apothecary Diaries \n6. Kaguya sama Love is War \n7. Komi Can't Communicate")


if genre == 'comedy':
	if dura == 'medium':
		if year == 1990:
			print("This are some of the manga recommendation we have for you: \n1. Gintama \n2. Doraemon")
if genre == 'comedy':
	if dura == 'medium':
		if year == 2010:
			print("This are some of the manga recommendation we have for you: \n1. Saiki K \n2. Slam Dunk \n3. KONOSUBA \n4. Food Wars \n5. Buddy Daddies \n6. Haikyu")
if genre == 'comedy':
	if dura == 'medium':
		if year == 2020:
			print("This are some of the manga recommendation we have for you: \n1. Spy X Family")
if genre == 'comedy':
	if dura == 'long':
		if year == 1990:
			print("This are some of the manga recommendation we have for you: \n1. OnePiece \n2. DragonBall \n3. Bleach \n4. Pokemon")

else:
	print("Sorry, there is no", dura, genre, "manga from the", str(year) + "s in our list")









