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
    end = 40
    categories = [0 for _ in range(end+1)]
    for index in categories[10:end]:
        while categories[index] < 10:
            cover_len = get_cover_generated(generation, precision)
            if cover_len >= end:
                categories[end] += 1
            else: categories[cover_len] += 1
    return categories


def get_cover_pi_distr(pi_digits):
    """
    :param pi_digits: list of 1 million digits of pi
    :return: the cover distribution of pi digits
    """
    end = 40
    covers = [0 for _ in range(end+1)]  # 50 is arbitrary
    pi_index = 0
    while pi_index < 1000000:
        cover_len = 0
        categories = [0 for _ in range(10)]
        while (0 in categories) & (pi_index < 1000000):
            categories[int(str(pi_digits)[pi_index])] += 1
            cover_len += 1
            pi_index += 1
        if cover_len >= end:
            covers[end] += 1
        else: covers[cover_len] += 1

    return covers


def get_distr_prob(size_distr):
    """
    Computes the probability
    :param size_distr:
    :return:
    """
    categories = [(q(r-1)-q(r)) for r in range(size_distr-1)]
    categories.append(1-sterling(size_distr-2, 10)*factorial(10)/(10**(size_distr-2)))
    return categories


def q(r):
    if r < 10:
        return 0
    return 1 - (sterling(r, 10) * factorial(10) / (10 ** r))


def collector_test(generation, precision=1):
    if generation == "pi":
        generated = get_cover_pi_distr(get_digits())
        print(len(generated))
        print(generated)
        expected = get_distr_prob(len(generated))
        print(len(expected))
        print(expected)

    else:
        generated = get_cover_gen_distr(generation, precision)
        expected = get_distr_prob(len(generated))

    return chisq(generated[10:], expected[10:])
