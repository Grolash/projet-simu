from math import factorial
from chisq import chisq
from utils import sterling

def get_r(hand, precision):
    """
    Finds the r value of the given hand 
    hand is a small subset of the generated set, size k
    precision determines the number of buckets to split into
    """
    k = len(hand)
    d = 10**precision
    buckets = [0 for _ in range(d)]

    for value in hand:
        bucket = int(str(value)[:precision]) if isinstance(value, int) else int(str(value)[2:precision])
        buckets[bucket] += 1

    r = 0
    for bucket in buckets:
        if bucket > 0:
            r += 1

    # exp_r = (factorial(k) / (k**k * factorial(k-r) * sterling(r, k))) * (r/k) * (k - r)
    exp_r = (sterling(k, r) * factorial(d)) / (factorial(d-r) * d**k)

    acc = 0
    for r2 in range(d):
        acc+= (sterling(k, r2) * factorial(d)) / (factorial(d-r2) * d**k)
    print()

    return r, exp_r

def poker_test(values, k, precision):

    if len(values) % k != 0:
        raise ValueError("The given value list is not a multiple of the given k value")

    generated = []
    expected = []
    for n in range(len(values)//k-1):
        gen, exp = get_r(values[n*k : (n+1)*k], precision)
        generated.append(gen)
        expected.append(exp)

    # print(generated)
    # print(expected)

    return chisq(generated, expected)