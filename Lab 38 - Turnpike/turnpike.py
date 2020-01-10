# Hunter Casillas

import bisect

def delta_y(y, x):
    delta = []
    for el in x:
        diff = abs(y - el)
        bisect.insort(delta, diff)
    return delta


def sublist(lst1, lst2):
    return set(lst1) <= set(lst2)


def place(list_l, x, width):
    list_l = sorted(list_l)
    if len(list_l) == 0:
        toprint = ''
        for el in x:
            toprint += str(el) + ' '
        print(toprint)
        exit()
    y = list_l[-1]
    y_delta = delta_y(y, x)
    if sublist(y_delta, list_l):
        bisect.insort(x, y)
        for el in y_delta:
            list_l.remove(el)
        place(list_l, x, width)
        x.remove(y)
        for el in y_delta:
            bisect.insort(list_l, el)
    wy = width - y
    wy_delta = delta_y(wy, x)
    if sublist(wy_delta, list_l):
        bisect.insort(x, wy)
        for el in wy_delta:
            list_l.remove(el)
        place(list_l, x, width)
        x.remove(wy)
        for el in wy_delta:
            bisect.insort(list_l, el)
    return x


def partial_digest(list_l):
    list_l = sorted(list_l)
    width = list_l[-1]
    list_l.remove(width)
    x = [0, width]
    place(list_l, x, width)
    return


def turnpike(list_l):
    list_l = sorted([el for el in list_l if el > 0])
    partial_digest(list_l)
    return


def get_input(path):
    with open(path) as input_data:
        list_ll = list(map(int, input_data.readline().split(' ')))
    return list_ll


data = get_input("rosalind_ba4m.txt")
turnpike(data)
