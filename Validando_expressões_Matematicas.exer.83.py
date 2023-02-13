def is_balanced(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            else:
                stack.pop()
    return not stack
expression = input('Digite a expressão: ')
if is_balanced(expression):
    print('A expressão esta correta !')
else:
    print('A expressão esta errada !')
    