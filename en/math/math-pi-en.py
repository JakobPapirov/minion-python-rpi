# -*- coding: utf-8 -*-
import random as rand # Standard library
from yachalk import chalk # pip install yachalk
import emoji as emoji # pip install emoji

import math # Standard library
from mpmath import mp # https://mpmath.org/ | # pip install mpmath

from library.welcomeScreen import welcome_en as welcome
from library.farwell import showTotalScoreBye_en as showTotalScoreBye

name, questionsNum = welcome()

questionsKeeper = 1
rightAns = 0
progress = ''

while questionsKeeper <= questionsNum:

  questionsKeeper += 1

  # Generates pi to a designated precision
  piDecimalQty = input("How many decimals do you want ? ")
  if piDecimalQty == '':
    mp.dps = 1
  else:
    mp.dps = int(piDecimalQty)

  if mp.dps == 0:
    mp.dps = 1

  genPI = mp.quad(lambda x: mp.exp(-x ** 2), [-mp.inf, mp.inf]) ** 2
  genPIfloat = float(genPI)

  tempBool = True
  # Might be useful to add a type check first (for this one or similar programme)

  while tempBool:
    print("")
    mq1In = input("Type {} ? ".format(genPI))
    if mq1In == '':
        mq1In = 1
    else:
        mq1In = float(mq1In) # https://stackoverflow.com/questions/379906/how-do-i-parse-a-string-to-a-float-or-int

    absValThreshold = 0.5 # Experimentally determined to be sufficient for an accidental type-o by user (=minion)
      # Could technically be determined by the number of decimals chosen
    varCompBool = math.isclose(mq1In, genPIfloat, abs_tol=absValThreshold) # Expected result True/False
      # https://docs.python.org/3/whatsnew/3.5.html#pep-485-a-function-for-testing-approximate-equality

    if varCompBool == True:
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