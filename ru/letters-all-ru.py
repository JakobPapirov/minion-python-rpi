# -*- coding: utf-8 -*-
import random as rand

from library.welcomeScreen import welcome_ru as welcome
from library.farwell import showTotalScoreBye_ru as showTotalScoreBye
# https://stackoverflow.com/questions/20309456/call-a-function-from-another-file

name, questionsNum = welcome()

questionsKeeper = 1
rightAns = 0
progress = ''

while questionsKeeper <= questionsNum:

  questionsKeeper += 1

  alphabetBig = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
              'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

  alphabetSmall = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
              'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

  randAlphabet = rand.randint(0,2)

  if randAlphabet == 0:
      randIntGen = rand.randint(0, alphabetBig.__len__() -1 )
      qLetter = alphabetBig[randIntGen]

      qIn = 'A'
  else:
      randIntGen = rand.randint(0, alphabetSmall.__len__() - 1)
      qLetter = alphabetSmall[randIntGen]

      qIn = ''

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