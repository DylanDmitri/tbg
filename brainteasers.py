from math import log

digits = [1, 2, 3, 4, 5]
target = 25


def aim():
    current = digits
    decimals = log(target, 10)
    lead = int(str(target)[0])

    spots = {
        spot: digits[spot]
        for spot in range(1, len(digits)-decimals)
    }

def doot():
    r = ''
    for i in range(len(ops)):
        r += str(digits[i])
        r += ops[i]
    r += str(digits[-1])
    print(eval(r))

doot()


1 + 23 - 4 + 5
1 - 23 + 45