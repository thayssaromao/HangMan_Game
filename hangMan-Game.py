import random, os, time

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
listOfWords = ["Baile", "Coca cola", "Duna", "Askov", "Homem aranha", "alanzoka", "zombie", "apple", "Brazil"]
lives = 6
hang = 0
letterPicked = []
wordChosen = random.choice(listOfWords).lower()
print(HANGMANPICS[hang])
  
while True:
  #time.sleep(3)
  #os.system('clear')
  print(f"\n{lives} lives left", end="\n")

  askLetter = input("Letter > ").lower()
  if askLetter in letterPicked:
    print("You've tried that before")
    continue
  letterPicked.append(askLetter)
  print()

  if  askLetter not in wordChosen:
    hang += 1
    lives -=1
    print(HANGMANPICS[hang])
    
  
  winGame = True
  print()
  for i in wordChosen:
    if i in letterPicked:
      print(i, end=" ")
    elif i == " ":
      print(" ", end="")
    else:
      print("_", end=" ")
      winGame=False
  if winGame:
    print(f"\nYOU WON WITH {lives} lives left!! ")
    break
  print() 
  if lives <= 0:
    print("\nYOU LOOOOOOOOOOOOOSE !!!!", end="\n")
    print(f"The word was '{wordChosen}'")
    break