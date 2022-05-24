import datetime

from pi import get_digits


class DisplacementGenerator:

    def __init__(self, seed=None):
        if seed == None:
            seed = datetime.datetime.now().microsecond % 1000000
        self.seed = seed
        self.n = seed
        self.pi = get_digits()
        self.offset = 300007# TODO: Find a good manner to calclulate the offset, static offset is a pretty bad idea overall

    def next(self):
        word = ""
        for i in range(10):
            word += self.pi[(self.n+i*self.offset)%1000000]
        self.n += 1
        return word