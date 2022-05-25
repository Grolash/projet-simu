from math import factorial
from chisq import chisq
from utils import stirling

def poker_test(values, k=None):
    """
    Poker test, values imputed must be multiplied bu 10**k beforehand
    """

    d = 10
    if k == None : k = len(str(values[0]))

    generated = [0 for _ in range(k)]
    for value in values:
        buckets = [0 for _ in range(d)]
        for digit in value:
            buckets[int(digit)] += 1
        r = 0
        for bucket in buckets:
            if bucket > 0:
                r += 1
        generated[r-1] += 1

    expected = [(stirling(k, r) * factorial(d)) / (factorial(d-r) * d**k) for r in range(1, k+1)]

    return chisq(generated, expected)