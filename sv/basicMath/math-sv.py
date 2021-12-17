# -*- coding: utf-8 -*-
import random as rand
import emoji as emoji
from yachalk import chalk

print("")
name = str(input("Vad heter du ? "))
print("Välkommen, " + chalk.red(chalk.bg_white("{}")).format(name) + emoji.emojize(":red_exclamation_mark:"))

questionsNum = int(input("Hur många frågor vill du ha ? "))
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

if rightAns == questionsNum:
  if questionsNum == 0:
    print(chalk.bg_yellow_bright(chalk.cyan("Haha, du ville inte ha några frågor!")))
  else:
    print("Wow totalt :) = {}".format(rightAns))
    print("Super :==) {} \o/".format(name))
    print("")
