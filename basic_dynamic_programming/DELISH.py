for _ in range(int(input())):
    num_ingredients = int(input())
    delish_values = list(map(int, input().split()))
    prefix_max = [0]*num_ingredients; prefix_max[0] = delish_values[0]
    prefix_min = [0]*num_ingredients; prefix_min[0] = delish_values[0]
    suffix_max = [0]*num_ingredients; suffix_max[-1] = delish_values[-1]
    suffix_min = [0]*num_ingredients; suffix_min[-1] = delish_values[-1]
    for i in range(1, num_ingredients):
        prefix_max[i] = max(prefix_max[i-1] + delish_values[i], delish_values[i])
        prefix_min[i] = min(prefix_min[i-1] + delish_values[i], delish_values[i])
        suffix_max[num_ingredients-1-i] = max(
            suffix_max[num_ingredients-i] + delish_values[num_ingredients-1-i], 
            delish_values[num_ingredients-1-i]
        )
        suffix_min[num_ingredients-1-i] = min(
            suffix_min[num_ingredients-i] + delish_values[num_ingredients-1-i], 
            delish_values[num_ingredients-1-i]
        )
    for i in range(1, num_ingredients):
        prefix_max[i] = max(prefix_max[i], prefix_max[i-1])
        prefix_min[i] = min(prefix_min[i], prefix_min[i-1])
        suffix_max[num_ingredients-1-i] = max(
            suffix_max[num_ingredients-1-i], 
            suffix_max[num_ingredients-i]
        )
        suffix_min[num_ingredients-1-i] = min(
            suffix_min[num_ingredients-1-i], 
            suffix_min[num_ingredients-i]
        )
    max_delish = max(
        prefix_max[0]-suffix_min[1], 
        suffix_max[num_ingredients-1] - prefix_min[num_ingredients-2]
    )
    for i in range(1, num_ingredients - 1):
        max_delish = max(
            max_delish, 
            abs(prefix_max[i] - suffix_min[i+1]),
            abs(suffix_max[i] - prefix_min[i-1])
        )
    print(max_delish)
