from sys import stdin
import bisect
input = stdin.readline
num_frogs, max_distance, num_pairs = map(int, input().split())
frog_positions = list(map(int, input().split()))
sorted_positions = sorted(frog_positions)
max_left = {}
max_left[sorted_positions[0]] = sorted_positions[0]
for i in range(1, num_frogs):
    if sorted_positions[i] - sorted_positions[i-1] <= max_distance:
        max_left[sorted_positions[i]] = max_left[sorted_positions[i-1]]
    else:
        max_left[sorted_positions[i]] = sorted_positions[i]

for i in range(num_pairs):
    frog1, frog2 = map(int, input().split())
    frog1_position = frog_positions[frog1-1]
    frog2_position = frog_positions[frog2-1]
    if (
        (max_left[frog2_position] <= frog1_position <= frog2_position)
        or (max_left[frog1_position] <= frog2_position <= frog1_position)
    ):
        print('Yes')
    else:
        print('No')
