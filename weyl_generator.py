import datetime

from pi import get_digits


class WeylGenerator:
    def __init__(self):
        self.seed = int('Ob1' + bin(datetime.datetime.now().microsecond % 100000) + '1')
        # seed must begin with 1 and end with 1 (ex: 100000000001)
        self.x = 0
        self.w = 0

    def next(self):
        self.x = self.x * self.x % 1000000
        self.w += self.seed % 1000000
        self.x += self.w % 1000000
        self.x = int(str(self.x)[len(self.x)/2:] + str(self.x)[:len(self.x)/2])
        random = ''
        for i in range(6):
            random += get_digits()[i + self.x]
        return int(random)
