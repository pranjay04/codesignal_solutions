from itertools import product, filterfalse
def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return sorted(list(filterfalse( lambda x: int(x)%d != 0, map(lambda i : createNumber(i), product(digits,repeat = k)))))
