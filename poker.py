from math import factorial
from chisq import chisq_unprocessed
from utils import sterling

def poker_test(values, k=None):
    """
    Poker test, values imputed must be multiplied bu 10**k beforehand
    """

    d = 10
    if k == None : k = len(str(values[0]))

    generated = [0 for _ in range(k)]
    for value in values:
        value_digits = str(value)
        buckets = [0 for _ in range(d)]
        for digit in value_digits:
            buckets[int(digit)] += 1
        r = 0
        for bucket in buckets:
            if bucket > 0:
                r += 1
        generated[r-1] += 1

    expected = [(sterling(k, r) * factorial(d) * len(values)) / (factorial(d-r) * d**k) for r in range(1, k+1)]

    return chisq_unprocessed(generated, expected)