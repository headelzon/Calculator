import string


print('Welcome to WKalculator!')
print('Please input your equation.')

equation = input()
print(equation)
query = []
digits = set(string.digits)

for each in equation:
    query.append(each)

print(query)
print(digits)

operands = []
operands_working = []
operators = ['+', '-', '*', '//']
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

results_working = [] # Used as stack

print('operands_working: {}'.format(operands_working))
print('operands: {}'.format(operands))
print('operators_working: {}'.format(operators_working))

for x in range(len(operators_working)):
    if operators_working[x] == '+':
        # Addition
        # result = add(operands[x], operands[x+1])
        # operands.pop(x) <-- remove operand 1
        # operands.pop(x+1) <-- remove operand 2
        # operands.insert(0, result) <-- places the result of operation at the place of two used operands
        pass
    elif operators_working[x] == '-':
        # Difference
        # result = detract(operands[x], operands[x+1])
        # results_working.append(result)
        pass
