from string import ascii_lowercase
import sys, os

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'

try:
    input = raw_input
except NameError:
    pass

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Hangman(object):
    def __init__(self, word):
        self.keylist = ASCII[:]
        self.word = word
        self.lowercase = word.lower()
        self.guseedlet = []
        self.guessedword = []
        for x in word:
            if x.lower() in self.keylist:
                self.guessedword.append('_')
            else:
                self.guessedword.append(x)
        self.the_game()

    def the_game(self):
        youwin = False
        for hang in HANG_GRAPHICS:
            while 1:
                clear()
                if '_' not in self.guessedword:
                    print('You guest it, way to go')
                    return 0
                print(' '.join(self.keylist))
                print(hang)
                print(''.join(self.guessedword))
                guess = input('Enter a letter')
                guess = guess.lower()
                if guess in self.guseedlet or guess not in ASCII:
                    # all ready guessed it
                    pass
                elif guess not in self.lowercase:
                    self.guseedlet.append(guess)
                    self.keylist[self.keylist.index(guess)] = '_'
                    break
                else:
                    self.guseedlet.append(guess)
                    self.keylist[self.keylist.index(guess)] = '_'
                    self.lowercase.replace(guess, '_')
                    for i, w in enumerate(word):
                        if w.lower() == guess:
                            self.guessedword[i] = w

        print('You lost, better luck next time')
        print('The answer was: {}'.format(self.word))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()
    Hangman(word)
