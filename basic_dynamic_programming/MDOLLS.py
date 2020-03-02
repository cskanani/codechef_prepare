def get_fit(mem, doll):
    left = 0
    right = len(mem)-1
    while left <= right:
        mid = (left + right) // 2
        if mem[mid][0] == doll[0] or mem[mid][1] <= doll[1]:
            left = mid + 1
        else:
            right = mid - 1
    return left

for _ in range(int(input())):
    num_dolls = int(input())
    dolls_info_unformatted = list(map(int, input().split()))
    dolls_info = []
    for i in range(num_dolls):
        width, height = dolls_info_unformatted[2*i], dolls_info_unformatted[2*i+1]
        dolls_info.append((width, height))
    dolls_info.sort(key = lambda x: (-x[0], x[1]))
    mem = []
    mem.append(dolls_info[0])
    for i in range(1, num_dolls):
        replace_ind = get_fit(mem, dolls_info[i])
        if replace_ind == len(mem):
            mem.append(dolls_info[i])
        else:
            mem[replace_ind] = dolls_info[i]
    print(len(mem))
