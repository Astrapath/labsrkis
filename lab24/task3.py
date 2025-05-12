from enum import Enum
class Operation(Enum):
    add = 1
    sub = 2
    mult = 3
    div = 4
def calc(a, b, op):
    result = 0
    match op:
        case Operation.add:
            result = a + b
        case Operation.sub:
            result = a - b
        case Operation.mult:
            result = a * b
        case Operation.div:
            result = a / b
    return a, b, op, result
a = int(input('Введите А: '))
b = int(input('Введите B: '))
op_text = input("выберите операцию(от 1 до 4): ");
op = Operation[op_text.upper()]
print(calc(a, b, op))