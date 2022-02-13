from Game.secret import Secret 
from Game.director import Director
from Game.jumper import Jumper

class Player:
    "This class is for for every correct guess of the player"

    def __init__(self):
        self._lives = 4
        self._director = Director()
        self._secret = Secret()

    def display(self):
        guess_letter = self._director.get_prompt(self)
        secret_word = self._secret.get_word(self)
        underscore = "_"*len(secret_word)
        underscore = list(underscore)
        for k in range(0, len(secret_word)):
            if guess_letter == secret_word[k]:
                underscore[k] = guess_letter
        ",".join(underscore)

        print(*underscore)


