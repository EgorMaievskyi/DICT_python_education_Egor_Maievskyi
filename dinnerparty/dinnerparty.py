import random
friends = {}
name_input = None
number = 0
try:
    number = int(input("Enter the number of friends joining (including you):\n >"))
except ValueError:
    exit("No one is joining for the party")
if number <= 0:
    exit("No one is joining for the party")

for key in range(int(number)):
    name_input = input("Enter the name of every friend (including you),each on a new line:\n >")
    friends.setdefault(name_input, 0)

print(friends)