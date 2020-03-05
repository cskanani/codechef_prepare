from collections import Counter
for _ in range(int(input())):
    num_sticks = int(input())
    stick_lens = Counter(map(int, input().split()))
    max_len = -1
    second_max_len = -1
    for stick_len in stick_lens:
        if stick_lens[stick_len] >= 4:
            if stick_len > max_len:
                max_len = stick_len
                second_max_len = stick_len
            elif stick_len > second_max_len:
                second_max_len = stick_len
        elif stick_lens[stick_len] >= 2:
            if stick_len > max_len:
                second_max_len = max_len
                max_len = stick_len
            elif stick_len > second_max_len:
                second_max_len = stick_len
    if max_len != -1 and second_max_len != -1:
        print(max_len * second_max_len)
    else:
        print(-1)
