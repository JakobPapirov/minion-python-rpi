import random as rand
from yachalk import chalk
import emoji

def welcome():

    print("")
    name = str(input("What's your name ? "))

    print("Welcome, " + chalk.red(chalk.bg_white("{}")).format(name) + emoji.emojize(":red_exclamation_mark:"))

    print("")
    questionsNum = int(input("How many questions do you want ? "))
    print("")

    return name, questionsNum