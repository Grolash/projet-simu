import datetime

from pi import get_digits


class WeylGenerator:

    def __init__(self):
        self.seed = 0
        self.update_seed()
        # seed must begin with 1 and end with 1 (ex: 100000000001)
        self.x = 0
        self.w = 0
        self.iter = 0

    def next(self):
        self.iter += 1
        # if self.iter >= 20:
        #     self.update_seed()
        self.x = self.x * self.x % 1000000
        self.w += self.seed % 1000000
        self.x += self.w % 1000000
        self.x = int(str(self.x)[len(str(self.x))/2:] + str(self.x)[:len(str(self.x))/2])
        random = ''
        for i in range(6):
            random += get_digits()[i + self.x]
        return int(random)

    def update_seed(self):
        self.seed = int('0' + str(bin(datetime.datetime.now().microsecond % 100000))[2:] + '1', 2)
