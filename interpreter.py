# from tokenizer import paren, break_on_spaces, pulverize

"""
grouping

'	symbols (like enumerated types but global, to avoid passing strings)
"	strings
{}
[]	list shit
()	order of operations


infixes

math	 * - + / // % ^
range 	 ..
compare	 = < >
&	noodle the 'and' groups ie (where >2 & odd)
|	noodle the 'or' groups ie (where multiple 3|5)
"""


class _atom:
    pass

class inert(_atom):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return '{}<{}>'.format(type(self.val), self.val)


lookup = {}

class f_atom(_atom):
    def __init__(self, name, func):
        self.name = name
        self.func = func
        lookup[self.name] = self

    def __call__(self, *args, **kwargs):
        return self.func(*args)

    def __str__(self):
        return self.r.format(self.name)

class prefix(f_atom):
    r = ' {}_'

class suffix(f_atom):
    r = '_{} '

class infix(f_atom):
    r = '_{}_'


infix('+', lambda x, y: x+y)
prefix('sum', sum)
infix('..', range)
infix('print', lambda s: print(s))



def _to_atom(val):
    if val in lookup:
        return lookup[val]
    return inert(eval(val))


def reduce_new_lines(text, indent=4):
    lines = [line for line in text.split('\n') if line]
    indents = []

    for line in lines:
        depth = 0
        for c in line:
            if c == ' ': depth += 1
            else: break
        indents.append(depth)

    for i, this in enumerate(indents):
        prev = indents[i-1] if i else 0
        next = indents[i+1] if i < len(indents) else 0

        if next > this: # don't finish
            pass
        if next < this: # then do the finish
            pass





class Atomizer:
    def __init__(self, text):
        self.text = text
        self.structure = []





#
#
# while True:
#     atomize(input('> '))
#

def mult(n):
    out = lambda s: print(('{:>' + str(len(str(n**2))+1) + '}').format(s), end='')

    out('')
    for i in range(n):
        out(i)
    print()
    for j in range(n):
        out(j)
        for i in range(n):
            out(i*j)
        print()

mult(30)