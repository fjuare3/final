import os
import random
def tweenty_one_dealer():
    print ("This program returns the probability of a dealer busting (losing) in a game of 21")
    n = (int(input("How many games are played? ")))
    bust = 0
    for i in range(n):
        total = 0
        while total < 17:
            draw = random.randrange(1, 11)
            if (draw == 1 or draw == 11) and (total + 11) in (17, 18, 19, 20, 21):
                total = total + 11
            elif (total + draw) > 21:
                bust = bust + 1
                break
            else:
                total += draw
    print((bust/n)*100, "percent")

tweenty_one_dealer()
