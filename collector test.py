from utils import sterling


def get_cover(generation, precision):
    len_cover = 0
    categories = [0 for i in range(10*precision)]
    while 0 in categories:
        categories[int(str(generation)[2:precision])] += 1
        len_cover += 1
    return len_cover


