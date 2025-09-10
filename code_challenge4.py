print ("Welcome to the manga Reader Recommender!")

print ("Let me ask some question so I can recommend the exact Manga you need!")

genre = input ("What genre do you like to read? (action, romance, horror): ")

duration = input("How long should the Manga be? (short, medium, long): ")

if genre == "romance" and duration == "long":
	print("I recommend you Boys Over Flowers!")

if genre == "romance" and duration == "medium" :
	print("I recommend you Dengeki Daisy!")

if genre == "romance" and duration == "short":
	print("I recommend you Paradise Kiss!")

if genre == "romance" and duration == "long":
	print("I recommend you A Silent Voice!")

if genre == "romance" and duration == "medium":
	print("I recommend you Orange!")


if genre == "romance" and duration == "short":
	print("I recommend you I Want to Eat Your Pancreas!")


if genre == "horror" and duration == "long":
	print("I recommend you My Dress-Up Darling!")


if genre == "horror" and duration == "medium":
	print("I recommend you Yamada Tarou Monogatari!")


if genre == "horror" and duration == "short":
	print("I recommend you Tomo-chan Is a Girl!")
