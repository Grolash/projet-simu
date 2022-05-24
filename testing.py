# Testing the consistency of the digits of pi
import matplotlib.pyplot as plt
from chisq import chisq, generated_quantities
from poker import poker_test
from collector2 import collector_test
from shuffle_generator import ShuffleGenerator
from utils import display_results 
# from displacement_generator import DisplacementGenerator

if __name__ == "__main__":

    gen = ShuffleGenerator()
    # gen = TimeGenerator()
    # gen.index = 0
    # gen = WeylGenerator()
    # gen = DisplacementGenerator()
    gen.seed = 0 # For consistency
    # random.seed(0)

    # print(gen.seed)

    # first = gen.next()
    # second = gen.next()

    # flag = True
    # n = 1
    # while flag:
    #     value = gen.next()
    #     if value == first:
    #         flag = False
    #     n += 1

    # print(n)
    # print(second)
    # print(gen.next())


    generated_list = [str(gen.next()) for _ in range((10**6))]
    
    quantities = generated_quantities(generated_list)
    res, generated, expected, labels = chisq(quantities, [0.1 for _ in range(10)])

    plt.bar(labels, generated)
    plt.axhline(expected[0], color="red", label="Expected value")
    plt.ylim(min(generated)-100, max(generated)+100)
    plt.legend()

    display_results(res)

    # # plt.savefig("./outputs/mersenne_histogram_chisq", dpi=200)
    # plt.cla()
    plt.show()

    handsize = len(generated_list[0])
    res, generated, expected, labels = poker_test(generated_list, handsize)

    plt.bar(labels, generated, alpha=0.5, label="Real sample count")
    plt.bar(labels, expected, alpha=0.5, color="red", label="Expected sample count")
    plt.ylim(min(generated)-100, max(generated)+100)
    plt.legend()


    display_results(res)

    # # plt.savefig("./outputs/mersenne_histogram_poker", dpi=200)
    # plt.cla()
    plt.show()

  
    res, generated, expected, labels = collector_test(generated_list)
    labels[-1] += "+"

    plt.bar(labels, generated, alpha=0.5, label="Real sample count")
    plt.bar(labels, expected, alpha=0.5, color="red", label="Expected sample count")
    plt.legend()

    display_results(res)


    # plt.savefig("./outputs/mersenne_histogram_poker", dpi=200)
    # plt.cla()

    plt.show()
