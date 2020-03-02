from math import gcd
from collections import defaultdict
for _ in range(int(input())):
    num_elements = int(input())
    num_list = list(map(int, input().split()))
    mem = [defaultdict(int) for i in range(num_elements)]
    mem[0][num_list[0]] = 1
    for num_i in range(1, num_elements):
        mem[num_i][num_list[num_i]] += 1
        for prev_num_i in range(num_i):
            for divisor in mem[prev_num_i]:
                mem[num_i][gcd(num_list[num_i], divisor)] += mem[prev_num_i][divisor]
    required_sub_seq_count = 0
    for num_i in range(num_elements):
        required_sub_seq_count += mem[num_i][1]
    print(required_sub_seq_count)
