from math import factorial as f

dico = {}

def sterling(k, r):

    # formula from: https://keisan.casio.com/exec/system/1292214964
    return sum((-1)**(r-i)*(f(r)/(f(i)*f(r-i)))*i**k for i in range(r+1)) / f(r)


    # Reaches recursion limit

    # if r == 1 or k == r:
    #     return 1

    # global dico

    # print(dico)

    # res = dico.get((k, r))
    # if res == None: 
    #     res = sterling(k-1, r-1) + r * sterling(k-1, r)
    #     dico[(k, r)] = res

    # return res