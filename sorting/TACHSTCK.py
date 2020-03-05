num_sticks, max_diff = map(int, input().split())
stick_lens = []
for stick_i in range(num_sticks):
    stick_lens.append(int(input()))
stick_lens.sort()
stick_i = 0
num_pairs = 0
while stick_i+1 < num_sticks:
    if stick_lens[stick_i+1] - stick_lens[stick_i] <= max_diff:
        num_pairs += 1
        stick_i += 1
    stick_i += 1
print(num_pairs)
