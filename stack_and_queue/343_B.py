wire_sequence = input()
stack = []
for x in wire_sequence:
    if stack and stack[-1] == x:
        stack.pop()
    else:
        stack.append(x)
if stack:
    print('No')
else:
    print('Yes')
