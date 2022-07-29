#python game using pygame following a tutorial but adding my own twist
import pygame
import math
import random

#initalize pygame and the dimension of the game window
pygame.init()
WIDTH, HEIGHT = 1280, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")


#loading images 
images = []
for i in range(7):
  image = pygame.image.load("hangman" + str(i) + ".png")
  images.append(image)

print(images)
#================setting up game loop=======================

#variables for hangman game
attempt_count = 0
words = ["WORLD", "APPROACH", "ZOMBIE", "CRAVINGS", "JEALOUS"]
#randomly selects a word from the list
word = random.choice(words) 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
guessed_letters = []

#fonts
LETTER_FONT = pygame.font.SysFont('impact', 40)
WORD_FONT = pygame.font.SysFont("impact", 60)
TITLE_FONT = pygame.font.SysFont("impact", 80)

#button variables
RADIUS = 30
GAP = 20
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 600
A = 65

for i in range(26):
  x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
  y = starty + ((i //13) * (GAP + RADIUS * 2))
  letters.append([x, y, chr(A + i), True])

#function to draw the buttons on the window for the hangman game
def draw():
  #setting background to white and update the display
  window.fill(WHITE)

  #draw title
  text = TITLE_FONT.render("Hangman Game", 1, BLACK)
  window.blit(text, (WIDTH / 2 - text.get_width() / 2, 30))

  #blit = draw
  #drawing each image from the images list based on the attempt_count at pos(200, 200)

  #draw word
  display_word = ""
  #checks each letter in the word that is supposed to be guessed
  for letter in word:
    #checks if the letter is in the guessed letters list
    if letter in guessed_letters:
      #if it is, then the letter is automaticall added in the correct spot
      display_word += letter + " "
    else:
      #if it is not, then an "_ " is displayed showing the letter has not been guessed
      display_word += "_ "
  text = WORD_FONT.render(display_word, 1,  BLACK)
  window.blit(text, (550, 325))

  #draw  buttons
  for letter in letters:
    x, y, ltr, visible = letter
    if visible:
      pygame.draw.circle(window, BLACK, (x, y), RADIUS, 4)
      text = LETTER_FONT.render(ltr, 1, BLACK)
      window.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

  window.blit(images[attempt_count], (200, 200))
  pygame.display.update()

#function to display the end game message
def display_message(message):
  window.fill(WHITE)
  text = WORD_FONT.render(message, 1, BLACK)
  window.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
  pygame.display.update()
  pygame.time.delay(3000)

#function for the entire game
def game():
  global attempt_count
  #setting FPS and clock
  FPS = 144 
  clock = pygame.time.Clock()

  #boolean for the runnning of the game
  run = True
  while run:
    clock.tick(FPS)
    #looking for mouse or keyboard events
    for event in pygame.event.get():
      #if the event is clicking the quit button, exits the while loop and ends the game
      if event.type == pygame.QUIT:
        run = False
      #if the event is clicking the mouse button on a position in the pygame window
      if event.type == pygame.MOUSEBUTTONDOWN:
        m_x, m_y = pygame.mouse.get_pos()
        for letter in letters:
          x, y, ltr, visible = letter
          if visible:
            distance = math.sqrt((x - m_x) **2 + (y - m_y) **2)
            if distance < RADIUS:
              letter[3] = False
              guessed_letters.append(ltr)
              #check to see if the letter is not in the word to update the attempt count
              if ltr not in word:
                attempt_count += 1

    draw()
    #checking the end game
    won = True
    #checks for each letter in the word
    for letter in word:
      #checks to see if the letter is not in the guessed letters list
      if letter not in guessed_letters:
        #won is set to false
        won = False
        break

    #changes display if won
    if won:
      display_message("You WON!")
      break

    #changes display if lost
    if attempt_count == 6:
      display_message("You LOST!")
      break

game()
pygame.quit()
