for _ in range(int(input())):
    bracket_expression = input()
    reverse_polish_expression = ''
    operator_stack = []
    for i in range(len(bracket_expression)):
        if bracket_expression[i] == ')':
            reverse_polish_expression += operator_stack.pop()
        elif bracket_expression[i] in '+-*/^':
            operator_stack.append(bracket_expression[i])
        elif bracket_expression[i] != '(':
            reverse_polish_expression += bracket_expression[i]
    print(reverse_polish_expression)
