import random
from time import time
from dico import DICO

random.seed(time())

def get_input_player(toto):
  inp = raw_input("Choose a letter (not in %s)" % toto)
  letter = inp[0].strip()
  if letter == '':
    print("Please choose a letter")
    return get_input_player()
  toto+= letter
  return letter

def is_in_word(word, letter):
  if letter in word:
    print("We have to print all %s" % letter)
    return True
  return False

def loop_game(word):
  tried = []
  buffer = ["_",] * len(word)
  play = True
  lives = 9
  print("You got %s lives" % lives)
  while play:
    print("My Animation |")
    print("My Animation /")
    inp = get_input_player(tried)
    if is_in_word(word, inp):
      for i in range(len(word)):
        print(i, word[i], inp)
        if word[i] == inp:
          buffer[i] = inp
      # Find all positions for this letter 
      # replace all position with the letter
    else:
        lives -= 1 
    print(play, ' num of lives', lives)
    print("Already tried %s" % tried)
    print("Current Word: [%s]" % "".join(buffer))
    play = lives > 0
    if not "_" in buffer:
      play = False
  if lives < 0:
    print("You lost sorry")
    print("Word to find was %s" % word)
  else:
    print("Yeah good job you find with still %s lives !" % lives)

 
def select_random_word():
  return DICO[random.randint(0, len(DICO) - 1)]

def main():
  word = select_random_word() # Preparation du jeu
  word = word.lower()
  loop_game(word) # Lancement du jeu

if __name__ == '__main__':
  main()
