import datetime

from pi import get_digits


class TimeGenerator:

    def next(self):
        index = datetime.datetime.now().microsecond % 100000
        random = ''
        for i in range(6):
            random += get_digits()[i + index]
        return int(random)
