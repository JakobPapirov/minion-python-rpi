from yachalk import chalk
import emoji

def showTotalScoreBye_en(rightAns, questionsNum, name):
    if rightAns == questionsNum:
      if questionsNum == 0:
        print(chalk.bg_yellow_bright(chalk.cyan("Haha, no questions wanted!")))
      else:
        print("Wow total :) = {}".format(rightAns))
        print("Super :==) {} \o/".format(name))
        print("")
        print("Bye " + emoji.emojize(":red_exclamation_mark:"))


def showTotalScoreBye_sv(rightAns, questionsNum, name):
  if rightAns == questionsNum:
    if questionsNum == 0:
      print(chalk.bg_yellow_bright(chalk.cyan("HAHA, DU VILLE INTE HA NÅGRA FRÅGOR!")))
    else:
      print("Wow, TOTALT :) = {}".format(rightAns))
      print("SUPER :==) {} \o/".format(name))
      print("")
      print("Hej då " + emoji.emojize(":red_exclamation_mark:"))

def showTotalScoreBye_ru(rightAns, questionsNum, name):
  if rightAns == questionsNum:
    if questionsNum == 0:
      print(chalk.bg_yellow_bright(chalk.cyan("Хаха, вопросов нехотьела!")))
    else:
      print("Уау сумма :) = {}".format(rightAns))
      print("Супер :==) {} \o/".format(name))
      print("")
      print("Пака " + emoji.emojize(":red_exclamation_mark:"))