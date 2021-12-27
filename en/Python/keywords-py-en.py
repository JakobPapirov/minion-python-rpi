# -*- coding: utf-8 -*-
import random as rand # Standard library
import time # Standard library
from yachalk import chalk # pip install yachalk
import emoji as emoji # pip install emoji

from library.welcomeScreen import welcome_en as welcome
from library.farwell import showTotalScoreBye_en as showTotalScoreBye

def printDef():
  printInText = input("Type something: ")
  if printInText == '':
    printInText = 'S o n j a'
    #print("You didn't make a choice, please try again")
  else:
    pass

  printInColor = input("Pick text-color: black, white, red: ")
  if printInColor == '':
    printInColor = 'red'
  else:
    pass

  printInBgColor = input("Pick a background-color: black, white, red: ")
  if printInBgColor == '':
    printInBgColor = 'black'
  else:
    pass

  if printInColor == 'black':
    if printInBgColor == 'black':
      print(chalk.bg_black(chalk.black("{}".format(printInText))))
    elif printInBgColor == 'white':
      print(chalk.bg_white(chalk.black("{}".format(printInText))))
    elif printInBgColor == 'red':
      print(chalk.bg_red(chalk.black("{}".format(printInText))))
  elif printInColor == 'white':
    if printInBgColor == 'black':
      print(chalk.bg_black(chalk.white("{}".format(printInText))))
    elif printInBgColor == 'white':
      print(chalk.bg_white(chalk.white("{}".format(printInText))))
    elif printInBgColor == 'red':
      print(chalk.bg_red(chalk.white("{}".format(printInText))))
  elif printInColor == 'red':
    if printInBgColor == 'black':
      print(chalk.bg_black(chalk.red("{}".format(printInText))))
    elif printInBgColor == 'white':
      print(chalk.bg_white(chalk.red("{}".format(printInText))))
    elif printInBgColor == 'red':
      print(chalk.bg_red(chalk.red("{}".format(printInText))))

def forLoopDef():
  forLoopDefIn = input("How many times to loop ? ")
  if forLoopDefIn == '':
    forLoopDefIn = 3
  else:
    forLoopDefIn = int(forLoopDefIn)

  forLoopDefText = "Wheee"
  for i in range(forLoopDefIn):
    print(chalk.bg_black(chalk.red("{}. {}".format(i, forLoopDefText))))

def keywordDef():
  print("")
  print("Here you will learn \n"
        + chalk.bg_yellow_bright(chalk.blue("for")) + ", "
        + chalk.bg_yellow_bright(chalk.blue("input")) + " and\n"
        + chalk.bg_yellow_bright(chalk.blue("print")) + " keywords")
  tempVar = ['for', 'input', 'print']

  randIntGen = rand.randint(0, tempVar.__len__() - 1)
  keywordDefPick = tempVar[randIntGen]

  if keywordDefPick == 'for':
    answer = True
    while answer:
        print('')
        keywordDefIn = input('How to show text once or many times on screen (loop) ? ')
        if keywordDefIn == 'for':
            print(":)")
            break
        else:
            print(":(")
  if keywordDefPick == 'input':
    answer = True
    while answer:
        print('')
        keywordDefIn = input('How to ask user for input ? ')
        if keywordDefIn == 'input':
          print(":)")
          break
        else:
          print(":(")
  if keywordDefPick == 'print':
    answer = True
    while answer:
        print('')
        keywordDefIn = input('How to print text to screen once ? ')
        if keywordDefIn == 'print':
          print(":)")
          break
        else:
          print(":(")

storeState = True

while storeState:
    print("")
    print("----------")
    print("1. print.")
    print("2. for-loop.")
    print("3. keywords.")
    print("0. Press 0 to exit the game")
    print("")
    userChoice = input("What do you want to do ? ")
    print("----------")
    print("")
    if userChoice == '':
        print("You didn't make a choice, please try again")
    else:
        userChoice = int(userChoice)

    if userChoice == 1:
        printDef()
    elif userChoice == 2:
        forLoopDef()
    elif userChoice == 3:
      keywordDef()
    elif userChoice == 0:
        print("Thanks for coding !")
        print("See you next time !")
        storeState = False