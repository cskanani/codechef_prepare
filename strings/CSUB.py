for _ in range(int(input())):
    string_len = int(input())
    num_of_ones = input().count('1')
    # rquired strings = strings starting and ending with '1'
    num_of_rquired_strings = num_of_ones * (num_of_ones + 1) // 2
    print(num_of_rquired_strings)
