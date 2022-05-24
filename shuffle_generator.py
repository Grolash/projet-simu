import datetime

from pi import get_digits
from itertools import permutations as p


N = 7 # Digit precision

class ShuffleGenerator:
    def __init__(self):
        self.seed = datetime.datetime.now().microsecond % 100000
        self.pi = get_digits()
        self.index = 0
        # self.permutations = list(p(range(N)))
        # self.shuffle = 0
        # print(len(self.permutations))

    def next(self, digits=True):
        digits = ''
        for i in range(N):
            d = self.pi[(self.index+self.seed+i**2)%(len(self.pi))]
            # if self.neg : d = str(9 - int(d))

            digits += d
            self.index += 1
            if self.index >= 10**6:
                self.index = 0
        #         self.shuffle = (self.shuffle+877)%len(self.permutations)
        
        # shuffled = ""
        # for pos in self.permutations[self.shuffle]:
        #     shuffled += digits[pos]

        # digits = shuffled

        if digits: return digits
        else: return float("0."+digits)