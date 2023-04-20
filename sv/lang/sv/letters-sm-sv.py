# -*- coding: utf-8 -*-
import random as rand

from library.welcomeScreen import welcome_sv as welcome
from library.farwell import showTotalScoreBye_sv as showTotalScoreBye
# https://stackoverflow.com/questions/20309456/call-a-function-from-another-file

name, questionsNum = welcome()

questionsKeeper = 1
rightAns = 0
progress = ''

while questionsKeeper <= questionsNum:

  questionsKeeper += 1

  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
              'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z',
              'å','ä','ö']

  randIntGen = rand.randint(0, alphabet.__len__() -1 )
  qLetter = alphabet[randIntGen]

  qIn = 'A'

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