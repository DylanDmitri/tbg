from time import time
from random import randint


def calc():
    total = 0
    num = 1
    sign = 1
    while True:
        change = sign*(1/num)
        input('{} {} 1/{} = {}'.format(total, '+' if sign>0 else '-', num, total+change))
        total += change
        num += 2
        sign *= -1

calc()



def get_good(s):
    print('write:', s)
    n = ''
    while n != s:
        n = input(':')

class Card:
    def __init__(self, question, answer):
        self.q = question
        self.a = answer
        self.times = [60, 60, 60, 60, 60]

    def run(self):
        s = time()
        print()
        u = input(self.q)
        if u == self.a:
            self.times.append(time()-s)
            print('correct!')
        else:
            self.times.append(60)
            print('nope --', self.a, '--')
            s = self.q[:3]+self.a
            get_good(s + ' ' + s + ' ' + s)


    @property
    def doot(self):
        return int(sum(a*b for a, b in zip(self.times[-(min(5, len(self.times))):], range(5))))

class Deck:
    def __init__(self, cards):
        self.cards = cards
        self.prev = [-1, -1, -1]

    def total(self):
        return sum(card.doot for card in self.cards)

    def run(self):
        total = self.total()
        while True:
            spot = randint(1, total)
            stoodlee = 0
            for i, card in enumerate(self.cards):
                stoodlee += card.doot
                if stoodlee > spot:
                    if i in self.prev:
                        break
                    card.run()
                    self.prev.append(i)
                    self.prev.pop(0)
                    return


    def play(self):
        while True:
            self.run()


cards = []
for i in range(18, 25):
    j = i
    cards.append(Card('{} x {} = '.format(i, j), str(i*j)))
Deck(cards).play()





