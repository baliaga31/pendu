import random, curses
import time
from dico import DICO

stdscr = curses.initscr()
stdscr.nodelay(True)
random.seed(time.time())

def get_input_player(tried):
  inp = stdscr.getch()
  if inp == -1:
    return None
  if chr(inp) in tried:
    return get_input_player(tried)
  return chr(inp)

def is_in_word(word, letter):
  if letter in word:
    return True
  return False

def turn(word, tried, buffer, lives):
  play = True
  inp = get_input_player(tried)
  if inp is None:
    return play, lives
  tried.append(inp)
  if is_in_word(word, inp):
    for i in range(len(word)):
      if word[i] == inp:
        buffer[i] = inp
  else:
    lives -= 1 
  play = lives > 0
  if not "_" in buffer or lives <= 0:
    play = False
  return play, lives
    

def print_data(buffer, lives, tried):
  stdscr.addstr("Player: ")
  stdscr.addstr("%s lives\n" % lives, curses.A_UNDERLINE)
  stdscr.addstr("%s\n" % buffer)
  stdscr.addstr("Tried Letters: %s\n" %tried)

def print_endgame(word, win=False):
  if win:
    stdscr.addstr("You Won ! Good Job !")
  else:
    stdscr.addstr("You Lost ! Sorry.")
  stdscr.addstr("The Word was ")
  stdscr.addstr(word, curses.A_UNDERLINE)
  while None == get_input_player([]):
    time.sleep(0.1)

def loop_game(word):
  tried = []
  buffer = ["_",] * len(word)
  lives = 9
  play = True
  while play:
    # clean screen
    stdscr.clear()
    # print on screen
    print_data(buffer, lives, tried)
    stdscr.refresh()
    # do game loop
    play, lives = turn(word, tried, buffer, lives)
    # wait 0.1ms
    time.sleep(0.1)
  print_endgame(word, lives >= 0)
 
def select_random_word():
  return DICO[random.randint(0, len(DICO) - 1)]


def main():
  curses.noecho()
  curses.cbreak()

  word = select_random_word() # Preparation du jeu
  word = word.lower()
  loop_game(word) # Lancement du jeu
  curses.endwin()

if __name__ == '__main__':
  main()
