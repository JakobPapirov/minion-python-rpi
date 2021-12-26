# -*- coding: utf-8 -*-
import random as rand
from yachalk import chalk
import emoji as emoji

from library.welcomeScreen import welcome_en as welcome
from library.farwell import showTotalScoreBye_en as showTotalScoreBye

name, questionsNum = welcome()

questionsKeeper = 1
rightAns = 0
progress = ''

while questionsKeeper <= questionsNum:

  questionsKeeper += 1

  mathVarA = rand.randint(0,1)
  mathVarB = rand.randint(0,8)

  mq1In = 999999

  while mq1In != (mathVarA + mathVarB):
    mq1In = input("{} + {} ? ".format(mathVarA, mathVarB))
    if mq1In == '':
        mq1In = 1 # Why = 1?
    else:
        mq1In = int(mq1In)

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
