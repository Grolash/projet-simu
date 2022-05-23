from scipy.stats import chi2

alphas = [0.1, 0.05, 0.01, 0.001]


def adjust_sizes(generated, expected):
    """
    Adjust sample sizes so that they're all >=5
    """

    gen = [0]
    exp = [0]
    i = 0
    for n in range(len(generated)):
        gen[i] += generated[n]
        exp[i] += expected[n]
        if gen[i] >= 5 and exp[i] >= 5:
            i += 1
            if n < len(generated)-1:
                gen.append(0)
                exp.append(0)

    last = len(gen)-1
    if (gen[last] < 5 or exp[last] < 5) and last > 0:
        gen[last-1] += gen[last]
        exp[last-1] += exp[last]
        gen.pop()
        exp.pop()

    # if everything else fails, raise an error
    for n in range(len(gen)):
        genn = gen[n]
        expn = exp[n]
        if genn < 5 or expn < 5:
            raise ValueError(f"Failed to merge enough classes")

    return gen, exp

def chisq(generated, probabilities):
    """
    Takes in a list containing the generated and expected counts
    for each value, and uses them to calculate the value used in chi² test
    """
    
    expected = expected_quantities(generated, probabilities)
    return chisq_unprocessed(generated, expected)


def chisq_unprocessed(generated, expected):

    if len(generated) != len(expected):
        raise ValueError("Lists of different sizes")

    generated, expected = adjust_sizes(generated, expected)

    # print(generated)
    # print(expected)

    chi_value = 0
    for n in range(len(generated)):
        genn = generated[n]
        expn = expected[n]

        """if genn < 5 or expn < 5:
            list_name = "expected list" if expn < 5 else "generated list"
            raise ValueError(f"Number of samples <5 in the {list_name} at position {n}")"""

        chi_value += (expn - genn) ** 2 / expn

    liberty = len(generated)-1

    results = {}
    for alpha in alphas:
        critical_level = chi2.ppf(1-alpha, liberty)
        results[alpha] = (chi_value, critical_level, chi_value < critical_level)
    return results, generated, expected #the last two are here for convenience in making the histograms


# TODO: This will need to go in the pi-testing part
def generated_quantities(digit_list):
    distribution_list = [0 for i in range(10)]
    for d in digit_list:
        distribution_list[int(d)] += 1
    return distribution_list


def expected_quantities(generated, probabilities):
    """
    Takes in the expected probabilities and outputs them times the adjusted to the size of generated data
    """
    total = sum(generated)
    # total_prob = sum(probabilities)
    # print(generated)
    # print(total) #TODO REMOVE
    expected = [total * prob for prob in probabilities]
    # expected = [total * prob / total_prob for prob in probabilities]
    return expected

