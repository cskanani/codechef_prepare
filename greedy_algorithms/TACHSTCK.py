num_chopstics, allowed_diff = map(int, input().split())
chopstic_lengths = []
for i_chopstic in range(num_chopstics):
    chopstic_lengths.append(int(input()))
chopstic_lengths.sort()

possible_pairs = 0
i = 1
while i < num_chopstics:
    if chopstic_lengths[i] - chopstic_lengths[i-1] <= allowed_diff:
        possible_pairs += 1
        i += 1
    i += 1
print(possible_pairs)
