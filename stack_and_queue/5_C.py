bracket_string = input()
stack = []
max_len = 0
max_len_count = 1
for i in range(len(bracket_string)):
    if bracket_string[i] == ')' and stack and bracket_string[stack[-1]] == '(':
        stack.pop()
        if stack:
            cur_left_index = stack[-1]
        else:
            cur_left_index = -1
        cur_len = i - cur_left_index
        if cur_len > max_len:
            max_len = cur_len
            max_len_count = 1
        elif cur_len == max_len:
            max_len_count += 1
    else:
        stack.append(i)
print(max_len, max_len_count)
