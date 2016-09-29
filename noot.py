data = open('doto.txt', 'r').read()
heroes = {}

class Hero:
    def __init__(self, txt):
        lines = txt.split('\n')
        heroes[lines[0]] = self
        self.pickrate = lines[1::2]
        self.winrate = lines[2::2]

        self.increasing = self._increasing()

    def __str__(self):
        r=''
        def col(*args): return ''.join(a.ljust(15) for a in args) + '\n'
        r += col('1k', '2k', '3k', '4k', '5k')
        r += col(*self.pickrate)
        r += col(*self.winrate)
        return r

    def _increasing(self):
        return all(max(doot) == doot[-1] for doot in )


for h in data.split('\n\n'): Hero(h)

print(heroes['Razor'])

