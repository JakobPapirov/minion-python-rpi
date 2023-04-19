# -*- coding: utf-8 -*-
import random as rand

from library.welcomeScreen import welcome
from library.farwell import showTotalScoreBye
# https://stackoverflow.com/questions/20309456/call-a-function-from-another-file

name, questionsNum = welcome()

questionsKeeper = 1
rightAns = 0
progress = ''

while questionsKeeper <= questionsNum:

  questionsKeeper += 1

  alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
              'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

  randIntGen = rand.randint(1, alphabet.__len__() +1 )
  qLetter = alphabet[randIntGen]

  qIn = 'a'

  while qIn != qLetter:
    qIn = str(input("Type {} ? ".format(qLetter)))

    if qIn == qLetter:
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
