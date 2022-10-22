import random
r = ("Snake", "Water", "Gun")
print("Welcome to SNAKE WATER GUN game.")
s = "Snake"
w = "Water"
g = "Gun"
c = 0
u = 0
co = 0
while(True):
    i = input("What do you wish to chose SNAKE, WATER or GUN?\nNOTE: Please write in proper case.\n")
    c = c + 1
    swg = random.choice(r)
    if (c==11):
        print("Game Over!\n", "Now Time for scores:\n",
        "Computer scored:",co,"\nYou scored:", u)
        break
    if (i==swg):
        print("Computer chose:",swg,"\nRound Score:Tie")
        continue
    elif (i!=swg):
        if (i==s):
            if (swg==g):
                print("Computer chose:",swg,"\nRound Score: You Lost")
                co = co + 1
            else:
                print("Computer chose:",swg,"\nRound Score: You Won")
                u = u + 1
        elif (i==w):
            if (swg==s):
                print("Computer chose:",swg,"\nRound Score: You Lost")
                co = co + 1
            else:
                print("Computer chose:",swg,"\nRound Score: You Won")
                u = u + 1
        elif (i==g):
            if (swg==w):
                print("Computer chose:",swg,"\nRound Score: You Lost")
                co = co + 1
            else:
                print("Computer chose:",swg,"\nRound Score: You Won")
                u = u + 1
        continue
    break