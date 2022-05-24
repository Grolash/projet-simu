from scipy.stats import chi2

alphas = [0.1, 0.05, 0.01, 0.001]


def adjust_sizes(generated, expected, label):
    """
    Adjust sample sizes so that they're all >=5
    """

    gen = [0]
    exp = [0]
    lab = [""]
    i = 0
    for n in range(len(generated)):
        gen[i] += generated[n]
        exp[i] += expected[n]
        lab[i] += label[n] if lab[i] == "" else ","+label[n]
        if gen[i] >= 5 and exp[i] >= 5:
            i += 1
            if n < len(generated)-1:
                gen.append(0)
                exp.append(0)
                lab.append("")

    last = len(gen)-1
    if (gen[last] < 5 or exp[last] < 5) and last > 0:
        gen[last-1] += gen[last]
        exp[last-1] += exp[last]
        lab[last-1] += lab[last]
        gen.pop()
        exp.pop()
        lab.pop()

    # if everything else fails, raise an error
    for n in range(len(gen)):
        genn = gen[n]
        expn = exp[n]
        if genn < 5 or expn < 5:
            raise ValueError(f"Failed to merge enough classes")

    return gen, exp, lab

def chisq(generated, probabilities, labels=None):
    """
    Takes in a list containing the generated and expected counts
    for each value, and uses them to calculate the value used in chi² test
    """
    
    expected = expected_quantities(generated, probabilities)
    return chisq_unprocessed(generated, expected, labels)


def chisq_unprocessed(generated, expected, labels=None):

    if len(generated) != len(expected):
        raise ValueError("Lists of different sizes")

    # print(generated)
    # print(expected)

    if labels == None : labels = [str(n) for n in range(1, len(generated)+1)]

    generated, expected, labels = adjust_sizes(generated, expected, labels)

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
    return results, generated, expected, labels #the last two are here for convenience in making the histograms


# TODO: This will need to go in the pi-testing part
def generated_quantities(digit_list):
    distribution_list = [0 for i in range(10)]
    for d in digit_list:
        distribution_list[int(str(d)[0])] += 1
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

