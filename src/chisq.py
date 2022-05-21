
"""
Takes in a list containting the generated and expected counts
for each value, and uses them to calculate the value used in chi² test

"""
def chisq(generated, expected):

    if len(generated) != len(expected):
        raise ValueError("Lists of different sizes")

    res = 0
    for n in range(len(generated)):
        genn = generated[n]
        expn = expected[n]

        if genn < 5 or expn < 5:
            list_name = "expected list" if expn < 5 else "generated list"
            raise ValueError(f"Number of samples <5 in the {list_name} at position {n}")

        res += (expn-genn)**2 / expn

    return res


