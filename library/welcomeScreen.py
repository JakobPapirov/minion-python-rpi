import random as rand
from yachalk import chalk
import emoji

def welcome_en():

    print("")
    name = str(input("What's your name ? "))
    if name == '':
        name = 'Jakob'
    else:
        pass

    print("Welcome, " + chalk.red(chalk.bg_white("{} ")).format(name) + emoji.emojize(":red_exclamation_mark:"))

    print("")
    questionsNum = input("How many questions do you want ? ")
    print("")
    if questionsNum == '':
        questionsNum = 1
    else:
        questionsNum = int(questionsNum)

    return name, questionsNum

def welcome_sv():

    print("")
    name = str(input("VAD HETER DU ? "))
    if name == '':
        name = 'Jakob'
    else:
        pass

    print("Välkommen, " + chalk.red(chalk.bg_white("{} ")).format(name) + emoji.emojize(":red_exclamation_mark:"))

    print("")
    questionsNum = input("HUR MÅNGA FRÅGOR VILL DU HA ? ")
    print("")
    if questionsNum == '':
        questionsNum = 1
    else:
        questionsNum = int(questionsNum)

    return name, questionsNum

def welcome_ru():

    print("")
    name = str(input("Как тебя завут ? "))
    print("Привет, " + chalk.red(chalk.bg_white("{}")).format(name) + emoji.emojize(":red_exclamation_mark:"))

    print("")
    questionsNum = input("Сколько вопросов задать ? ")
    print("")
    if questionsNum == '':
        questionsNum = 1
    else:
        questionsNum = int(questionsNum)

    return name, questionsNum