for test_case in range(int(input())):
    num_chicks, min_req_chicks, barn_location, max_time = map(int, input().split())
    remaining_distances = [barn_location - int(chick_location) for chick_location in input().split()]
    speed = list(map(int, input().split()))
    total_swaps = 0
    swaps_for_chick = 0
    i = num_chicks - 1
    while i > -1 and min_req_chicks:
        if speed[i] * max_time >= remaining_distances[i]:
            min_req_chicks -= 1
            total_swaps += swaps_for_chick
        else:
            swaps_for_chick += 1
        i -= 1
    if min_req_chicks:
        total_swaps = 'IMPOSSIBLE'
    print('Case #{}: {}'.format(test_case+1, total_swaps))
