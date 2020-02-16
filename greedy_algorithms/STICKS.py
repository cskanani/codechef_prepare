from collections import Counter
for _ in range(int(input())):
    num_sticks = int(input())
    stick_lens_count = Counter(map(int, input().split()))
    max_stick_len = 0
    second_max_stick_len = 0
    for stick_len in stick_lens_count:
        if stick_lens_count[stick_len] > 3:
            if stick_len > max_stick_len:
                max_stick_len = stick_len
                second_max_stick_len = stick_len
            elif stick_len > second_max_stick_len:
                second_max_stick_len = stick_len
        elif stick_lens_count[stick_len] > 1:
            if stick_len > max_stick_len:
                second_max_stick_len = max_stick_len
                max_stick_len = stick_len
            elif stick_len > second_max_stick_len:
                second_max_stick_len = stick_len
    area = max_stick_len * second_max_stick_len 
    if area:
        print(area)
    else:
        print(-1)
