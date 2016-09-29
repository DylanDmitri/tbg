def r(a, s):
    assert a[0] == 'r'
    return s.registers[int(a[1:])]


def l(a, s):
    assert a.isdigit()
    return int(a)


def f(a, s):
    assert a in s.label_map
    return s.label_map[a]


funcs = {}


class Function:
    def __init__(self, name, action, *fields):
        # where f1, f2, f3 are the three is_ functions above
        funcs[name] = name
        self.fields = fields
        self.action = action
        self.params = []

    def run(self, board, *fs):
        assert len(fs) == len(self.fields)
        self.params = tuple(map(self.fields, fs))
        self.action(*self.params)

def asCommand(*fields):
    def temp(f):
        Function(f.__name__, f, *fields)
    return temp


@asCommand(r, r, r)
def add(a, b, c):  a[0] = b[0] + c[0]


@asCommand(r, r, l)
def addi(a, b, c): a[0] = b[0] + c


@asCommand(r, r, r)
def sub(a, b, c): a[0] = b[0] - c[0]


@asCommand(r, r, l)
def subi(a, b, c): a[0] = b[0] - c



class InstructionSet:
    def __init__(self, filename):
        txt = list(open(filename, 'r').read().split('\n'))
        self.pointer = 0

        self.label_map = {}
        for i, line in enumerate(txt):
            if line[-1] == ':':
                self.label_map[line[:-1]] = i

        self.instructions = [line for line in txt if line and ':' not in line]

    def active(self):
        return self.instructions[self.pointer]


class Board:
    def __init__(self, filename):
        self.registers = [[0] for _ in range(23)]
        self.instructions = InstructionSet(filename)

    def step(self):
        to_execute = self.instructions.active()

        instr, f1, f2, f3 = to_execute.split()

        funcs[instr].run(self, f1, f2, f3)

    def __str__(self):
        return str(self.registers)


b = Board()





