# -*- coding: utf-8 -*-
import random as rand # Standard library
import emoji as emoji # pip install emoji
from yachalk import chalk # pip install yachalk

from library.welcomeScreen import welcome_en as welcome
from library.farwell import showTotalScoreBye_en as showTotalScoreBye

name, questionsNum = welcome()

questionsKeeper = 1
rightAns = 0
# Change to rightAnsCount across all programmes
progress = ''

def followupQ(mathVar, mathVarB, correctAns):
  userIn2 = 999999

  while userIn2 != correctAns:
    userInput2 = int(input("Good, now tell me what's {} ⋅ {} = ? ".format(mathVar, (mathVarB+1))))
    # Programme fails if enter or letters are submitted
    # https://wumbo.net/symbols/dot-operator/
    if userInput2 == correctAns:
      print(" :)")
      print("")
      break
    else:
      print(" :(")
      print("")

while questionsKeeper <= questionsNum:

  questionsKeeper += 1

  mathVar = 2
  mathVarB = rand.randint(0,9)
  # Later ask user to set difficulty, by setting max (currently 9)

  mq1In = 999999

  correctAns = (mathVar * (mathVarB + 1))
  print(correctAns)

  print("Add everything together: \n{}".format(mathVar))
  for i in range(mathVarB):
    print("+ {}".format(mathVar))
  while mq1In != correctAns:

    mq1In = int(input("Total is = ? "))
    # Programme fails if enter or letters are submitted

    if mq1In == correctAns:
      print(" :)")
      print("")

      followupQ(mathVar, mathVarB, correctAns)

      progress = str(progress) + '='
      print("{}".format(progress))
      print("")
      rightAns += 1
      break
    else:
      print(" :(")
      print("")

showTotalScoreBye(rightAns, questionsNum, name)