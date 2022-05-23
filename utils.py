def sterling(k, r):

    if r == 1 or k == r:
        return 1

    res = sterling(k-1, r-1) + r * sterling(k-1, r)

    return res