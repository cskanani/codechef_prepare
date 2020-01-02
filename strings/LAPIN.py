from math import ceil
from collections import Counter
for _ in range(int(input())):
    string = input()
    string_len = len(string)
    left_char_count = Counter(list(string[:string_len//2]))
    right_char_count = Counter(list(string[ceil(string_len/2):]))
    if left_char_count == right_char_count:
        print('YES')
    else:
        print('NO')
