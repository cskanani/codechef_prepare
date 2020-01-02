for _ in range(int(input())):
    expression = input()
    stack = []
    max_valid_length = 0
    for i in range(len(expression)):
        if expression[i] == '>' and stack and expression[stack[-1]] == '<':
            stack.pop()
            if not stack:
                max_valid_length = i + 1
        else:
            stack.append(i)
    print(max_valid_length)
