import datetime

from pi import get_digits


class TimeGenerator:
    def __init__(self):
        self.index = datetime.datetime.now().microsecond % 100000
        self.pi = get_digits()

    def next(self, digits=True):
        random = ''
        for i in range(7):
            random += self.pi[(i + self.index)%(len(self.pi))]
            self.index += 1
            if self.index >= 1000000:
                self.index = 0
        if digits: return random
        else: return float("0."+random)