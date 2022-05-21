"""
Takes in a list containing the generated and expected counts
for each value, and uses them to calculate the value used in chi² test

"""
from scipy.stats import chi2

alphas = [0.1, 0.05, 0.01, 0.001]
critical_levels = {0.1: 14.684, 0.05: 16.919, 0.01: 21.666, 0.001: 27.877}


def chisq(generated, expected):
    if len(generated) != len(expected):
        raise ValueError("Lists of different sizes")

    chi_value = 0
    for n in range(len(generated)):
        genn = generated[n]
        expn = expected[n]

        if genn < 5 or expn < 5:
            list_name = "expected list" if expn < 5 else "generated list"
            raise ValueError(f"Number of samples <5 in the {list_name} at position {n}")

        chi_value += (expn - genn) ** 2 / expn

    degree_of_william_wallace = len(generated)

    results = {}
    for alpha in alphas:
        results[alpha] = (chi_value, critical_levels[alpha], chi_value < critical_levels)
    return results


def distribution(digit_list):
    distribution_list = [0 for i in range(10)]
    for d in digit_list:
        distribution_list[digit_list[d]] += 1
    return distribution_list
