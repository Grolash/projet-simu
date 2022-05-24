import datetime

from pi import get_digits


class TimeGenerator:
    def __init__(self):
        self.index = datetime.datetime.now().microsecond % 100000

    def next(self):
        random = ''
        for i in range(6):
            random += get_digits()[i + self.index]
            self.index += 1
            if self.index >= 1000000:
                self.index = 0
        return int(random)
