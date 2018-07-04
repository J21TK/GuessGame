from GuessGame_2 import *

class NewPlayer(Player):
    def interpreter(self, func_name):
        if func_name == self.random_guess.__name__:
            return self.random_guess
        elif func_name == self.half_guess.__name__:
            return self.half_guess
        elif func_name == self.designed_guess_halfstart.__name__:
            return self.designed_guess_halfstart
        elif func_name == self.designed_guess_randomstart.__name__:
            return self.designed_guess_randomstart
        elif func_name == self.designed_guess_randomfirst.__name__:
            return self.designed_guess_randomfirst
        elif func_name == self.designed_guess_halffirst.__name__:
            return self.designed_guess_halffirst
        elif func_name == self.onethree_guess.__name__:
            return self.onethree_guess
        elif func_name == self.onethree_random_guess.__name__:
            return self.onethree_random_guess
        elif func_name == self.twothree_random_guess.__name__:
            return self.twothree_random_guess
        elif func_name == self.random_onethree_guess.__name__:
            return self.random_onethree_guess
        elif func_name == self.switch_three_guess.__name__:
            return self.switch_three_guess
        elif func_name == self.switch_three_random.__name__:
            return self.switch_three_random
        
    def designed_guess_halfstart(self):
        try:
            if self.history[-2] < self.low:
                prev_low = self.history[-2]
                prev_high = self.high
            elif self.history[-2] > self.high:
                prev_low = self.low
                prev_high =self.history[-2]
            if self.high - self.low > (prev_high - prev_low)/3:
                return self.random_guess()
            else:
                return self.half_guess()
        except: #self.history[-2]が存在しない時、つまり初手
            return self.half_guess()
        
    def designed_guess_randomstart(self):
        try:
            if self.history[-2] < self.low:
                prev_low = self.history[-2]
                prev_high = self.high
            elif self.history[-2] > self.high:
                prev_low = self.low
                prev_high =self.history[-2]
            if self.high - self.low > (prev_high - prev_low)/3:
                return self.random_guess()
            else:
                return self.half_guess()
        except: #self.history[-2]が存在しない時、つまり初手
            return self.random_guess()
    
    def designed_guess_randomfirst(self):
        if len(self.history) == 0:
            return self.random_guess()
        else:
            return self.half_guess()  

    def designed_guess_halffirst(self):
        if len(self.history) == 0:
            return self.half_guess()
        else:
            return self.random_guess()   

    def onethree_guess(self):
        tmp = (self.high - self.low)//3 + self.low
        while tmp in self.history:
            tmp += 1
        self.history.append(tmp)
        return tmp
    
    def twothree_guess(self):
        tmp = (self.high - self.low)//3*2 + self.low
        while tmp in self.history:
            tmp += 1
        self.history.append(tmp)
        return tmp

    def onethree_random_guess(self):
        try:
            if self.history[-2] < self.low:
                prev_low = self.history[-2]
                prev_high = self.high
            elif self.history[-2] > self.high:
                prev_low = self.low
                prev_high =self.history[-2]
            if self.high - self.low > (prev_high - prev_low)/3:
                return self.random_guess()
            else:
                return self.onethree_guess()
        except: #self.history[-2]が存在しない時
            return self.onethree_guess()

    def twothree_random_guess(self):
        try:
            if self.history[-2] < self.low:
                prev_low = self.history[-2]
                prev_high = self.high
            elif self.history[-2] > self.high:
                prev_low = self.low
                prev_high =self.history[-2]
            if self.high - self.low > (prev_high - prev_low)/3:
                return self.random_guess()
            else:
                return self.twothree_guess()
        except: #self.history[-2]が存在しない時
            return self.twothree_guess()

    def random_onethree_guess(self):
        try:
            if self.history[-2] < self.low:
                prev_low = self.history[-2]
                prev_high = self.high
            elif self.history[-2] > self.high:
                prev_low = self.low
                prev_high =self.history[-2]
            if self.high - self.low > (prev_high - prev_low)/3:
                return self.random_guess()
            else:
                return self.onethree_guess()
        except: #self.history[-2]が存在しない時
            return self.random_guess()

    def switch_three_guess(self):
        if len(self.history) > 5:
            return self.half_guess()
        elif len(self.history)//2 == 0:
            return self.twothree_guess()
        else:
            return self.onethree_guess()

    def switch_three_random(self):
        if len(self.history) > 5:
            return self.random_guess()
        elif len(self.history)//2 == 0:
            return self.twothree_guess()
        else:
            return self.onethree_guess()

def main():
    test_range = 100 #int(input("Enter the test range. >> "))
    trial = 1000 #int(input("Enter how many times you want to test. >> "))
    
    player = NewPlayer()

    player.gamecenter(test_range, trial, player.interpreter("random_guess"))
    player.gamecenter(test_range, trial, player.interpreter("half_guess"))
    player.gamecenter(test_range, trial, player.interpreter("designed_guess_halfstart"))
    player.gamecenter(test_range, trial, player.interpreter("designed_guess_randomstart"))
    player.gamecenter(test_range, trial, player.interpreter("designed_guess_randomfirst"))
    player.gamecenter(test_range, trial, player.interpreter("designed_guess_halffirst"))
    player.gamecenter(test_range, trial, player.interpreter("onethree_guess"))
    player.gamecenter(test_range, trial, player.interpreter("onethree_random_guess"))
    player.gamecenter(test_range, trial, player.interpreter("twothree_random_guess"))
    player.gamecenter(test_range, trial, player.interpreter("random_onethree_guess"))
    player.gamecenter(test_range, trial, player.interpreter("switch_three_guess"))
    player.gamecenter(test_range, trial, player.interpreter("switch_three_random"))


if __name__ == '__main__':
    main()