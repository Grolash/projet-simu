import datetime

from pi import get_digits
from itertools import permutations as p


N = 7 # Digit precision
M = 3 # Making this too big makes the results much worse, it's a period/quality tradeoff 
      # 3 seems the best, 5 has a significant dropoff


class HashGenerator:
    def __init__(self):
        self.seed = datetime.datetime.now().microsecond % 100000
        self.pi = get_digits()
        self.index = 0

    def next(self, digits=True):
        digits = ''

        for i in range(N):
            i = N*(self.index%M)+i

            d = self.pi[(self.index//M+self.seed+i**2)%(len(self.pi))]

            # Surprisingly, this improves test results,
            # seems to mitigate to amplification of the minor 
            # imbalance of digit counts in pi
            if i % 2 == 1 : d = str(9 - int(d))

            digits += d
            self.index += 1
            # if self.index >= 10**6:
            #     self.index = 0

        if digits: return digits
        else: return float("0."+digits)