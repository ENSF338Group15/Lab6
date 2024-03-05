import sys
if len(sys.argv) > 1:
    exp = sys.argv[1]
else:
    print('Running test expression, if you wish to run with your own expression, run with a commandline argument')
    exp = [
        '5',
        '( 1 + 1 )',
        '( 6 – 3 ) * 4',
        '( ( ( 5 – 28 ) * 345 ) – ( 6 / 2 ) ) * 0'
    ][0]
exp = exp.split()

operator_dict = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '–': lambda a, b: a - b,  # Some minus signs in the example are not \U+002D
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

# Above code copied from Lab 5 ex1.py of our group


class Node:
    def __init__(self, op=None, left=None, right=None, value=None):
        self.op = op
        self.left = left
        self.right = right
        self.value = value

    def compute(self):
        if self.value is not None:
            return self.value
        if type(self.left) is Node:
            self.left = self.left.compute()
        if type(self.right) is Node:
            self.right = self.right.compute()
        left = self.left.value if type(self.left) is Node else self.left
        right = self.right.value if type(self.right) is Node else self.right
        self.value = operator_dict[self.op](left, right)
        return self.value

    def __str__(self):
        return f'Node({self.op}, {self.left}, {self.right})' + ('' if self.value is None else f' = {self.value}')


def split_expression(expression):
    if expression[0] == '(':
        bracket = 1
        for i, char in enumerate(expression[1:]):
            if char == '(':
                bracket += 1
            if char == ')':
                bracket -= 1
            if bracket == 0:
                if len(expression) == i+2:
                    return expression[1:i+1], None, None
                if expression[i+3] == '(':
                    return expression[1:i+1], expression[i+2], expression[i+4:-1]
                else:
                    return expression[1:i+1], expression[i+2], expression[i+3:]
    else:
        if expression[2] == '(':
            return expression[0], expression[1], expression[3:-1]
        else:
            return expression[0], expression[1], expression[2]


def build_tree(expression):
    if (type(expression) == list and len(expression) == 1) or type(expression) == str:
        return Node(value=int(expression[0]))
    if expression[1] is None:
        left, op, right = split_expression(expression[0])
        return Node(op, left, right)
    if expression[1] is not None:
        left, op, right = split_expression(expression)
        if op is None:
            left, op, right = split_expression(left)
        return Node(op, build_tree(left), build_tree(right))


tree = build_tree(exp)
tree.compute()
print(tree.value)
