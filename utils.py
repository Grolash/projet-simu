dico = {}

def sterling(k, r):

    if r == 1 or k == r:
        return 1

    global dico

    res = dico.get((k, r))
    if res == None: 
        res = sterling(k-1, r-1) + r * sterling(k-1, r)
        dico[(k, r)] = res

    return res