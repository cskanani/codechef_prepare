from itertools import permutations

def get_fit(color_perm, mem, card):
    left = 0
    right = len(mem) - 1
    while left <= right:
        mid = (left + right) // 2
        if color_perm.index(mem[mid][0]) > color_perm.index(card[0]):
            right = mid - 1
        elif color_perm.index(mem[mid][0]) < color_perm.index(card[0]):
            left = mid + 1
        elif mem[mid][1] > card[1]:
            right = mid - 1
        else:
            left = mid + 1
    return left

num_colors, num_cards = map(int, input().split())
cards = []
for i in range(num_colors * num_cards):
    color, card = map(int, input().split())
    cards.append((color, card))

longest_iss = 0
for color_perm in permutations(list(range(1, num_colors + 1))):
    mem = []
    mem.append(cards[0])
    for i in range(1, num_colors * num_cards):
        replace_ind = get_fit(color_perm, mem, cards[i])
        if replace_ind == len(mem):
            mem.append(cards[i])
        else:
            mem[replace_ind] = cards[i]
    longest_iss = max(longest_iss, len(mem))
print(num_colors * num_cards - longest_iss)
