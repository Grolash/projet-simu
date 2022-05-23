from math import factorial

from chisq import chisq
from pi import get_digits
from utils import sterling


def get_cover_generated(generation, precision):
    len_cover = 0
    categories = [0 for _ in range(10 * precision)]
    while 0 in categories:
        categories[int(str(generation)[2:precision])] += 1
        len_cover += 1
    return len_cover

def get_cover_gen_distr(generation, precision=1):
    """
    This algorithm seems in O(n^3) but in fact each "failure" to fill categories[key] contributes to fill
    categories[other key]. By the time categories[key] > 10, most categories[other key] are at least partially filled.
    :param generation: method of generation
    :param precision: number of digits to consider while making categories
    :return: the cover distribution of the generation process
    """
    categories = [0 for _ in range(30)]
    for index in categories[:30]:
        while categories[index] < 10:
            cover_len = get_cover_generated(generation, precision)
            categories[cover_len] += 1
    return categories

def get_cover_pi_distr(pi_digits):
    """
    This algorithm seems in O(n^3) but in fact each "failure" to fill categories[key] contributes to fill
    categories[other key]. By the time categories[key] > 10, most categories[other key] are at least partially filled.
    :param pi_digits: list of 1 million digits of pi
    :return: the cover distribution of pi digits
    """
    covers = [0 for _ in range(30)]
    pi_index = 0
    for index in covers[:30]:
        while covers[index] < 10:
            cover_len = 0
            categories = [0 for i in range(10)]
            while 0 in categories:
                categories[int(pi_digits[pi_index])] += 1
                cover_len += 1
                pi_index += 1
            covers[cover_len] += 1

    return covers

def get_distr_prob(size_distr):
    """
    Computes the probability
    :param size_distr:
    :return:
    """
    categories = []
    for t in range(10, size_distr):
        categories[t] = 1 - sterling(t-1, 10) * factorial(10) / 10**(t-1)
    return categories

def collector_test(generation, precision=1):
    if generation is "pi":
        generated = get_cover_pi_distr(get_digits())
        expected = get_distr_prob(len(generated))

    else:
        generated = get_cover_gen_distr(generation, precision)
        expected = get_distr_prob(len(generated))

    chisq(generated, expected)
