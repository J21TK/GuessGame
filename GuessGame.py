# a is to define the player name, b is the maximum numberof this game,
# c and d are to define how many times the player is allowed to guess (c is for counter),
# e is the guessed number of the player, x is the actual number of PC.

import random
a = input("Hi, what is your name?\n>")
b = input("Hi {}, tell me your favorite number (integer, greater than 1).\n>".format(a))
x = random.randint(1,int(b))
c = int(input("OK {}, now I am thinking of a number from 1 to {}. \n"
              "How many guesses do you need to guess my number?\n>".format(a, b)))
d = c
while c != 0:
    if c == 1:
        e = input("Please give me your number. This is a last chance.\n>")
    else:
        e = input("Please give me your number. You have {} more guess.\n>".format(c-1))
    try:
        if e == "Give up":
           print("Game over. My number is {}".format(x))
        elif int(e) == x:
            print("Great job, {}! You guessed my number in {} guesses!".format(a, d-c+1))
            break
        elif int(e) > x:
            print("{} is too large!".format(e))
        elif int(e) < x:
            print("{} is too small!".format(e))
        c -= 1
    except:
        print("Hey {}, what are you talking about??".format(a))
if c == 0:
    print("Game over. My number is {}".format(x))