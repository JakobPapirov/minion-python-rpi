from yachalk import chalk
import emoji

def showTotalScoreBye(rightAns, questionsNum, name):
    if rightAns == questionsNum:
      if questionsNum == 0:
        print(chalk.bg_yellow_bright(chalk.cyan("Haha, no questions wanted!")))
      else:
        print("Wow total :) = {}".format(rightAns))
        print("Super :==) {} \o/".format(name))
        print("")
        print("Bye" + emoji.emojize(":red_exclamation_mark:"))