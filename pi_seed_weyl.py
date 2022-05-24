import datetime

from pi import get_digits


class PiSeedWeylGenerator:

    def __init__(self):
        self.seed = int('0b1' + str(bin(datetime.datetime.now().microsecond % 100000))[2:] + '1')
        self.pi = get_digits()
        self.pi_index = 0
        # self.update_seed()
        self.x = 0
        self.w = 0

    def next(self):
        self.x = self.x * self.x % 1000000
        self.w += self.seed % 1000000
        self.update_seed()
        self.x += self.w % 1000000
        self.x = int(str(self.x)[len(str(self.x)) / 2:] + str(self.x)[:len(str(self.x)) / 2])
        random = ''
        for i in range(6):
            random += get_digits()[i + self.x]
        return int(random)

    def update_seed(self):
        self.seed = [self.pi[i + self.pi_index] for i in range(6)]
        self.pi_index += 6
