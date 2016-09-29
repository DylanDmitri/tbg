from time import time
import random

# for algorithms class


# doot >> print "harambe died for our sins"


def test(func):
    while True:
        print(func(*map(eval, input(':').split())))
    return func


def compare(data, *funcs):
    r = []
    for func in funcs:
        s = time()
        for part in data:
            func(part)
        r.append( time()-s )
    return r


def my_max1(A):
    max = A[0]
    for element in A:
        if element > max:
            max = element
    return max

def my_max2(A):
    max = A[0]
    for element in A[1:]:
        if element > max:
            max = element
    return max

def my_max3(A):
    max = -float('inf')
    for element in A:
        if element > max:
            max = element
    return max

data = []

mymax = []
dmax = []

DOOT = 15
iteration = 0
for num, j in zip(range(DOOT)[::-1], range(DOOT)):
    num = 3**num
    j = 3**j
    for _ in range(num):
        part = []
        for _ in range(j):
            part.append(random.choice(range(100)))
        data.append(part)
    print(iteration, *compare(data, max, my_max1, my_max2, my_max3), sep='\t')
    iteration += 1

