base = ord('a')
char_list = [ord(char) - base for char in list(input())] # string converted to intiger list with a-z having value 0-25
min_string = ''
char_count = [0] * 26
stack = []

for x in char_list:
    char_count[x] += 1

cur_min_char = 0
for i in range(26):
    if char_count[i]:
        cur_min_char = i
        break
    
for x in char_list:
    if x == cur_min_char:
        min_string += chr(x + base)
        char_count[x] -= 1
        if char_count[x] == 0:
            cur_min_char = 0
            for i in range(26):
                if char_count[i]:
                    cur_min_char = i
                    break
            while stack and stack[-1] <= cur_min_char:
                min_string += chr(stack.pop() + base)
    else:
        stack.append(x)
        char_count[x] -= 1
while stack:
    min_string += chr(stack.pop() + base)
print(min_string)
