# -*- coding: utf-8 -*-
import random as rand # Standard library
from yachalk import chalk # pip install yachalk
import emoji as emoji # pip install emoji

from library.welcomeScreen import welcome_en as welcome
from library.farwell import showTotalScoreBye_en as showTotalScoreBye

name, questionsNum = welcome()

questionsKeeper = 1
rightAns = 0
progress = ''

while questionsKeeper <= questionsNum:

  questionsKeeper += 1

  mathVarA = rand.randint(8,12)
  mathVarB = rand.randint(0,4)

  while mathVarA + mathVarB > 12:
    mathVarB = rand.randint(0, 4)
  else:
    pass

  mq1In = 999999

  while mq1In != (mathVarA + mathVarB):
    mq1In = input(input("{} + {} ? ".format(mathVarA, mathVarB)))

    if mq1In == (mathVarA + mathVarB):
      print(" :)")
      print("")
      progress = str(progress) + '='
      print("{}".format(progress))
      print("")
      rightAns += 1
      break
    else:
      print(" :(")
      print("")

showTotalScoreBye(rightAns, questionsNum, name)