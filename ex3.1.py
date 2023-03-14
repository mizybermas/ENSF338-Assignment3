import sys


def calculateInstance(num1: int, num2: int, operator: str) -> int:
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '/':
        return num1 / num2
    if operator == "*":
        return int(num1 * num2)


def calculateExpression(expression: str) -> int:
    operand_stack = []
    number_stack = []

    for i in range(len(expression)):
        if expression[i] == '(':
            operand_stack.append(expression[i+1])

        if expression[i].isnumeric():
            number_stack.append(int(expression[i]))

        if expression[i] == ')':
            operator = operand_stack.pop()
            number = number_stack.pop()

            number_stack[-1] = calculateInstance(
                number_stack[-1], number, operator)

    return int(number_stack[0])


print(calculateExpression(sys.argv[1]))
