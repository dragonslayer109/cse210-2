
# file = open("Week5/Jumper Incompete/Text/Parachute.txt", "r")
# parachute = file.readlines()

# print(parachute)

# import random
# with open("Week5/Jumper Incompete/Text/Words.txt", "r") as file:
#     text = file.read()
#     words = list(map(str, text.split()))
#     random_word = random.choice(words)
#     print(random_word)
    

file = open("Week5/Jumper Incompete/Text/Parachute.txt", "r")
parachute = file.readlines()
lives = 4

#parachute = ["  ___", "/ ___ \ ", "\     /", " \   /", "   O", "  /|\ ", "  / \ ", "⌃⌃⌃⌃⌃⌃⌃"]
if lives == 4:
    for x in range(4-lives, len(parachute)):
        print(parachute[x])

elif lives == 3:
    for x in range(4-lives, len(parachute)):
        print(parachute[x])

elif lives == 2:
    for x in range(4-lives, len(parachute)):
        print(parachute[x])

elif lives == 1:
    for x in range(4-lives, len(parachute)):
        print(parachute[x])

elif lives == 0:
    for x in range(4-lives, len(parachute)):
        print(parachute[x])