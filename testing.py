# Testing the consistency of the digits of pi
import matplotlib.pyplot as plt
from chisq import chisq, generated_quantities
from poker import poker_test
from collector import collector_test
from hash_generator import HashGenerator, M
from utils import print_results 
from pi import get_digits
import random

GEN_COLOR = "#00688B"
# GEN_COLOR = "#3D59AB"
# EXP_COLOR = "#8B2048"
EXP_COLOR = "#80B030"

if __name__ == "__main__":

    DISPLAY = False # Switch this to show the plots instead of saving them

    gen = HashGenerator()
    # For consistency
    gen.seed = 0
    random.seed(0)

    methods = [
        {"name": "Digits of pi",
         "list": get_digits()},
        {"name": "Mersenne Twister",
         "list": [str(random.random())[2:9] for _ in range((M*10**6))]},
        {"name": "Pi-based generator",
         "list": [str(gen.next()) for _ in range((M*10**6))]}
         ]


    for method in methods:

        numbers = method["list"]
        name = method["name"]
        print("\n\t\t"+name+":")

        quantities = generated_quantities(numbers)
        res, generated, expected, labels = chisq(quantities, [0.1 for _ in range(10)], labels=[str(i) for i in range(10)])

        plt.figure(figsize=[15, 5])
        plt.title("Chi Squared Test for the "+name)
        plt.bar(labels, generated, color=GEN_COLOR)
        plt.bar(labels, expected, width=0.4, align="edge", color=EXP_COLOR, label="Expected sample count")
        # plt.bar(labels, expected, width=0.4, align="edge", color="red", label="Expected value")
        plt.ylim(min(generated)-100, max(generated)+100)
        plt.xlabel("Digit")
        plt.ylabel("Number of occurances")
        plt.legend()

        print("="*5+" Chi Squared Test results for "+name+" "+"="*5)
        print_results(res)

        if DISPLAY: plt.show()
        else: 
            plt.savefig("./outputs/"+name+" histogram chisq", dpi=200)
            plt.cla()

        handsize = len(numbers[0])
        if handsize == 1:
            # Means it's the pi digits list, this one needs more preporcessing done before giving it to the poker test
            handsize = 10 # A multiple of 10**6, so every digit is included in the test
            numbers2 = [numbers[i*handsize : (i+1)*handsize] for i in range((10**6)//handsize)]
        else: numbers2 = numbers

        res, generated, expected, labels = poker_test(numbers2, handsize)

        plt.title("Poker Test for the "+name)
        plt.bar(labels, generated, color=GEN_COLOR, label="Real sample count")
        plt.bar(labels, expected, width=0.4, align="edge", color=EXP_COLOR, label="Expected sample count")
        plt.xlabel("Distinct digits per hand served")
        plt.ylabel("Number of occurances")
        plt.legend()

        print("="*5+" Poker Test results for "+name+" "+"="*5)
        print_results(res)
        
        if DISPLAY: plt.show()
        else: 
            plt.savefig("./outputs/"+name+" histogram poker", dpi=200)
            plt.cla()
    
        res, generated, expected, labels = collector_test(numbers)
        labels[-1] += "+"

        plt.figure(figsize=[20, 5])
        plt.title("Coupon Collector Test for the "+name)
        plt.bar(labels, generated, color=GEN_COLOR, label="Real sample count")
        plt.bar(labels, expected, width=0.4, align="edge", color=EXP_COLOR, label="Expected sample count")
        plt.xlabel("Length of the sequence")
        plt.ylabel("Number of occurances")
        plt.legend()

        print("="*5+" Coupon Collector Test results for "+name+" "+"="*5)
        print_results(res)

        if DISPLAY: plt.show()
        else: 
            plt.savefig("./outputs/"+name+" histogram collector", dpi=200)
            plt.cla()