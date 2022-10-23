import random
print("HANGMAN\n The game will be available soon.")
wrong = 0
wrong_max = 8
words = ["jawa", "python" , "cash" , "opinion"]
word = random.choice(words)
used = []
so_far = "-" * len(word)
print(so_far)
print("Hangman \n Guess the word")
while wrong < wrong_max and so_far != word:
    print("Attempts :" ,wrong)
    lett = input("Input a letter>")

    while lett in used:
        print("You've already guessed this letter")
        lett = input("\n\nInput a letter: ")
        used.append(lett)
    if lett in word:
        new = ""
        for i in range(len(word)):
            if lett == word[i]:
                new += lett
            else:
                new += so_far[i]
        so_far = new
        print(so_far)
    else:
        wrong += 1
        print("That letter doesn't appear in the word")

if wrong == wrong_max:
    print("You dead!")
else:
    print("You survived!")


