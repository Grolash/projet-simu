from math import floor

sterling_dict = {}

def sterling(k, r):

    if k == 1 or k == r:
        return 1

    res = sterling_dict.get(k, r)
    if res == None:
        res = sterling(k-1, r-1) + r * sterling(k-1, r)
        sterling_dict[(k, r)] = res

    return res



def integer_splitter(value, d):
    if not (0 <= value <= 9): raise ValueError("This splitter only accepts integer values between 0 and 9")
    return value

def interval_splitter(value, d):
    if not(0 <= value < 1): raise ValueError("This splitter only accepts float values between 0 and 1")
    return floor(value*d)