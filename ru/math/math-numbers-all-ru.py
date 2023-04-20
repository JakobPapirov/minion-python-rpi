# -*- coding: utf-8 -*-
import random as rand # Standard library
from yachalk import chalk # pip install yachalk
import emoji as emoji # pip install emoji
import numpy as np # pip install numpy

from library.welcomeScreen import welcome_ru as welcome
from library.farwell import showTotalScoreBye_ru as showTotalScoreBye

name, questionsNum = welcome()

questionsKeeper = 1
rightAns = 0
progress = ''

while questionsKeeper <= questionsNum:

  questionsKeeper += 1

  genNum = np.random.random_sample() * np.power(10, rand.randint(1, 9))
  # https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html
  # https://numpy.org/doc/stable/reference/random/index.html#random-quick-start

  mq1In = 0

  while mq1In != (genNum):
    mq1In = input("Type {} : ".format(genNum))

    if mq1In == (genNum):
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