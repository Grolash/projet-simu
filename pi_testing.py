# Testing the consistency of the digits of pi
from unittest import result
import matplotlib.pyplot as plt
from chisq import chisq, generated_quantities
from poker import poker_test
from collector import collector_test 
from pi import get_digits

if __name__ == "__main__":

    pi_list = get_digits()

    if False:
        
        quantities = generated_quantities(pi_list)
        res, generated, expected = chisq(quantities, [0.1 for _ in range(10)])

        plt.bar([str(d) for d in range(10)], generated)
        plt.axhline(expected[0], color="red", label="Expected value")
        # plt.bar([str(d) for d in range(10)], [100000 for _ in range(10)], alpha=0.5, color="red")
        plt.ylim(min(generated)-100, max(generated)+100)
        plt.legend()

        plt.savefig("./outputs/pi_histogram_chisq", dpi=200)
        plt.cla()
        # plt.show()

        print(res)

    handsize = 10
    #res, generated, expected, labels = poker_test([pi_list[i*handsize : (i+1)*handsize] for i in range((10**6)//handsize)], handsize)
    res, generated, expected, labels = collector_test("pi")
    # print(generated)
    # print(expected)
    labels[-1] += "+"

    plt.bar(labels, generated, alpha=0.5, label="Real sample count")
    plt.bar(labels, expected, alpha=0.5, color="red", label="Expected sample count")
    # plt.ylim(min(generated)-100, max(generated)+100)
    plt.legend()

    # plt.savefig("./outputs/pi_histogram_poker", dpi=200)
    # plt.cla()

    plt.show()

    print(res)
