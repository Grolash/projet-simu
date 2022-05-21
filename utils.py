sterling_dict = {}

def sterling(k, r):

    if k == 1 or k == r:
        return 1

    res = sterling_dict.get(k, r)
    if res == None:
        res = sterling(k-1, r-1) * r * sterling(k-1, r)
        sterling_dict[(k, r)] = res

    return res