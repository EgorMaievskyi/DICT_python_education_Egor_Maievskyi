import random
print("HANGMAN\n The game will be available soon.")
wrong = 0
wrong_max = 8
words = ["jawa", "python" , "cash" , "opinion"]
word = random.choice(words)
so_far = "-" * len(word)
print(so_far)
print("Hangman \n Guess the word")
 while wrong < wrong_max and so_far != word:
a = input("Input a letter>")
  while a in used:
      wrong += 1
      print("No improvements")
      a = input("Input a letter>")

      if a in word:
          new = ""



