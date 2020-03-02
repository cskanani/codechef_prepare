for _ in range(int(input())):
    array_size, k = map(int, input().split())
    array = map(int, input().split())
    possible_xors = [False]*(1024)
    possible_xors[0] = True
    for element in array:
        for i in range(1024):
            possible_xors[i] = possible_xors[i] or possible_xors[i^element]
    max_value = k
    for i in range(1024):
        if possible_xors[i]:
            max_value = max(max_value, i^k)
    print(max_value)
