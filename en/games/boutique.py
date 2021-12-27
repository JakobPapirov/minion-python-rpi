# -*- coding: utf-8 -*-
import random as rand # Standard library
import time # Standard library
from yachalk import chalk # pip install yachalk
import emoji as emoji # pip install emoji

# Should game data be stored inside a Boutique class with Animal etc subclasses?
# Should I use numpy and an array to store data?
# *Might* add buyer start capital

""" State of the art:
https://appdividend.com/2021/02/23/python-comment-block-how-to-write-multi-line-comments/
* User can let the programme generate a boutique for her/him, but is allowed to have a say in types of items
    animals = cats or dogs
    foods = milk or bread
        Not yet implemented
    The quantity available and price
* The boutique has a cashier which increases with each purchase
"""

def animalsCreator(content):
    #print("{}".format(content) + " created.")
    animalsList = ['Cats', 'Dogs']

    # Should be able to extract each index and store as a key I believe
    class Animal:
        def __init__(self, species, qty, price):
            self.species = species
            self.qty = qty
            self.price = price

        # Perhaps change to a getter https://www.geeksforgeeks.org/getter-and-setter-in-python/
        def stats(self):
            print("")
            print(f"Species: {self.species}\nQuantity: {self.qty}\nPrice: {self.price}")
                # https://realpython.com/python-f-strings/

        def animalGetPrice(self):
            return self.price

        def animalSetQty(self, qtyOut):
            self.qty = self.qty - qtyOut

    for x in animalsList:
        print("")
        # Presently, only if cats = no, then asks for dogs - need to solve this
        animalsListChoice = str(input("Does your boutique have {} ? [yes/no] ".format(x)))
        if animalsListChoice == "yes":
            print("")
            animalsQtyIn = int(input("How many {}".format(x) + " does your boutique have ? "))
            animalsPriceIn = int(input("How much does one {} cost ? ".format(x)))

            creature = Animal(x, animalsQtyIn, animalsPriceIn)
            creature.stats()

            return creature
        elif animalsListChoice == "no":
            print("No {}".format(x) + " in boutique, understood.")

def boutiqueOpen(creature):
    cashier = 0

    boutiqueStatus = True

    while boutiqueStatus:
        print("")
        print("~~~~~~~~~~~~~~~~~~~~")
        print("1. Purchase something.")
        print("2. Check inventory.")
        print("3. Check cashier.")
        print("0. Exit back to boutique 'initial' menu.")
        print("")
        userChoice = input("What do you want to do ? ")
        print("~~~~~~~~~~~~~~~~~~~~")
        print("")
        if userChoice == '':
            print("You didn't make a choice, please try again")
        else:
            userChoice = int(userChoice)

        if userChoice == 1:
            # print("This feature is not yet complete.")
            # Presently only possible to purchase animals (one type, see 'animalsList')
            # Should list available items to buy
            itemToBuy = input("What do you wish to buy ? ")
            # Hard-coding choices at the moment
            if itemToBuy == 'cat':
                itemToBuyPrice = print(f"Price of cat is {creature.animalGetPrice()} €")
                itemToBuyQty = input("How many do you wish to buy ? : ")
                if itemToBuyQty == '':
                    itemToBuyQty = 1
                else:
                    itemToBuyQty = int(itemToBuyQty)
                itemToBuyTotalPrice = input(f"Total price is {creature.animalGetPrice() * itemToBuyQty} € : ")
                if itemToBuyTotalPrice == '':
                    itemToBuyTotalPrice = 1
                else:
                    itemToBuyTotalPrice = int(itemToBuyTotalPrice)

                cashier = cashier + itemToBuyTotalPrice
            elif itemToBuy == 'dog':
                itemToBuyPrice = print(f"Price of dog is {creature.animalGetPrice()} €")
                itemToBuyQty = input("How many do you wish to buy ? : ")
                if itemToBuyQty == '':
                    itemToBuyQty = 1
                else:
                    itemToBuyQty = int(itemToBuyQty)
                itemToBuyTotalPrice = input(f"Total price is {creature.animalGetPrice() * itemToBuyQty} € : ")
                if itemToBuyTotalPrice == '':
                    itemToBuyTotalPrice = 1
                else:
                    itemToBuyTotalPrice = int(itemToBuyTotalPrice)

                cashier = cashier + itemToBuyTotalPrice
            else:
                pass
        elif userChoice == 2:
            print("This feature is not yet complete.")
        elif userChoice == 3:
            print(f"You have {cashier} €")
        elif userChoice == 0:
            print("Exiting the boutique")
            print("... Going back to main menu !")
            # Disabled during dev
            # time.sleep(4) # Delay in seconds
            boutiqueStatus = False

def boutiqueCreator():

    # Should re-name after main def is renamed
    def boutiqueCreatorDef():
        boutiqueContentList = ['Animals', 'Foods']

        boutiqueContentListChecker = []

        for x in boutiqueContentList:
            print("")
            boutiqueContentsChoice = str(input("Does your boutique have {} ? [yes/no] ".format(x)))
            # No user error handling, should add perhaps a try/catch block
            if boutiqueContentsChoice == "yes":
                print("")
                # print("{}".format(x) + " created.")
                boutiqueContentListChecker.append("yes") # https://www.w3schools.com/python/python_lists_add.asp
                #if boutiqueContentList[x] == 'Animals' and userChoice == 'yes':  # Error here <--
                #    creature = animalsCreator(x)
                #    creature.stats()
                creature = animalsCreator(x)
                #creature.stats()
                # Presently, the code doesn't take into account the choice of having Foods
            elif boutiqueContentsChoice == "no":
                boutiqueContentListChecker.append("no")
                print("No {}".format(x) + " in boutique, understood.")
        return creature

    boutiqueCreatorState = True

    while boutiqueCreatorState:
        print("")
        print("====================")
        print("1. Create boutique.")
        print("2. Check the stats of your boutique.")
        print("3. Open boutique.")
        print("0. Exit back to main menu.")
        print("")
        userChoice = input("What do you want to do ? ")
        print("====================")
        print("")
        if userChoice == '':
            print("You didn't make a choice, please try again")
        else:
            userChoice = int(userChoice)

        if userChoice == 1:
            creature = boutiqueCreatorDef() # Should be several creatures, foods, etc
        elif userChoice == 2:
            creature.stats() # Should be several creatures, foods, etc
        elif userChoice == 3:
            creature = boutiqueOpen(creature) # Should be several creatures, foods, etc
        elif userChoice == 0:
            print("Boutiqe has closed !")
            print("... Going back to main menu !")
            # Disabled during dev
            # time.sleep(4) # Delay in seconds
            boutiqueCreatorState = False

storeState = True

while storeState:
    print("")
    print("----------")
    print("1. Let the game create your boutique for you.")
    print("2. Create one yourself.")
    print("0. Press 0 to exit the game")
    print("")
    userChoice = input("What do you want to do ? ")
    print("----------")
    print("")
    if userChoice == '':
        print("You didn't make a choice, please try again")
    else:
        userChoice = int(userChoice)

    if userChoice == 1:
        # Should re-name
        boutiqueCreator()
    elif userChoice == 2:
        print("This feature is not yet complete.")
        storeState = False
    elif userChoice == 0:
        print("Thanks for playing !")
        print("See you next time !")
        storeState = False