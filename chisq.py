

alphas = [0.1, 0.05, 0.01, 0.001]
critical_levels = {9: {0.1: 14.684, 0.05: 16.919, 0.01: 21.666, 0.001: 27.877},
                   5: {0.1: 9.236, 0.05: 11.070, 0.01: 15.086, 0.001: 20.515}}




def chisq(generated, probabilities):
    """
    Takes in a list containing the generated and expected counts
    for each value, and uses them to calculate the value used in chi² test
    """

    if len(generated) != len(probabilities):
        raise ValueError("Lists of different sizes")



    chi_value = 0
    for n in range(len(generated)):
        genn = generated[n]
        expn = probabilities[n]

        if genn < 5 or expn < 5:
            list_name = "expected list" if expn < 5 else "generated list"
            raise ValueError(f"Number of samples <5 in the {list_name} at position {n}")

        chi_value += (expn - genn) ** 2 / expn

    liberty = len(generated)-1
    if liberty not in levels.keys(): raise ValueError("Unsupported degree of liberty")
    levels = critical_levels[liberty]

    results = {}
    for alpha in alphas:
        results[alpha] = (chi_value, levels[alpha], chi_value < levels[alpha])
    return results


# TODO: This will need to go in the pi-testing part
def generated_quantities(digit_list):
    distribution_list = [0 for i in range(10)]
    for d in digit_list:
        distribution_list[digit_list[d]] += 1
    return distribution_list



def expected_quantities(generated, probabilities):
    """
    Takes in the expected probabilities and outputs them times the adjusted to the size of generated data
    """
    total = sum(generated)
    expected = [total * prob for prob in probabilities]
    return expected

