import random
import art
import os
import sys
import os
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def game():
    print(art.art)
    card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    yourCard = [random.choice(card),random.choice(card)]
    print(f"Your Cards : {yourCard}    sum = {sum(yourCard)}")
    camputerC1 = [random.choice(card),random.choice(card)]
    if sum(yourCard) > 10 or sum(camputerC1) > 10:
        card[0] = 1
    card = card*4    
    print(f"camputer's first Card : {camputerC1[0]}")
    
    def newCard():
        q = input("Type 'y' to get another card, type 'n' to pass: ")
        if q == "y":
            card3 = random.choice(card)
            yourCard.append(card3)
            print(f"your new cards : {yourCard}    sum = {sum(yourCard)}")
            if sum(yourCard) > 21 :
                print(f"your cards are higher than 21 YOU LOST!    sum = {sum(yourCard)} ")
                q = input("do you want to start new game? 'y' or 'n'  :")
                if q == "y":
                    clear()
                    return
                else:
                    sys.exit()
            if q == "y":
                newCard()
        elif q == "n":
            print(f"your final cards : {yourCard}   sum = {sum(yourCard)}")
            sumC = sum(camputerC1)
            while sumC < 17:
                card3C = random.choice(card)
                camputerC1.append(card3C)
                sumC = sum(camputerC1)
            print(f"dealer's final card : {camputerC1}   sum = {sum(camputerC1)}")
        if sum(camputerC1) > sum(yourCard) and sum(camputerC1) < 22:
            q = input("sorrryy you losse! enter 'n' for start new game! : ")
            if q == "n":
                clear()
                return
        elif sum(camputerC1) == sum(yourCard):
            q = input("draw ! not bad. enter 'n' for start new game! : ")
            if q == "n":
                clear()
                return
        elif sum(camputerC1) < sum(yourCard) or sum(camputerC1) > sum(yourCard):
            q = input("you WIN!! perfect. enter 'n' for start new game! :")
            if q == "n":
                clear()
                return
                
    newCard()
while True:
    game()
