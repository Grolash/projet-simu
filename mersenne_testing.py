# Testing the consistency of the digits of pi
from unittest import result
import matplotlib.pyplot as plt
from chisq import chisq, generated_quantities
from poker import poker_test
from collector import collector_test 
import random

if __name__ == "__main__":

    random.seed(0)

    mersenne_list = [str(random.random())[2:12] for _ in range((10**6))]

    # if False:
        
    quantities = generated_quantities(mersenne_list)
    res, generated, expected, labels = chisq(quantities, [0.1 for _ in range(10)])

    plt.bar(labels, generated)
    plt.axhline(expected[0], color="red", label="Expected value")
    # plt.bar([str(d) for d in range(10)], [100000 for _ in range(10)], alpha=0.5, color="red")
    plt.ylim(min(generated)-100, max(generated)+100)
    plt.legend()

    # plt.savefig("./outputs/mersenne_histogram_chisq", dpi=200)
    # plt.cla()
    plt.show()

    print(res)

    handsize = len(mersenne_list[0])
    print(handsize)
    res, generated, expected, labels = poker_test(mersenne_list, handsize)

    print(generated)
    print(expected)

    plt.bar(labels, generated, alpha=0.5, label="Real sample count")
    plt.bar(labels, expected, alpha=0.5, color="red", label="Expected sample count")
    # plt.ylim(min(generated)-100, max(generated)+100)
    plt.legend()

    # plt.savefig("./outputs/mersenne_histogram_poker", dpi=200)
    # plt.cla()

    plt.show()

    print(res)



