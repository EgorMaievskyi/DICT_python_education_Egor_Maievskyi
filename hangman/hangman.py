import random
print("HANGMAN\n The game will be available soon.")
words = ["jawa", "python" , "cash" , "opinion"]
word = random.choice(words)
so_far = "-" * len(word)
print(word[:3] + so_far[:-3])
print("Hangman \n Guess the word")
a = input(">")
if a == word:
    print("You survived")
else:
    print("You lost")
