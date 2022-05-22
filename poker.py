from math import factorial, floor
from chisq import chisq
from utils import sterling

def get_r(generated, splitter, d):
    """
    Finds the r value of the generated set
    generated is a small subset of size k, not the whole thing
    splitter should be the function that determines the bucket of a given value
    d is the number of buckets to split into
    """
    k = len(generated)
    buckets = [0 for _ in range(k)]

    for value in generated:
        buckets[splitter(value)] += 1

    r = 0
    for bucket in buckets:
        if bucket > 0:
            r += 1

    exp_r = (sterling(k, r) * factorial(d)) / (factorial(d-r) * d**k)

    return r, exp_r

def poker_test(values, k, d, splitter):

    if len(values) % k != 0:
        raise ValueError("The given value list is not a multiple of the given k value")

    generated = []
    expected = []
    for n in range(len(values)//k-1):
        gen, exp = get_r(values[n*k, (n+1)*k], splitter, d)
        generated.append(gen)
        expected.append(exp)

    return chisq(generated, expected)

def integer_splitter(value):
    if not (0 <= value <= 9): raise ValueError("This splitter only accepts integer values between 0 and 9")
    return value

def interval_splitter(value):
    if not(0 <= value < 1): raise ValueError("This splitter only accepts float values between 0 and 1")
    return floor(value*6)