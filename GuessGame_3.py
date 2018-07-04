#coding: utf-8

import random


class Player:
    def __init__(self, test_range):
        self.low = 1
        self.high = test_range
        self.history = []

    def interpreter(self, func_name):
        if func_name == 1:
            return self.random_guess
        elif func_name == 2:
            return self.half_guess
        elif func_name == 3:
            return self.designed_guess_randomfirst

    def renew(self, tpl):
        if tpl[0] == "low":
            self.low = tpl[1]
        elif tpl[0] == "high":
            self.high = tpl[1]

    def random_guess(self):
        tmp = random.randint(self.low + 1, self.high - 1)
        self.history.append(tmp)
        return tmp

    def half_guess(self):
        tmp = (self.low + self.high) // 2
        while tmp in self.history:
            tmp += 1
        self.history.append(tmp)
        return tmp

    def designed_guess_randomfirst(self):
        if len(self.history) == 0:
            return self.random_guess()
        else:
            return self.half_guess()


print("What is your name?")
name = input("> ")
maxi = 100
print("Which of the rules do you want this program to use?\n(Enter the number)")
print("  1. Random guess")
print("  2. Middle suggestion")
print("  3. First random, then middle suggestion")
while True:
    try:
        que = int(input("> "))
        break
    except:
        print("Hey {}, check your input!".format(name))
print("Hi{}, imagine a number between 1 to {}. I will find your number within 6 guess".format(name, maxi))

counter = 6
total = counter
pc = Player(maxi)
func = pc.interpreter(que)

while counter != 0:
    try:
        if counter == 1:
            print("This is the last round.")
        else:
            print("I have another {} chance(s)".format(counter - 1))

        pc_guess = func()
        print("Is it {}?".format(pc_guess))
        print("If yes, enter 'yes', if this is smaller than yours, enter 'low', if larger, enter 'high'.")

        while True:
            response = input("> ")
            if response not in ["yes", "low", "high"]:
                print("Hey {}, check your input!".format(name))
            else:
                break

        if response == "yes":
            print("Whoopee! Let's enjoy again！")
            break
        else:
            tpl = (response, pc_guess)
            pc.renew(tpl)
            counter -= 1
            print("")
    except:
        print("Hey {}, check your input!".format(name))

if counter == 0:
    print("What a bummer! Could you tell me your number?")
    ans = int(input("> "))
    if ans < pc.low or ans > pc.high or ans in pc.history:
        print("You are lying to me！")
    else:
        print("You win. Give me one more chance!")
