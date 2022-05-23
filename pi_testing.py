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

        plt.savefig("./outputs/pi_histogram", dpi=200)
        plt.cla()
        # plt.show()

        print(res)

    res, generated, expected = poker_test([int(pi_list[i*5 : (i+1)*5]) for i in range((10**6)//5)])
    # print(res)

    # res, generated, expected = collector_test("pi", precision=1)



