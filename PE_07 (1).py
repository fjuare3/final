from random import randrange
def intro():
    print("program simulates games of craps and returns the probability of player winning")
    n = int(input("how many games are played? "))
    return n

def game_sim(n):
    win = 0
    loss = 0
    for single_game in range(n):
        a = randrange(1,7)
        b = randrange(1,7)
        c = a + b
        if (a+b==7) or (a+b==11):
            win += 1
        elif (a+b==2) or (a+b==3) or (a+b==12):
            loss += 1
        else:
            a = b = 0
            while (a+b!=7) or (a+b!=c):
                a = randrange(1,7)
                b = randrange(1,7)
                if (a+b==7):
                    loss += 1
                    break
                elif (a+b==c):
                    win += 1
                    break
    print(win/(win+loss))

def script():
    n = intro()
    game_sim(n)

script()

