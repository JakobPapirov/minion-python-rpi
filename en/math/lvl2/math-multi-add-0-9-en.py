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

  mathVarA = rand.randint(0,3)
  mathVarB = rand.randint(0,3)
  mathVarC = rand.randint(0,3)

  mq1In = 999999

  while mq1In != (mathVarA + mathVarB + mathVarC):
    mq1In = int(input("{} + {} + {} ? ".format(mathVarA, mathVarB, mathVarC)))
    # Programme fails if enter or letters are submitted

    if mq1In == (mathVarA + mathVarB + mathVarC):
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