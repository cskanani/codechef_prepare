for _ in range(int(input())):
    array_size = int(input())
    array = list(map(int, input().split()))
    max_alternating_array = [1]*array_size
    i = array_size - 2
    while i > -1:
        if (
            (array[i] > 0 and array[i+1] < 0)
            or (array[i] < 0 and array[i+1] > 0)
        ):
            max_alternating_array[i] = max_alternating_array[i+1] + 1
        i -= 1
    print(' '.join(map(str, max_alternating_array)))
