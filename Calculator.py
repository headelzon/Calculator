import string
import operations


print('Welcome to WKalculator!')
print('Please input your equation.')

equation = input()
print(equation)
query = []
digits = set(string.digits)

for each in equation:
    query.append(each)

# print(query)
# print(digits)

operands = []
operands_working = []
operators = ['+', '-', '*', '/']
operators_working = []

for x in query:
    if x in digits:
        operands_working.append(x)
    elif x in operators:
        operand = ''.join(operands_working)
        operands.append(int(operand))
        operands_working = []
        operators_working.append(x)
    elif x == ' ':
        continue
    else:
        print('Error.')
        break

if operands_working != []:
    operand = ''.join(operands_working)
    operands.append(int(operand))
    operands_working = []

# print('operands_working: {}'.format(operands_working))
# print('operands: {}'.format(operands))
# print('operators_working: {}'.format(operators_working))

for x in operators_working:
    if x == '+':
        # Addition
        result = operations.add(operands[0], operands[1])
        operands.pop(0)     # remove operand 1
        operands.pop(0)     # remove operand 2
        operands.insert(0, result) # places the result of operation at the place of two used operands
    elif x == '-':
        # Subtraction
        result = operations.subtract(operands[0], operands[1])
        operands.pop(0)     # remove operand 1
        operands.pop(0)     # remove operand 2
        operands.insert(0, result) # places the result of operation at the place of two used operands
    elif x == '*':
        # Subtraction
        result = operations.multiply(operands[0], operands[1])
        operands.pop(0)     # remove operand 1
        operands.pop(0)     # remove operand 2
        operands.insert(0, result) # places the result of operation at the place of two used operands
    elif x == '/':
        # Subtraction
        result = operations.divide(operands[0], operands[1])
        operands.pop(0)     # remove operand 1
        operands.pop(0)     # remove operand 2
        operands.insert(0, result) # places the result of operation at the place of two used operands
    else:
        print('Error.')
        break


# print('operands_working: {}'.format(operands_working))
# print('operands: {}'.format(operands))

if len(operands) == 1:
    print('\n{} = {}'.format(equation, operands[0]))