# -*- coding: utf-8 -*-
import random as rand

print("")
name = str(input("What's your name ? "))
print("")

questionsNum = int(input("How many questions do you want? "))
print("")

questionsKeeper = 1
rightAns = 0
progress = ''

while questionsKeeper <= questionsNum:

  questionsKeeper += 1

  mathVarA = rand.randint(0,1)
  mathVarB = rand.randint(0,8)

  mq1In = 999999

  while mq1In != (mathVarA + mathVarB):
    mq1In = int(input("{} + {} ? ".format(mathVarA, mathVarB)))

    if mq1In == (mathVarA + mathVarB):
      print(":)")
      print("")
      progress = str(progress) + '='
      print("{}".format(progress))
      print("")
      rightAns += 1
      break
  else:
    print(":(")
    print("")

if rightAns == questionsNum:
  print("Wow total :) = {}".format(rightAns))
  print("Super :==) {} \o/".format(name))
  print("")
