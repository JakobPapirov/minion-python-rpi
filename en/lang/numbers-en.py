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

  numbers = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN',
              'ELEVEN', 'TWELVE', 'THIRTEEN', 'FOURTEEN', 'FIFTEEN', 'SIXTEEN', 'SEVENTEEN', 'EIGHTEEN', 'NINETEEN', 'TWENTY']

  randIntGen = rand.randint(1, numbers.__len__() +1 )
  qNumbers = numbers[randIntGen]

  qIn = 'a'

  while qIn != qNumbers:
    qIn = str(input("Type {} ? ".format(qNumbers)))

    if qIn == qNumbers:
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
