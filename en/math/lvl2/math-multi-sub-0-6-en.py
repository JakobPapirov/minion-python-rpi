# -*- coding: utf-8 -*-
import random as rand # Standard library
import emoji as emoji # pip install emoji
from yachalk import chalk # pip install yachalk

from library.welcomeScreen import welcome_en as welcome
from library.farwell import showTotalScoreBye_en as showTotalScoreBye

name, questionsNum = welcome()

questionsKeeper = 1
rightAns = 0
progress = ''

while questionsKeeper <= questionsNum:

  questionsKeeper += 1

  mathVar = 6

  mathVarA = rand.randint(0,2)
  mathVarB = rand.randint(0,2)
  mathVarC = rand.randint(0,2)

  mq1In = 999999

  while mq1In != (mathVar - mathVarA - mathVarB - mathVarC):
    mq1In = int(input("{} - {} - {} - {} ? ".format(mathVar, mathVarA, mathVarB, mathVarC)))
    # Programme fails if enter or letters are submitted

    if mq1In == (mathVar - mathVarA - mathVarB - mathVarC):
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