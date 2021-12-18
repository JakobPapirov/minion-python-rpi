import random as rand
from yachalk import chalk
import emoji

def welcome_en():

    print("")
    name = str(input("What's your name ? "))

    print("Welcome, " + chalk.red(chalk.bg_white("{}")).format(name) + emoji.emojize(":red_exclamation_mark:"))

    print("")
    questionsNum = int(input("How many questions do you want ? "))
    print("")

    return name, questionsNum

def welcome_sv():

    print("")
    name = str(input("Vad heter du ? "))

    print("Välkommen, " + chalk.red(chalk.bg_white("{}")).format(name) + emoji.emojize(":red_exclamation_mark:"))

    print("")
    questionsNum = int(input("Hur många frågor vill du ha ? "))
    print("")

    return name, questionsNum

def welcome_ru():

    print("")
    name = str(input("Как тебя завут ? "))
    print("Привет, " + chalk.red(chalk.bg_white("{}")).format(name) + emoji.emojize(":red_exclamation_mark:"))

    print("")
    questionsNum = int(input("Сколько вопросов задать ? "))
    print("")

    return name, questionsNum