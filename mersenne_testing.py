# Testing the consistency of the digits of pi
from unittest import result
import matplotlib.pyplot as plt
from chisq import chisq, generated_quantities
from poker import poker_test
from collector2 import collector_test 
import random

from utils import display_results

if __name__ == "__main__":

    random.seed(0)

    mersenne_list = [str(random.random())[2:12] for _ in range((10**6))]

    quantities = generated_quantities(mersenne_list)
    res, generated, expected, labels = chisq(quantities, [0.1 for _ in range(10)])

    plt.bar(labels, generated)
    plt.axhline(expected[0], color="red", label="Expected value")
    plt.ylim(min(generated)-100, max(generated)+100)
    plt.legend()

    display_results(res)

    # plt.savefig("./outputs/mersenne_histogram_chisq", dpi=200)
    # plt.cla()
    plt.show()


    handsize = len(mersenne_list[0])
    print(handsize)
    res, generated, expected, labels = poker_test(mersenne_list, handsize)


    plt.bar(labels, generated, alpha=0.5, label="Real sample count")
    plt.bar(labels, expected, alpha=0.5, color="red", label="Expected sample count")
    plt.legend()

    # plt.savefig("./outputs/mersenne_histogram_poker", dpi=200)
    # plt.cla()

    display_results(res)

    plt.show()

    res, generated, expected, labels = collector_test(mersenne_list)

    # print(generated)
    # print(expected)

    plt.bar(labels, generated, alpha=0.5, label="Real sample count")
    plt.bar(labels, expected, alpha=0.5, color="red", label="Expected sample count")
    plt.legend()

    # plt.savefig("./outputs/mersenne_histogram_poker", dpi=200)
    # plt.cla()

    display_results(res)

    plt.show()



