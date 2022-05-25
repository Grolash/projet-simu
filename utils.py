from math import factorial as f

dico = {}

def stirling(k, r):

    # formula from: https://keisan.casio.com/exec/system/1292214964
    return sum((-1)**(r-j) * (f(r)/(f(j)*f(r-j)))*j**k for j in range(r+1)) / f(r)


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


def print_results(results):
    for alpha in results.keys():
        print(f"Alpha value: {alpha}\tCritical value: {round(results[alpha][1], 3)}\t Calculated value: {round(results[alpha][0], 3)}\t Test result: {'Success' if results[alpha][2] else 'Fail'}")

def report_printer(results):
    for alpha in results.keys():
        print(f"{alpha} & {round(results[alpha][1], 3)} & {round(results[alpha][0], 3)} & {'Réussi' if results[alpha][2] else 'Raté'} \\\\")