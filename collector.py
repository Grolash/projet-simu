from math import factorial

from chisq import chisq
from utils import stirling

def get_cover_gen_distr(values, precision=1, length_of_testing = 70):
    end = length_of_testing
    covers = [0 for _ in range(end+1)]
    index = 0
    while index < len(values):
        cover_len = 0
        categories = [0 for _ in range(10)]
        while (0 in categories) & (index < len(values)):
            i = int(str(values[index])[:precision])
            categories[i] += 1
            cover_len += 1
            index += 1
        if cover_len >= end:
            covers[end] += 1
        elif cover_len >= 10: covers[cover_len] += 1

    return covers


def get_distr_prob(size_distr):
    """
    Computes the probability
    :param size_distr:
    :return:
    """
    categories = [(p(r)-p(r-1)) for r in range(size_distr-1)]
    categories.append(1-stirling(size_distr-2, 10)*factorial(10)/(10**(size_distr-2)))
    return categories

def p(r):
    if r < 10:
        return 0
    return stirling(r, 10)*factorial(10)/(10**r)

def q(r):
    if r < 10:
        return 0
    return 1 - (stirling(r, 10) * factorial(10) / (10 ** r))


def collector_test(values, precision=1, length_of_testing = 70):
    generated = get_cover_gen_distr(values, precision, length_of_testing)
    expected = get_distr_prob(len(generated))
    labels = [str(n+10) for n in range(len(generated))]
    
    return chisq(generated[10:], expected[10:], labels)
