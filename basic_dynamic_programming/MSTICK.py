def get_fit(height_mem, stick_height):
    left = 0
    right = len(height_mem) - 1
    while left <= right:
        mid = (left + right) // 2
        if height_mem[mid] == stick_height:
            return mid
        elif height_mem[mid] > stick_height:
            left = mid + 1
        else:
            right = mid - 1
    return left
    
for _ in range(int(input())):
    num_sticks = int(input())
    sticks_info_unformatted = list(map(int, input().split()))
    sticks_info = []
    for i in range(num_sticks):
        length, weight = sticks_info_unformatted[2*i], sticks_info_unformatted[2*i+1]
        sticks_info.append((length, weight))
    sticks_info.sort()
    height_mem = []
    height_mem.append(sticks_info[0][1])
    for i in range(1, num_sticks):
        add_ind = get_fit(height_mem, sticks_info[i][1])
        if add_ind == len(height_mem):
            height_mem.append(sticks_info[i][1])
        else:
            height_mem[add_ind] = sticks_info[i][1]
    print(len(height_mem))
