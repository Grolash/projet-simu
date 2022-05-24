import datetime

from pi import get_digits


class TimeGenerator:
    def __init__(self):
        self.index = datetime.datetime.now().microsecond % 100000
        self.pi = get_digits()

    def next(self):
        random = ''
        for i in range(10):
            random += self.pi[(i + self.index)%(len(self.pi))]
            self.index += 1
            if self.index >= 1000000:
                self.index = 0
        return int(random)
