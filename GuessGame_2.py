import random

class Player:
    def interpreter(self, func_name):
        if func_name == self.random_guess.__name__:
            return self.random_guess
        elif func_name == self.half_guess.__name__:
            return self.half_guess
    
    def renew(self, tpl):
        if tpl[0] == -1:
            self.low = tpl[1]+1
        elif tpl[0] == 1:
            self.high = tpl[1]-1

    def random_guess(self):
        tmp = random.randint(self.low, self.high)
        self.history.append(tmp)
        return tmp
    
    def half_guess(self):
        tmp = (self.low + self.high)//2 
        while tmp in self.history:
            tmp += 1
        self.history.append(tmp)
        return tmp
    
    def gamecenter(self, test_range, trial, func):
        result = []
        for i in range(test_range):
            tmp = []
            answer = i + 1
            for j in range(trial):
                self.low = 1
                self.high = test_range
                self.history = []
                counter = 1
                while True:
                    q = judge(answer, func())
                    if q[0] == 0:
                        tmp.append(str(counter))
                        break
                    else:
                        self.renew(q)
                        counter += 1
            result.append("\t".join(tmp))
        print("{} finished".format(func.__name__))
        with open("./results/{}_result.txt".format(func.__name__), "w") as f:
            f.write("\n".join(result)) 

def judge(ans, que):
    if que == ans:
        return (0, 0)
    elif que < ans:
        return (-1, que)
    else:
        return (1, que)

def main():
    test_range = 100 #int(input("Enter the test range. >> "))
    trial = 1000 #int(input("Enter how many times you want to test. >> "))
    
    player = Player()

    player.gamecenter(test_range, trial, player.interpreter("random_guess"))
    player.gamecenter(test_range, trial, player.interpreter("half_guess"))
    


if __name__ == '__main__':
    main()

