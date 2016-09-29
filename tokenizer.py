
match = {'}':'{', ')':'(', ']':'['}


def paren(line, mine=None):
    r = []

    for c in line:

        if c == '([{':
            r.append(paren(line, c))
        elif c == ')]}':
            assert match[c] == mine
            return r
        else:
            if len(r) == 0 or not isinstance(r[-1],str):
                r.append('')
            r[-1] += c
    return r


def apply_at_depth(func, tree):
    for i, branch in enumerate(tree):
        if not isinstance(branch, list):
            tree[i] = func(branch)
        else:
            apply_at_depth(func, branch)


def break_on_spaces(tree):
    for i, branch in enumerate(tree):
        if not isinstance(branch, list):
            if ' ' in branch:
                tree[i] = branch.split()
        else:
            break_on_spaces(branch)


tokens = ('<-','->','!','*','-','+','//','/','%','^','..','=','<','>','&','|')
def _everyother(t,part):
    r = []
    for e in part.split(t):
        if e: r.append(e)
        r.append(t)
    return r[:-1]

def pulverize(tree):

    for i, branch in enumerate(tree):
        if not isinstance(branch, list):
            if branch not in tokens:
                part = [branch]
                for token in tokens:
                    temp = []
                    for piece in part:
                        temp.extend(_everyother(token,piece))
                    part = temp[:]
                if len(part) > 1: tree[i] = part
        else:
            pulverize(branch)



def delim(line):
    tree = paren(iter(line))
    print(tree)
    break_on_spaces(tree)
    print(tree)
    pulverize(tree)
    print(tree)
    return tree


m = ('(1+1) / 4',
     '3 * (1+ 2)',
     'sum 1..10',
     'sum 1..100 where multiple 3|5',
     '(result <- func) @ list!1..')

for foo in m:
    print()
    print(foo)
    delim(foo)