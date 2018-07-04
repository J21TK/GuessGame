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


print("お名前は何ですか？")
name = input("> ")
range = 100
print("どのモードのPCと対戦しますか？（数字を入力して下さい）")
print("  1. ランダム選択")
print("  2. 1/2法")
print("  3. はじめだけランダム")
while True:
    try:
        que = int(input("> "))
        break
    except:
        print("{}さん、入力がおかしいですよ？".format(name))
print("{}さん、1から{}までの数字で、何か数字を思い描いて下さい 。私が6回以内に当てて見せます。".format(name, range))

counter = 6
total = counter
pc = Player(range)
func = pc.interpreter(que)

while counter != 0:
    try:
        if counter == 1:
            print("これがラストチャンスですね。")
        else:
            print("あと{}回チャンスが残っています。".format(counter - 1))

        pc_guess = func()
        print("あなたの数字は{}ですか？".format(pc_guess))
        print("（正しければ ok、これがあなたの数字より小さければ low、 大きければ highを入力）")

        while True:
            response = input("> ")
            if response not in ["ok", "low", "high"]:
                print("{}さん、入力がおかしいですよ？".format(name))
            else:
                break

        if response == "ok":
            print("わーい、当たった！また遊びましょう！")
            break
        else:
            tpl = (response, pc_guess)
            pc.renew(tpl)
            counter -= 1
            print("")
    except:
        print("{}さん、入力がおかしいですよ？".format(name))

if counter == 0:
    print("悔しいです。答えを教えて下さい。")
    ans = int(input("> "))
    if ans < pc.low or ans > pc.high:
        print("あなたはどこかで嘘をついています！")
    else:
        print("参りました。またやりましょう！")
