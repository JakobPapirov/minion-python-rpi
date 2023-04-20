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

  numbers = ['ETT', 'EN', 'TVÅ', 'TRE', 'FYRA', 'FEM', 'SEX', 'SJU', 'ÅTTA', 'NIO',
              'TIO', 'ELVA', 'TOLV', 'TRETTON', 'FJORTON', 'FEMTON', 'SEXTON',
             'SJUTTON', 'ARTON', 'NITTON','TJUGO']

  randIntGen = rand.randint(0, numbers.__len__() -1 )
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